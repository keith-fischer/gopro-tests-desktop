#!/usr/bin/python
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# File: GpCloudManager.py
# Description: Provides a utility to manage GoPro Cloud content
# Author: Sean Foley
# Date Created: 25 May 2016
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

import os
import sys, getopt
import json
sys.path.append(os.path.abspath('..'))
import logging
import datetime
#import pprint
#import qatoolbox
import rauth
import requests
# from rauth.utils import parse_utf8_qsl
import utils
import gda_sqllite_reader
import MedialistAnalysis

logging.basicConfig(filename='GpCloudManager.log',level=logging.DEBUG, stream=sys.stdout)
class GpCloudMediaDerivative(object):
    allFields = [
        'id',
        'available',
        'bitrate',
        'camera_positions',
        'created_at',
        'file_extension',
        'file_size',
        'fps',
        'gopro_user_id',
        'gumi',
        'height',
        'item_count',
        'label',
        'medium_id',
        'profile',
        'transcode_source',
        'type',
        'updated_at',
        'width'
    ]

    def __init__(self, jsonRep):
        """
        :param jsonRep:
            { u'available': True,
              u'gumi': u'0f0f68d861316412975ae7b62a87a798',
              u'id': u'591578617494897833',
              u'item_count': 1,
              u'medium_id': u'vOKkQybblo4e',
              u'profile': None,
              u'transcode_source': None,
              u'type': u'ProxyVideo',
              ...
            },

        """
        for key in jsonRep:
            self.__dict__.setdefault(key, jsonRep[key])

    def __str__(self):
        desc = self.id
        if self.__dict__.get("medium_id") is not None:
            desc += " (%s)" % self.medium_id

        return desc

class GpCloudMediaItem(object):
    allFields = [
        'id',
        'camera_metadata',
        'camera_model',
        'camera_positions',
        'captured_at',
        'client_updated_at',
        'composition',
        'content_description',
        'content_source',
        'content_title',
        'content_type',
        'created_at',
        'external_url',
        'file_extension',
        'file_location_url',
        'file_size',
        'filename',
        'fov',
        'gopro_user_id',
        'item_count',
        'location',
        'location_name',
        'moments_count',
        'music_track_artist',
        'music_track_name',
        'on_public_profile',
        'parent_id',
        'play_as',
        'products',
        'ready_to_view',
        'resolution',
        'revision_number',
        'source_duration',
        'source_gumi',
        'submitted_at',
        'tags',
        'token',
        'type',
        'updated_at',
        'verticals'
    ]

    def __init__(self, jsonRep):
        """
        :param jsonRep: {u'file_extension': u'jpg', u'filename': u'', u'id': u'zyzbZekQo9WR', ...}
        """
        for key in jsonRep:
            self.__dict__.setdefault(key, jsonRep[key])

    def __str__(self):
        desc = self.id
        if self.__dict__.get("filename") is not None:
            desc += " (%s" % self.filename
            if self.__dict__.get("file_extension") is not None:
                desc += ".%s" % self.file_extension
            desc += ")"

        return desc

class GpAccessToken(object):
    def __init__(self, json):
        """
        :param json:
            {u'access_token': u'6ad33b353085b6b7e505989101ec18a5681e4aed12c81c33f7e73460eff6ac86',
             u'expires_in': 21600,
             u'refresh_token': u'a066498fdbe61647acc03258d057be470d11d6dafdf7c7b2b4ca5623125d7fac',
             u'resource_owner_id': u'034d3b6e-3681-4c8d-9905-90ebd173a406',
             u'scope': u'upload me public',
             u'token_type': u'bearer'
            }
        """
        #self.access_token=object
        self.expires = datetime.datetime.now()
        self.updated = datetime.datetime.now()
        for key in json:
            self.__dict__.setdefault(key, json[key])
            if key == "expires_in":
                self.expires = self.updated + datetime.timedelta(seconds=json[key])

    def isExpired(self):
        now = datetime.datetime.now()
        return self.expires <= now

    def __str__(self):
        return self.access_token


class GpCloudManager(object):

    SYSTEMS = {
        "production": {
            "description": "GoPro Production",
            "base_url": "https://api.gopro.com",
            "access_token_url": "https://api.gopro.com/v1/oauth2/token",
            "authorize_url": "https://api.gopro.com/v1/oauth2/authorize"
        },

        "qa": {
            "description": "GoPro QA",
            "base_url": "https://api.qa.gopro.com",
            "access_token_url": "https://api.qa.gopro.com/v1/oauth2/token",
            "authorize_url": "https://api.qa.gopro.com/v1/oauth2/authorize"
        },

        "staging": {
            "description": "GoPro Staging",
            "base_url": "https://api.staging.gopro.com",
            "access_token_url": "https://api.staging.gopro.com/v1/oauth2/token",
            "authorize_url": "https://api.staging.gopro.com/v1/oauth2/authorize"
        }
    }
    # "production": {
    #                   "client_id": "caf2e380f57e41526a0d8ff77f74b356b3eb9ff4e15cc0242be9b2ac71964d9f",
    #                   "client_obfs_secret": "f332cfe64b40df654b06124a39a435f55dd1de08d12277784795587817018065",
    #                   "client_secret": "6fa55a297cdd8a8b98f8d6df4e0dab8d6758ca878faa09eb84e7463cb7e8a0f4",
    #                   "access_token": "161ed60c50a82de0a4f7c8bddd9c6fc903312aa5a631df13ee180da80d4b613b",
    #                   "profile_id": "fb21027d-cce9-4b52-aa0d-5c2d911a5968"
    #               },

    # This stuff comes from various sources and is likely be stale
    # One such source: https://wiki.gopro.com/pages/editpage.action?pageId=78783496
    # Another: git://git@github.com:generalthings/gopro-sdk-jakarta/test/gpsdk_jakarta_unittest/main.c
    CLIENTS = {
        "gda": {
            "production": {
                "client_id": "caf2e380f57e41526a0d8ff77f74b356b3eb9ff4e15cc0242be9b2ac71964d9f",
                "client_obfs_secret": "f332cfe64b40df654b06124a39a435f55dd1de08d12277784795587817018065",
                "client_secret": "6fa55a297cdd8a8b98f8d6df4e0dab8d6758ca878faa09eb84e7463cb7e8a0f4",
            },
            "qa": {
                "client_id": "077d808c0e58f7d91bb454ae9f734e4d79df4e3ad9b4303dd3994e496c4e0f50",
                "client_obfs_secret": "7fa179aad88ed03018b93d4c196df144b0725fe48bfa07053d1515b49cc041a4",
                "client_secret": "5fd83c7356c83006ff991fe84faea8ca37e82243d253293e48a07efd92ac8bfb"
            },
            "staging": {
                "client_id": "b961e40c5163e2adbf68e392a948611eace48d2e7e85b3d733d4abec04329cbc",
                "client_obfs_secret": "f8ab0fa2a6af16517187338c8053522e57dbc61446ef43afe141d9ebcd0732ed",
                "client_secret": "7cb594146a104ad5598f59325bf85ed8e59f54c00da19cf98962277441e10650"
            }
        },
        "webbrowser": {
            "production": {
                "client_id": "caf2e380f57e41526a0d8ff77f74b356b3eb9ff4e15cc0242be9b2ac71964d9f",
                "client_obfs_secret": "f332cfe64b40df654b06124a39a435f55dd1de08d12277784795587817018065",
                "client_secret": "6fa55a297cdd8a8b98f8d6df4e0dab8d6758ca878faa09eb84e7463cb7e8a0f4",
            },
            "qa": {
                "client_id": "077d808c0e58f7d91bb454ae9f734e4d79df4e3ad9b4303dd3994e496c4e0f50",
                "client_obfs_secret": "7fa179aad88ed03018b93d4c196df144b0725fe48bfa07053d1515b49cc041a4",
                "client_secret": "5fd83c7356c83006ff991fe84faea8ca37e82243d253293e48a07efd92ac8bfb"
            },
            "staging": {
                "client_id": "fcd366ea8af4e72cf7afa01c701b9a08265eb9eb1d15b8e9c30c926350a78410",
                "client_obfs_secret": "f8ab0fa2a6af16517187338c8053522e57dbc61446ef43afe141d9ebcd0732ed",
                "client_secret": "d8d24a7b28e9f66796a71128d6900ba0d041bbb31f466d9494f4b2a2c36bf8b2"
            }
        },

        "mr": {
            "production": {
                "client_id": "e9677bed89e10da1cfa95acaa6d2a89bec6191c78567e573417e73f06d4c639e",
                "client_obfs_secret": "f332cfe64b40df654b06124a39a435f55dd1de08d12277784795587817018065",
                "client_secret": "d34b8a3fc5063f53ac2630ee6f676c7bda4ba3af888b594332203331196d4a3a"
            },
            "qa": {
                "client_id": "077d808c0e58f7d91bb454ae9f734e4d79df4e3ad9b4303dd3994e496c4e0f50",
                "client_obfs_secret": "7fa179aad88ed03018b93d4c196df144b0725fe48bfa07053d1515b49cc041a4",
                "client_secret": "5fd83c7356c83006ff991fe84faea8ca37e82243d253293e48a07efd92ac8bfb"
            },
            "staging": {
                "client_id": "fcd366ea8af4e72cf7afa01c701b9a08265eb9eb1d15b8e9c30c926350a78410",
                "client_obfs_secret": "f8ab0fa2a6af16517187338c8053522e57dbc61446ef43afe141d9ebcd0732ed",
                "client_secret": "d8d24a7b28e9f66796a71128d6900ba0d041bbb31f466d9494f4b2a2c36bf8b2"
            }
        },
        "smarty": {
            "production": {
                "client_id": "e3b75b56b490e6cc7946b6a487c6df207945d98e46e036e72022a456c3559385",
                "client_obfs_secret": "4e8b54176193cbc628ebd0ad3306aaca6b70099e42bac7898860843a75c0b3e7",
                "client_secret": "6ef211ceefd52bf0cfcbf20965c5f344ecea74391b13e9b2fdd5ef737bac79b8"
            },
            "qa": {
                "client_id": "c0b72ddcdce5dea0c0b36dff0a66162fc0b596e43b1a789be37de70b7f006b4d",
                "client_obfs_secret": "b13fbebd4d54c1dc53fc9ec8e92baa1c51b37204de707b2a4db3ffd6e573125b",
                "client_secret": "9146fb64c31221eab4dcbc6cbfe8f392d6290fa387d955113806949feb1fd804"
            },
            "staging": {
                "client_id": "6d668ccf1d16fad7910f583e699ffc16903b52ddb0de927bcde291f1e694afd6",
                "client_obfs_secret": "58f7c7c73affedd34dabca34f05f10000000000000000bc423512faaa1254199",
                "client_secret": "788e821eb4b90de5aa8be890a69c498e879a7da759a925ff56e444e3af498bc6"
            }
        },
        "streaky": {
            "production": {
                "client_id": "71611e67ea968cfacf45e2b6936c81156fcf5dbe553a2bf2d342da1562d05f46",
                "client_obfs_secret": "181a8c6db6869bb414ba914ab83a9bc1683f71cf0f8c100468828baabf861cd2",
                "client_secret": "3863c9b438c07b82f39ab3eeeef9c24fefa50c6856253e3f1d37e0e3b1ead68d",
                "access_token": "88d72f3653a9b79c01e04cfd0c10a192acbf5f809563397ee77a1c8a0265109a",
                "profile_id":"a66cb492-47f1-4308-b102-529e0ba0a27e"
            },
            "qa": {
                "client_id": "dde50f6bc96fca548c095aebfda01ae9937eb7b5331d9206044bb485f2c0eaf6",
                "client_obfs_secret": "0617d2cd63c7131b5bf7af14187580f22f457e174bd4566728e8d74a9117d8c1",
                "client_secret": "266e9714ed81f32dbcd78db04eb6d97ca8df03b0127d785c5d5dbc039f7b129e"
            },
            "staging": {
                "client_id": "98134d8dc380746a87e279e3e52cf1d972d274ed6c82e9854b38f825d78ab790",
                "client_obfs_secret": "78b6f059d0832d0f2351decd5285f63bd24e70812a43b83b1818d678ca22ebae",
                "client_secret": "58cfb5805ec5cd39c471fc690446afb555d40d2673ea96006dadbd31c44e21f1"
            }
        }
    }

    OBFUSCATION_KEYS = [
        "c0b596e43b1a789be37de70b7f006b4d6ef211ceefd52bf0cfcbfa66162ff984",
        "6d668ccf1d16fad7910f583e699ffc16903b52ddb0de927bcde291f1e694afd6",
        "f56e444e3af984bc7946b6a487c6df207945d98e46e036e72022a456c3559385",
        "207945d98e46e036e72022a456c3598e879a7da759a92e3b75b56b490e6cca5f",
        "20965c5f344e788e821eb13e9b2fdd5ec0b72ddcdce5dea0c0b36dff0a66162f"
    ]

    #logger = qatoolbox.Logger(qatoolbox.Logger.LOG_LEVEL_INFO)
    logger = logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    def __init__(self, system="production", client="gda", username=None, password=None, clientid=None,obfs_client_secret=None,client_secret=None):
        """
        Initializer
        logger = logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
        :param username: The username (i.e. email address) used to access GoPro's cloud API
        :param password: The password used to access GoPro's cloud API
        :param system: Name of an entry from GpCloudManager.SYSTEMS (i.e. "production")
        :return: None
        """

        # if username is None:
        #     username = os.environ.get("GOPRO_CLOUD_USERNAME")
        #
        # if password is None:
        #     password = os.environ.get("GOPRO_CLOUD_PASSWORD")

        self.__username = username
        self.__password = password
        self.__accessToken = None

        self.__client = GpCloudManager.CLIENTS.get(client)
        if self.__client is None:
            self.logger.logError("Can't find keys for client: %s" % client)
            sys.exit(1)

        self.__system = GpCloudManager.SYSTEMS.get(system)
        if self.__system is not None:
            # Sanity check
            for key in ('description', 'base_url', 'access_token_url', 'authorize_url'): #, 'client_id', 'client_secret'):
                if key not in self.__system:
                    logging.error("Expected key '%s' not found in system\n%s" % (key, str(self.__system))) #pprint.pformat(self.__system)))
                    sys.exit(1)

            # override client_id and secret if they're set in the environment
            client_id=clientid
            if not client_id:
                client_id = os.environ.get("GOPRO_CLOUD_CLIENT_ID")
            if client_id is not None:
                self.__client[system]['client_id'] = client_id

            #if obfs_client_secret is None:
            #    obfs_client_secret = os.environ.get("GOPRO_CLOUD_CLIENT_OBFS_SECRET")
            if obfs_client_secret is not None:
                self.__client[system]['client_obfs_secret'] = obfs_client_secret
                self.__client[system]['client_secret'] = GpCloudManager.obfuscateClientSecret(obfs_client_secret,3)
                #self.__system['client_secret'] = GpCloudManager.obfuscateClientSecret(client_secret)

            # GpCloudManager.logger.logDebug("Setting up auth service with client: %s, config: %s" % (pprint.pformat(self.__client[system]), pprint.pformat(self.__system)))
            self.__authService = rauth.OAuth2Service(
                client_id=self.__client[system]["client_id"],
                client_secret=self.__client[system]["client_secret"],
                name=self.__system["description"],
                authorize_url=self.__system["authorize_url"],
                access_token_url=self.__system["access_token_url"],
                base_url=self.__system["base_url"]
            )

    @staticmethod
    def obfuscateClientSecret(secret, keyIndex = 3):
        """
        Client Secret Obfuscation is discussed here: https://wiki.gopro.com/pages/viewpage.action?spaceKey=SST&title=Camera+as+a+HUB+HLD#CameraasaHUBHLD-ClientSecretObfuscation
        Client secret is stored in CSI in an obfuscated string. Retrieve with something like:
            a:\>t api wireless csi_get CSI_CAH_CLIENT_SECRET
        Pass the obfuscated string to this function and (optionally) choose a key index to de/obfuscate with
        :param secret: obfuscated secret
        :param keyIndex:
        :return: de-obfuscated secret (or None on failure)
        """
        logging.info("secret: %s, keyIndex: %d" % (secret, keyIndex))
        result = None
        obfsKey = GpCloudManager.OBFUSCATION_KEYS[keyIndex]

        if secret is None:
            logging.error("No secret provided")
            return result

        if len(secret) != 64:
            logging.error("Invalid secret (len(%s) != 64)" % secret)
            return result

        logging.info("Chosen obfuscation string: %s" % obfsKey)

        obfsSecret = ""
        for i in range(len(secret)):
            src = int(secret[i], 16)
            key = int(obfsKey[i], 16)
            obfsSecret += "%x" % (src ^ key)

        result = obfsSecret
        logging.info("%s -> %s" % (secret, result))

        return result

    def authenticatedRequest(self, path, **kwargs):
        """

        :param path:
        :param kwargs:
        :return:
        """
        headers = {
            'Accept': 'application/vnd.gopro.jk.media+json; version=2.0.0',
            'Accept-Charset': 'utf-8',
            'Content-Type': 'application/json',
        }
        addlHeaders = kwargs.get("headers")
        if addlHeaders is not None:
            headers.update(addlHeaders)

        params = {}
        addlParams = kwargs.get("params")
        if addlParams is not None:
            params.update(addlParams)

        data = {}
        addlData = kwargs.get("data")
        if addlData is not None:
            data.update(addlData)

        url = path % self.__system['base_url']
        token = self.accessToken()
        self.token=token
        if token:
            session = self.__authService.get_session(str(token))
            response = session.get(url, params=params, headers=headers, data=data)

            try:
                response.raise_for_status()
                responseJson = response.json()
            except:
                GpCloudManager.logger.logError("Unexpected response from GoPro server:")
                #traceback.print_exc()
                return None

        #GpCloudManager.logger.logDebug("\nResponse:\n%s" % pprint.pformat(responseJson))

            return responseJson
        else:
            print "failed to get token"
            return None


    def accessToken(self):
        if self.__accessToken is None or self.__accessToken.isExpired():
            # headers = {
            #     "Accept": "application/vnd.gopro.jk.oauth-identity+json; version=1.0.0"
            # }
            # headers = {
            #     'Content-Type': 'application/json'
            # }
            # data = {
            #     "username": self.__username,
            #     "password": self.__password,
            #     "grant_type": "password",
            #     "scope": "public media_library_beta me root upload"
            # }
            data = {
                "username": self.__username,
                "password": self.__password,
                "grant_type": "password",
                "scope": "public me upload winter_alpha media_library_beta search root",
            }

            token = self.__authService.get_raw_access_token(method='POST',
#                                                                headers=headers,
                                                               data=data)
            #print str(jdata.__dict__)
            if token and token.status_code==200:
                tokenJson=token.json()
                logging.info("token: %s" % str(tokenJson))
                self.__accessToken = GpAccessToken(tokenJson)

        return self.__accessToken

    def get_request(self,url,headers):
        response = requests.get(url, headers=headers)

        try:
            response.raise_for_status()
            responseJson = response.json()
        except:
            logging.error("Failed to retrieve json data with url %s" % url)
            logging.error("%s" % str(response.content))
            #traceback.print_exc()
            return None

        return responseJson

    def delete_request(self,url,headers):
        response = requests.delete(url, headers=headers)

        try:
            response.raise_for_status()
            responseJson = response.json()
        except:
            logging.error("Failed to delete_request with url %s" % url)
            logging.error("status:%s - %s" % (str(response.status_code),str(response.content)))
            #traceback.print_exc()
            return None

        return responseJson

    def getusershow(self, profileid):
        #https://{{base_url}}/v1/users/{{profile_id}}
        """
        Retrieve metadata for media with ID = mediaID
        :param mediaID: Alphanumeric media ID (similar to: d47vX1pGJEoN)
        :return: json-formatted metadata response or None
        """
        token=self.accessToken()
        if token:
            url = "%s/v1/users/%s" % (self.__system.get('base_url'), profileid)
            headers = {
                "Content-Type": "application/json",
                "Authorization":"Bearer %s" % str(token)
            }

            return self.get_request(url,headers)
        return None

    def deleteusermedia(self,mediaids):
        #DELETE / admin / media?gopro_user_id = d351df1b
        #DELETE /media?ids=8dba48179aa57cdad0,f8c203bf0c83d7551a,123abcd456
        #{{base_url}}/media?ids={{media_id}}
        ids = ", ".join(mediaids)
        url = "%s/media?ids=%s" % (self.__system.get('base_url'), ids)
        headers = {
            "Accept": "application/vnd.gopro.jk.media+json; version=2.0.0",
            "Content-Type":"application/json",
            "Authorization": "Bearer " + str(self.accessToken())
        }

        return self.delete_request(url, headers)

    def getprofile(self, profileid):
        #https://{{base_url}}/v1/accounts/{{profile_id}}
        """
        Retrieve metadata for media with ID = mediaID
        :param mediaID: Alphanumeric media ID (similar to: d47vX1pGJEoN)
        :return: json-formatted metadata response or None
        """
        url = "%s/v1/accounts/%s" % (self.__system.get('base_url'), profileid)
        headers = {
            "Accept": "application/vnd.gopro.jk.media+json; version=2.0.0"
        }

        return self.get_request(url, headers)

    def metadataForMediaID(self, mediaID):
        """
        Retrieve metadata for media with ID = mediaID
        :param mediaID: Alphanumeric media ID (similar to: d47vX1pGJEoN)
        :return: json-formatted metadata response or None
        """
        url = "%s/media/%s" % (self.__system.get('base_url'), mediaID)
        headers = {
            "Accept": "application/vnd.gopro.jk.media+json; version=2.0.0"
        }

        return self.get_request(url, headers)

    def metadataForMedia(self, media):
        return self.metadataForMediaID(media.id)

    def getDerivativeList(self, media, fields=GpCloudMediaDerivative.allFields):
        path = "%s/" + ("media/%s/derivatives" % media.id)
        fieldsParam = ", ".join(fields)
        params = {
            "fields": fieldsParam
        }

        responseJson = self.authenticatedRequest(path, params=params)
        logging.info("Derivative List JSON: %s" % str(responseJson))
        embedded = responseJson.get('_embedded')
        if embedded is None:
            logging.error("Unable to get embedded dict from response")#\nResponse: %s" % str(responseJson))
            return None

        list = embedded.get('derivatives')
        if list is None:
            logging.error("Unable to get derivatives list from response")#\nResponse: %s" % str(responseJson))
            return None

        mediaList = []
        for medium in list:
            mediaList.append(GpCloudMediaDerivative(medium))

        return mediaList

    def getMediaList(self, fields=GpCloudMediaItem.allFields):
        """
        JSON: { u'_pages': {
                    u'total_items': 8,
                    u'per_page': 10000,
                    u'current_page': 1,
                    u'total_pages': 1
                },
                u'_embedded': {
                    u'media': [
                        {u'gopro_user_id': u'034d3b6e-3681-4c8d-9905-90ebd173a406',
                            u'content_description': u'',
                            u'client_updated_at': u'2016-07-12T15:50:49Z',
                            u'file_extension': u'jpg',
                            u'updated_at': u'2016-07-12T22:51:44Z',
                            u'content_source': u'gp-cah-controller',
                            u'verticals': None,
                            u'revision_number': 16,
                            u'file_size': 123592767,
                            u'id': u'zyzbZekQo9WR',
                            u'filename': u'',
                            u'ready_to_view': u'ready',
                            u'captured_at': u'2016-05-31T05:16:42Z',
                            u'file_location_url': None,
                            u'fov': None,
                            u'location_name': u'',
                            u'content_title': u'',
                            u'music_track_artist': None,
                            u'token': u'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZWRpdW1faWQiOiI1OTE1NzQ5MDQxNzY5MDMxOTUiLCJvd25lciI6IjAzNGQzYjZlLTM2ODEtNGM4ZC05OTA1LTkwZWJkMTczYTQwNiIsImlzX3B1YmxpYyI6ZmFsc2V9.n9obLvnmwyVmxsNYqo8zN6dZZhraybFkZbCCZDjlWWo',
                            u'item_count': 52,
                            u'parent_id': None,
                            u'location': None,
                            u'camera_metadata': None,
                            u'type': u'TimeLapse',
                            u'composition': None,
                            u'tags': u'',
                            u'content_type': None,
                            u'source_gumi': u'0f0af12de572e27e26745b736b4f776a',
                            u'submitted_at': None,
                            u'play_as': u'multi_shot_photo',
                            u'source_duration': None,
                            u'created_at': u'2016-07-12T22:45:56Z',
                            u'camera_positions': u'default',
                            u'on_public_profile': False,
                            u'camera_model': None,
                            u'products': None,
                            u'moments_count': 0,
                            u'resolution': u'12000000',
                            u'music_track_name': None,
                            u'external_url': None
                        },
                        ...
                    ],
                    u'errors': [
                    ]
                }
              }

        :param fields:
        :return:
        """
        path = "%s/media/search"
        fieldsParam = ", ".join(fields)
        params = {
            "fields": fieldsParam,
            "per_page": 10000
        }

        responseJson = self.authenticatedRequest(path, params=params)
        if responseJson:
            #GpCloudManager.logger.logNoise("mediaList JSON: %s" % responseJson)
            embedded = responseJson.get('_embedded')
            if embedded is None:
                GpCloudManager.logger.logError("Unable to get embedded dict from response\nResponse: %s" % str(responseJson))
                return None

            list = embedded.get('media')
            if list is None:
                GpCloudManager.logger.logError("Unable to get media list from response\nResponse: %s" % str(responseJson))
                return None

            mediaList = []
            for medium in list:
                mediaList.append(GpCloudMediaItem(medium))

            return mediaList
        print "Error: No access to Media List"
        return None

def prod_streakytest():
    system = "production"
    client = "streaky"
    username = None
    password = None

    systemKeys = " | ".join(GpCloudManager.SYSTEMS)
    clientKeys = " | ".join(GpCloudManager.CLIENTS)

    if len(sys.argv) < 2 or len(sys.argv) == 4:
        print "Usage: %s [%s] [%s] [<email_address> <password>]" % (sys.argv[0], systemKeys, clientKeys)
        print "Example: %s production streaky user@gopro.com password1234" % sys.argv[0]
        print "Example: %s staging mr" % sys.argv[0]
        print "Example: %s qa" % sys.argv[0]
        print "Example: %s" % sys.argv[0]
        sys.exit(1)

    if len(sys.argv) >= 2:
        system = sys.argv[1]

    if len(sys.argv) == 3:
        system = sys.argv[1]
        client = sys.argv[2]

    if len(sys.argv) >= 5:
        username = sys.argv[3]
        password = sys.argv[4]

    config = GpCloudManager.SYSTEMS.get(system)
    if config is None:
        GpCloudManager.logger.logError("Unknown system: %s. Use one of: %s." % (system, ", ".join(GpCloudManager.SYSTEMS)))
        sys.exit(1)

    clientKeys = GpCloudManager.CLIENTS.get(client)
    if clientKeys is None:
        GpCloudManager.logger.logError("Unknown client: %s. Use one of: %s." % (client, ", ".join(GpCloudManager.CLIENTS)))
        sys.exit(1)

    if clientKeys.get(system) is None:
        GpCloudManager.logger.logError("Unknown key (%s) for client %s." % (system, client))
        sys.exit(1)

    clients = GpCloudManager.CLIENTS
    for c in clients:
        systems = clients[c]
        for s in systems:
            obfs_secret = clients[c][s]['client_obfs_secret']
            secret = clients[c][s]['client_secret']
            testSecret = GpCloudManager.obfuscateClientSecret(secret)
            if obfs_secret == testSecret:
                GpCloudManager.logger.logInfo("Validate keys for (%s, %s): PASS" % (s, c))
            else:
                GpCloudManager.logger.logError("Validate keys for (%s, %s): FAIL: %s != %s" % (s, c, obfs_secret, testSecret))


    gpCloudManager = GpCloudManager(system, client, username, password)

    mediaList = gpCloudManager.getMediaList()
    for item in mediaList:
        #print "Medium: %s" % item.__dict__
        metadata = gpCloudManager.metadataForMedia(item)
        print "Metadata: %s" % metadata
        derivatives = gpCloudManager.getDerivativeList(item)
        print "Derivatives:"
        for derivative in derivatives:
            print "\t%s" % derivative
"""
medialist
      {
        "type": "Video",
        "filename": "songBADBLOOD30.mp4",
        "ready_to_view": "uploading",
        "captured_at": "2016-09-22T18:01:05Z",
        "updated_at": "2016-10-11T19:24:22Z",
        "client_updated_at": "2016-10-11T19:24:14Z",
        "revision_number": 0,
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZWRpdW1faWQiOiI2NTc0MjgwMDU3ODk4OTM3NDgiLCJvd25lciI6ImZiMjEwMjdkLWNjZTktNGI1Mi1hYTBkLTVjMmQ5MTFhNTk2OCIsImlzX3B1YmxpYyI6ZmFsc2UsIm8iOjF9.-LhGQUGdEejThRdlNCiU5Fj3kvEjaeaUuHprd9cY-2A",
        "source_gumi": "2d3213df6f64c5ca0c82eb6d758475ef",
        "file_extension": "mp4",
        "id": "qLR9gJnB8L0r"
      }
   mediaindex
      {
        "id": "qLR9gJnB8L0r",
        "filename": "songBADBLOOD30.mp4",
        "type": "Video",
        "ready_to_view": "uploading",
        "created_at": "2016-10-11T19:24:18Z",
        "captured_at": "2016-09-22T18:01:05Z",
        "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtZWRpdW1faWQiOiI2NTc0MjgwMDU3ODk4OTM3NDgiLCJvd25lciI6ImZiMjEwMjdkLWNjZTktNGI1Mi1hYTBkLTVjMmQ5MTFhNTk2OCIsImlzX3B1YmxpYyI6ZmFsc2UsIm8iOjF9.-LhGQUGdEejThRdlNCiU5Fj3kvEjaeaUuHprd9cY-2A"
      }
    "derivatives": [
      {
        "height": 1080,
        "width": 1920,
        "type": "Source",
        "gumi": "2d3213df6f64c5ca0c82eb6d758475ef",
        "bitrate": 308906,
        "item_count": 1,
        "file_extension": "mp4",
        "id": "657428009396995189"
      }

"""

def class_to_dict(obj):
    rc={}
    if obj:
        rc=obj.__dict__
    return rc

def prod_quick_test(settings):

    #get media list
    #{{base_url}}/media/search?per_page=10000&fields=type,filename,ready_to_view,captured_at,updated_at,client_updated_at,revision_number,token,source_gumi,file_extension,source_gumi
    # get derivatives
    # {{base_url}}/media/{{media_id}}/derivatives?fields=height,width,type,gumi,bitrate,item_count,file_extension
    # get media details
    # {{base_url}}/media?ids={{media_id}}&fields=id,filename,type,ready_to_view,created_at,captured_at,token
    system = settings['targetcloud'] #"production"
    if "client" in settings:
        client = settings['client'] #"quik"

    username = settings["login"] #""autogda00@gmail.com"
    password = settings["password"] #""access4auto"
    cleanupdelete=False
    if "deletecleanup" in settings and settings["deletecleanup"]==True:
        cleanupdelete=True
    systemKeys = " | ".join(GpCloudManager.SYSTEMS)
    clientKeys = " | ".join(GpCloudManager.CLIENTS)
    if not system:
        if len(sys.argv) < 2 or len(sys.argv) == 4:
            print "Usage: %s [%s] [%s] [<email_address> <password>]" % (sys.argv[0], systemKeys, clientKeys)
            print "Example: %s production streaky user@gopro.com password1234" % sys.argv[0]
            print "Example: %s staging mr" % sys.argv[0]
            print "Example: %s qa" % sys.argv[0]
            print "Example: %s" % sys.argv[0]
            sys.exit(1)

        if len(sys.argv) >= 2:
            system = sys.argv[1]

        if len(sys.argv) == 3:
            system = sys.argv[1]
            client = sys.argv[2]

        if len(sys.argv) >= 5:
            username = sys.argv[3]
            password = sys.argv[4]

    config = GpCloudManager.SYSTEMS.get(system)
    if config is None:
        GpCloudManager.logger.logError("Unknown system: %s. Use one of: %s." % (system, ", ".join(GpCloudManager.SYSTEMS)))
        sys.exit(1)

    clientKeys = GpCloudManager.CLIENTS.get(client)
    if clientKeys is None:
        GpCloudManager.logger.logError("Unknown client: %s. Use one of: %s." % (client, ", ".join(GpCloudManager.CLIENTS)))
        sys.exit(1)

    if clientKeys.get(system) is None:
        GpCloudManager.logger.logError("Unknown key (%s) for client %s." % (system, client))
        sys.exit(1)

    clients = GpCloudManager.CLIENTS
    if "profile_id" in clients[client][system]:
        profileid=clients[client][system]["profile_id"]
    if "client_id" in clients[client][system]:
        clientid = clients[client][system]["client_id"]

    if "client_obfs_secret" in clients[client][system]:
        client_obfs_secret=clients[client][system]["client_obfs_secret"]
    if "client_secret" in clients[client][system]:
        client_secret=clients[client][system]["client_secret"]

    gpCloudManager = GpCloudManager(system, client, username, password, clientid, None,client_secret) #client_obfs_secret)

    clouddata={}
     #clientKeys['production']['profile_id']

    medialist = gpCloudManager.getMediaList()
    if hasattr(gpCloudManager,'token') and hasattr(gpCloudManager.token,'gpCloudManager.token.resource_owner_id'):
        profileid = gpCloudManager.token.resource_owner_id
        clouddata['profileinfo']=gpCloudManager.getprofile(profileid)
        clouddata['showinfo']=gpCloudManager.getusershow(profileid)
    if not medialist:
        return
    ut=utils.Utils()

    count=0
    clouddata['medialist']=[]
    clouddata['testreport']=[]
    tc=TestCounters()
    for item in medialist:
        try:
            count += 1
            if count > 9999:
                break
            # if "client" in settings and item.content_source !=settings["client"]:
            #     continue
            #print "Medium: %s" % item.__dict__
            derivativeList = gpCloudManager.getDerivativeList(item)
            meta = gpCloudManager.metadataForMedia(item)
            if not meta:
                meta = class_to_dict(item)
                #continue

            if meta:
                meta['derivativeList'] = {}
                if derivativeList:
                    meta['derivativeList']=[]
                    for item1 in derivativeList:
                        d = class_to_dict(item1)
                        meta['derivativeList'].append(d)
                testitem,tc,passfail,can_delete = evalmedia(meta,tc)
                if can_delete and cleanupdelete:
                    media_ids=[str(item.id)]

                    resp=gpCloudManager.deleteusermedia(media_ids)
                    if resp and len(resp)>0:
                        if "_embedded" in resp:
                            if len(resp["_embedded"]["media"])==1:
                                tc.addtest("DELETE_MEDIA", 1)
                                logging.info("DELETE_MEDIA %s" % meta['filename'])
                if testitem:
                    clouddata['testreport'].append(testitem)
                clouddata['medialist'].append(meta)


            #clouddata['metadata'].append(metadata)
            print "%d. Metadata: %s" % (count,meta['filename'])


        except Exception, e:
            logging.error(str(e))
            logging.error(str(item.__dict__))
            clouddata["results"] = class_to_dict(tc)
            ut.json_save(settings['jsonpath'], clouddata)
    clouddata["results"]=class_to_dict(tc)
    ut.json_save(settings['jsonpath'], clouddata)
    if 'csvpath' in settings:
        ut.dict_to_csv(settings['jsonpath'], settings['csvpath'])
def evalitem(key,d):
    if key in d and d[key]!=None and len(str(d[key]))>0:
        return True
    return False
def evalmedia(mediaitem, testcounters):
    rc = []
    passfail=False
    can_delete=False
    msg = None
    if not mediaitem:
        testcounters.addtest("no media: mediaitem=None",1)
        testcounters.addtest("FAILED", 1)
        print "evalmedia: no mediaitem"
        return None

    if evalitem("content_source" , mediaitem):
        testcounters.addtest("content_source:%s" % mediaitem["content_source"],1)
    if evalitem("type" , mediaitem):
        testcounters.addtest("type:%s" % mediaitem["type"],1)
    if evalitem("composition" , mediaitem):
        testcounters.addtest("composition:%s" % mediaitem["composition"])
    if evalitem("resolution" , mediaitem):
        testcounters.addtest("resolution:%s" % str(mediaitem["resolution"]))

    if evalitem("ready_to_view",mediaitem) and str(mediaitem["ready_to_view"]) != "ready":
        msg="ready_to_view: not ready, >%s<" % str(mediaitem["ready_to_view"])
        can_delete = True
    elif evalitem("upload_completed_at",mediaitem) and str(mediaitem["upload_completed_at"]) == "null":
        msg="mediaitem[\"upload_completed_at\"] == \"null\""
    elif evalitem("derivativeList" , mediaitem):
        for derive in mediaitem['derivativeList']:
            if evalitem("label",derive):
                testcounters.addtest("label:%s" % str(derive["label"]),1,"derivative")
            if evalitem("width" ,derive):
                testcounters.addtest("width:%s" % str(derive["width"]),1,"derivative")
            if evalitem("height", derive):
                testcounters.addtest("height:%s" % str(derive["height"]),1,"derivative")
            if evalitem("fps" , derive):
                testcounters.addtest("fps:%.2f" % float(derive["fps"]),1,"derivative")
            if evalitem("bitrate" , derive ):
                testcounters.addtest("bitrate:%.0f00000" % (float(derive["bitrate"])/100000),1,"derivative")
            if evalitem("file_size" , derive):
                testcounters.addtest("file_size:%.0f00000" % (float(derive["file_size"])/100000),1,"derivative")

            #eval for pass/fail
            if evalitem('available',derive):
                if derive['available'] != True:
                    if str(derive['label']) != 'source':
                        msg= "derivative-available=False"
                    break
    if msg:
        rc.append(msg)
        testcounters.addtest(msg, 1)
        testcounters.addtest("FAILED", 1)
        rc.append(mediaitem)
    else:
        passfail=True
        testcounters.addtest("PASSED", 1)
    return rc,testcounters,passfail,can_delete

def parseargs():
    argv=sys.argv[1:]
    settings={}
    settings["deletecleanup"] = False
    try:
        opts, args = getopt.getopt(argv, "hj:l:p:v:c:t:d:x:m:b:", ["jsonpath=", "login=","password=","validatepath=","client=", "targetcloud=","deletecleanup","csv=","mediadbpath=","dbjsonpath="])
    except getopt.GetoptError:
        print 'test.py -j <json output path> -l <login> -p <password> -v <validatepath> -c <client> -t <targetcloud> -x <csv>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print '-j <json output path> -l <login> -p <password>  -c <client> -t <targetcloud> -v <validatepath> -d <deletecleanup>'
            print '-j <json output path> path to output json file name'
            print '-l <login> the cloud account email'
            print '-p <pasword> the cloud account password'
            print '-c <client> the client gda|webbrowser'
            print '-t <targetcloud> the cloud environment prod|staging|qa'
            print '-d <deletecleanup> cleanup invalid media items in cloud account such as failed uploads'
            print '-x <csv> outputs a csv file for excel import'
            print '-m <mediadbpath> path to Quik(GDA) sqlite db file. (does not write,update or delete records,only read)'
            print '-b <dbjsonpath> path to output json file sqlite db data snapshot'

            sys.exit()

        elif opt in ("-j", "--jsonpath"):
            settings['jsonpath'] = arg
        elif opt in ("-l", "--login"):
            settings['login'] = arg
        elif opt in ("-p", "--password"):
            settings['password'] = arg
        elif opt in ("-v", "--validatepath"):
            settings['validatepath'] = arg
        elif opt in ("-c", "--client"):
            settings['client'] = arg
            if settings['client']=="quik":
                settings['client']="gda"
        elif opt in ("-t", "--targetcloud"):
            settings['targetcloud'] = arg
        elif opt in ("-d", "--deletecleanup"):
            settings["deletecleanup"]=True
        elif opt in ("-x", "--csv"):
            settings['csvpath'] = arg
        elif opt in ("-m", "--mediadbpath"):
            settings['mediadbpath'] = arg
        elif opt in ("-b", "--dbjsonpath"):
            settings['dbjsonpath'] = arg
    return settings

class TestCounters():
    def __init__(self):
        self.tests={}
    def addtest(self,name,count=1,subkey=None):
        if subkey:
            if subkey in self.tests and name in self.tests[subkey]:
                self.tests[subkey][name] += count
            else:
                if subkey not in self.tests:
                    self.tests[subkey]={}
                self.tests[subkey][name]=count
        else:
            if name in self.tests:
                self.tests[name] += count
            else:
                self.tests[name]=count

# ----------------------------------------------------------------------------------------------------------------
# module start
#-----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    #prod_streakytest()
    settings=parseargs()
    #get the target cloud account media list saved to local cloud.json file
    prod_quick_test(settings)
    #get the local gda media.db to json snapshot
    sqllt = gda_sqllite_reader.GDA_SQLLiteReader(settings)
    #evaluate the info between the cloud.json and the mediadb.json
    md=MedialistAnalysis.MediaDataAnalysis(settings)
    if md.ok:
        print "Done"
    else:#somthing went wrong loading or evaluating the json files
        print "Failed"


