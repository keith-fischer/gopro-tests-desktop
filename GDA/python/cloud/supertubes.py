#!/usr/bin/env python

import argparse
import ConfigParser
from functools import wraps
import hashlib
import json
import os
import requests
import signal
import socket
import ssl
import sys
import threading
import time
import uuid

from CodernityDB.database import Database
from CodernityDB.tree_index import TreeBasedIndex
from Crypto.PublicKey import RSA
from OpenSSL import crypto
from flask import Flask, request, send_from_directory, Response
import paho.mqtt.client as paho
from zeroconf import ServiceInfo, ServiceBrowser, Zeroconf
import ZODB, ZODB.FileStorage, BTrees.OOBTree
import persistent

version = '1.0'
verbose = 1

ip = socket.gethostbyname(socket.gethostname())

def prnt(level, msg):
    if verbose >= level:
        print msg

#
# trap ctrl-c
#

def signal_handler(sig, frame):
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        mdns_remove()
    #sys.exit(0)
    os.kill(os.getpid(), signal.SIGQUIT)
signal.signal(signal.SIGINT, signal_handler)

#
# config file
#

class Config:
    def __init__(self):
        self.config_filename = 'supertubes.cfg'
        self.config = ConfigParser.RawConfigParser()
        self.config.read(self.config_filename)
    def get_check(self, section, key, default):
        if not self.config.has_section(section):
            self.config.add_section(section)
        if not self.config.has_option(section, key):
            if default:
                self.config.set(section, key, default)
            return False
        return True

    def get(self, section, key, default):
        return self.config.get(section, key) if self.get_check(section, key, default) else default

    def get_boolean(self, section, key, default):
        return self.config.getboolean(section, key) if self.get_check(section, key, default) else default

    def get_int(self, section, key, default):
        return self.config.getint(section, key) if self.get_check(section, key, default) else default

    def set(self, section, key, value):
        if value:
            self.config.set(section, key, value)
            self.config.write(open(self.config_filename, 'w'))

config = Config()
abs_media_dir            = os.path.abspath(config.get('global', 'media_dir', './media'))
debug                    = config.get_boolean('global', 'debug', 'false')
http_port                = config.get_int('http', 'port', 5000)
iot_ca_cert_filename     = config.get('iot', 'ca_cert_filename', 'root_ca_cert.pem')
iot_client_cert_filename = config.get('iot', 'client_cert_filename', 'client_cert.pem')
iot_server               = config.get('iot', 'server', None)
iot_port                 = config.get_int('iot', 'port', 8883)
ssl_csr_filename         = config.get('ssl', 'csr_filename', 'csr.pem')
ssl_private_key_filename = config.get('ssl', 'private_key_filename', 'privkey.pem')
cloud_server             = config.get('cloud', 'server', 'https://api.staging.gopro.com')
cloud_user_id            = config.get('cloud', 'user_id', None)
device_id                = config.get('device', 'id', None)
device_token             = config.get('device', 'token', None)

#
# database
#

db = None

def db_init():
    global db
    if not os.path.exists('db'):
        os.mkdir('db')

    storage = ZODB.FileStorage.FileStorage('db/supertubes.db')
    db = ZODB.DB(storage)

    with db.transaction() as conn:
        if not hasattr(conn.root, 'media'):
            prnt(1, 'adding media collection')
            conn.root.media = BTrees.OOBTree.BTree()
        if not hasattr(conn.root, 'drives'):
            prnt(1, 'adding drives collection')
            conn.root.drives = BTrees.OOBTree.BTree()
        if not hasattr(conn.root, 'state'):
            prnt(1, 'adding state collection')
            conn.root.state = BTrees.OOBTree.BTree()
        if not hasattr(conn.root, 'settings'):
            prnt(1, 'adding settings collection')
            conn.root.settings = BTrees.OOBTree.BTree()
    print 'initialized database', db

class DatabaseEntry(persistent.Persistent):
    def __init__(self, doc=None):
        self.doc = {}
        if doc != None:
            self.doc = doc
            self._p_changed = True
    def set_doc(self, d):
        self.doc = d.copy()
        self._p_changed = True
    def get_doc(self):
        return self.doc

def reset_db_media():
    with db.transaction() as conn:
        conn.root.media = BTrees.OOBTree.BTree()
def reset_db_drive():
    with db.transaction() as conn:
        conn.root.drives = BTrees.OOBTree.BTree()
        conn.root.drives['internal'] = DatabaseEntry('{\"type\": \"drive\", \"id\": \"123456789012345678901234567890\", \"capacity_mb\": 1000000, \"usage_mb\": 12345, \"name\": \"SUPERTUBES\", \"state\": \"ok\", \"number_of_drive_errors\": 4, \"number_of_files_on_drive\", 1234}')
def reset_db_state():
    with db.transaction() as conn:
        conn.root.state = BTrees.OOBTree.BTree()
        conn.root.state['firmware_version'] = DatabaseEntry('ST01.01.00.00')
        conn.root.state['device_state'] = DatabaseEntry('ok')
        conn.root.state['online'] = DatabaseEntry(True)
        conn.root.state['offloading'] = DatabaseEntry(0)
        conn.root.state['streaming'] = DatabaseEntry(False)
        conn.root.state['transcoding'] = DatabaseEntry(0)
        conn.root.state['storage_capacity_mb'] = DatabaseEntry(1000000)
        conn.root.state['storage_used_mb'] = DatabaseEntry('12345')
        conn.root.state['storage_used_files'] = DatabaseEntry(1000)
def reset_db_settings():
    with db.transaction() as conn:
        conn.root.settings = BTrees.OOBTree.BTree()
        conn.root.settings['device_name'] = DatabaseEntry('My Supertubes')
        conn.root.settings['hls_streaming_enabled'] = DatabaseEntry(True)
        conn.root.settings['dlna_streaming_enabled'] = DatabaseEntry(False)
        conn.root.settings['chromecast_streaming_enabled'] = DatabaseEntry(False)
        conn.root.settings['smb_enabled'] = DatabaseEntry(False)
        conn.root.settings['delete_media_after_import'] = DatabaseEntry(True)
def reset_db():
    reset_db_media()
    reset_db_drive()
    reset_db_state()
    reset_db_settings()

# db test

if 0:
    with db.transaction() as conn:
        if conn.root.media.has_key('gumi-1'):
            print 'has medium!'
        else:
            print 'inserting medium'
            m = DatabaseEntry()
            m.set_doc({'width': 4000, 'height': 3000})
            conn.root.media['gumi-1'] = m
            conn.root.media['gumi-2'] = m

    with db.transaction() as conn:
        m = conn.root.media['gumi-1']
        print m.doc

    with db.transaction() as conn:
        conn.root.media['gumi-2'] = DatabaseEntry()

    print 'all items:'
    with db.transaction() as conn:
        for (k,v) in conn.root.media.iteritems():
            print ' ', k, v.doc

    with db.transaction() as conn:
        del conn.root.media['gumi-2']

    print 'all items:'
    with db.transaction() as conn:
        for (k,v) in conn.root.media.iteritems():
            print ' ', k, v.doc

    sys.exit(0)

#
# web service
#

class SecuredStaticFlask(Flask):
    def get_send_file_max_age(self, name):
        return 600
    def send_static_file(self, filename):
        # Get user from session
        #if ext.login.current_user.is_authenticated():
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        print 'user is authorized'
        return super(SecuredStaticFlask, self).send_static_file(filename)
        #else:
        #    abort(403)

def check_auth(username, password):
    """This function is called to check if a username / password combination is valid."""
    valid = False

    if username == 'developer' and password == 'radmagix':
        valid = True
    return valid


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

#app = Flask(__name__)
app = SecuredStaticFlask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Supertubes Simulator v1.0</h1>
    <h2>mDNS API</h2>
    <p>When this simulator starts, it will perform an mDNS announcement supporting the _gopro-media._tcp.local service.
    When the simulator is stopped (by CRTL-C) the mDNS service will be unregistered.

    <h2>HTTP API</h2>
    The following HTTP API is supported:
    <ul>
    <li> <b>GET /capabilities</b> returns device capabilities as a JSON document (.. under construction)</li>
    <li> <b>GET /settings</b> returns device settings as a JSON document.</li>
    <li> <b>GET /status</b> returns device state info as a JSON document.</li>
    <li> <b>GET /setup</b> returns info required for device setup (mainly the oauth client id) and info about
         whether the device has already been setup (but not info about who has set it up).</li>
    <li> <b>GET /media</b> (aliased as <b>/gp/gpMediaList</b>) returns media info (in gpMediaList V3 formatted JSON)
         <p> Will return info about ALL media on the device by default. However, several query parameters are supported:
         <ul>
         <li> <b>page=X</b> and <b>per_page=Y</b> pagination (X and Y are integers, obviously)</li>
         <li> <b>type=X</b> filter by media type (valid values are video, photo, burst, timelapse, continuous, loop</li>
         <li> <b>filesystem=X</b> filter by media stored on the specified drive id (drive ids are found in the /status endpoint)</li>
         </ul></p>
    </li>
    <li> <b>GET /media/:id[format]</b> returns media
         <p> <b>:id</b> is the media id (gumi) that is returned in the call to /media. <b>format</b> is one of
         <ul>
         <li> <b>.jpg</b> valid for photos and videos (returns a thumbnail for a video medium). There is an additional query parameter
              available for photo mediums: <b>version=X</b> which returns different resolutions. Valid values for this query
              parameter are "thumbnail" and "screennail". If no version query parameter is given, the full image is returned.</li>
         <li> <b>.mp4</b> valid for videos and long timelapses. Returns a progressive MP4 file.</li>
         <li> <b>.m3u8</b> valid for videos and long timelapses. Returns an HLS master playlist. Query parameters supported for
              this format include:
              <ul>
                 <li> <b>resolution=X</b> only these resolutions are supported: 4k, 1080p, 720p, 480p</li>
                 <li> <b>frame_drop=X</b> only stream every Xth frame (useful when source is 120fps or 240fps for example).</li>
              </ul>
              </li>
         </ul>
         <p>Both .jpg and .mp4 formats support a query parameter <b>index=X</b> which allows indexing the Xth file in a multi-file
         medium (bursts, timelapses, chaptered video, looped video, etc.). This continues the lie that a medium can be represented
         by a single gumi (frown) but that's the information architecture we have at this point</p>

    </li>
    <li> <b>PUT /setup</b> initial device setup (or re-setup). Request body is a JSON document with all information necessary
         to do initial product setup (auth code mainly). Response body is a JSON object with the response to the setup process.
         This call allows re-setup only if the new user is the same as the existing user. If the user is different then this
         call will fail with a 401 status code.</li>
    <li> <b>PUT /settings</b> updates all device settings. Request body is a JSON document containing settings key/value pairs.</li>
    <li> <b>PATCH /settings</b> updates one or more device settings. Request body is a JSON document containing settings key/value pairs.</li>
    <li> <b>DELETE /setup</b> Unregisters the device (disassociates the device from a user so another user can setup the
         device.</li>
    <li> <b>DELETE /media/:id</b> deletes a medium by id (gumi). If the medium is a multi-file medium all files associated with
         that medium are deleted.<</li>
    </ul>

    <h2>HTTP Development API</h2>
    These APIs are not part of the final product - they just exist to help development and prototyping.
    <ul>
    <li> <b>GET /</b> (this help page)</li>
    <li> <b>POST /media</b> adds new media to this simulated device. This accepts a request body of metadata in gpMediaList V3 format.
         Media must already exist in the referenced location on the hard drive (this API does not upload media, just registers it
         so the GET APIs do something reasonable). The body can be a single gpMediaList V3 object or can be an array of such objects.
         If an array, this will do a batch registration (efficient way to seed the simulator with a bunch of media).</li>
    <li> <b>PUT /state</b> change the supertubes state. Request body is a JSON document with key/value pairs representing the state
         that should change.</li>
    <li> <b>GET /state</b> Get the current state of the system.
    </ul>

    <h2>MQTT API</h2>
    This device subscribes to three MQTT topics:
    <ul>
    <li> <b>device/:id/#</b> device-specific topics</li>
    <li> <b>user/:id/#</b> user-specific topics</li>
    <li> <b>$aws/things/:id/#</b> device shadow topics</li>
    </ul>
    '''

@app.route('/capabilities')
@requires_auth
def capabilities():
    caps = {'version': '1.0.0', 'capabilities': []}
    return json.dumps(caps)

@app.route('/state', methods=['GET', 'PUT'])
@requires_auth
def state():
    if request.method == 'GET':
        state_info = {'version': '1.0', 'state':{}}
        with db.transaction() as conn:
            for (k,v) in conn.root.state.iteritems():
                state_info['state'][k] = v.doc
        return json.dumps(state_info)
    else:
        for k,v in request.json:
            with db.transaction() as conn:
                conn.root.state[k] = v

@app.route('/settings', methods=['GET', 'PUT'])
@requires_auth
def settings():
    if request.method == 'GET':
        settings_info = {'version': '1.0', 'settings':{}}
        with db.transaction() as conn:
            for (k,v) in conn.root.settings.iteritems():
                settings_info['settings'][k] = v.doc
        return json.dumps(settings_info)
    else:
        for k,v in request.json:
            with db.transaction() as conn:
                conn.root.settings[k] = v

@app.route('/setup', methods=['GET', 'PUT', 'DELETE'])
@requires_auth
def setup():
    setup = {'version': '1.0.0', 'setup': 'yes'}
    if request.method == 'DELETE':
        return 'delete setup'
    if request.method == 'PUT':
        return 'setup'
    return json.dumps(setup)

@app.route('/drives')
@requires_auth
def drive_info():
    drive_info = {'drives':[]}
    print 'db =', db
    if db == None:
        return 'ouch'

    with db.transaction() as conn:
        for (k,v) in conn.root.drives.iteritems():
            drive_info['drives'].append(v.doc)
    return json.dumps(drive_info)

@app.route('/gp/gpMediaList')
@requires_auth
def media_list():
    return media()

@app.route('/media')
@requires_auth
def media():
    media_info = {'version': '1.0.0', 'media': []}
    filtr = None
    if request.args.has_key('type'):
        arg = request.args.get('type')
        if arg == 'photo':
            filtr = 'photo'
        if arg == 'video':
            filtr = 'video'
    with db.transaction() as conn:
        for (k,v) in conn.root.media.iteritems():
            media_info['media'].append(v.doc)
    return json.dumps(media_info)

def media_from_drive(d):
    return 'media from ' + d

def media_from_all_drives():
    return 'media from all drives'

@app.route('/media/<gumi>/<fmt>', methods=['GET'])
@requires_auth
def download_file(gumi, fmt):
    prnt(2, 'download_file(%s,%s)' % (gumi, fmt))
    try:
        with db.transaction() as conn:
            if not conn.root.media.has_key(gumi):
                prnt(2, 'no gumi found')
                return '', 404
            f = fmt.lower()
            if conn.root.media[gumi].doc.has_key(f):
                filename = conn.root.media[gumi].doc[f]
                prnt(2, 'returning %s' % filename)
                #return send_from_directory(os.path.join(abs_media_dir, drive_id), filename)
                dirname, fname = os.path.split(filename)
                return send_from_directory(dirname, fname)
    except Exception as e:
        print 'exception: ', e
    return 'no file found', 404

@app.route('/media/<gumi>', methods=['GET', 'PUT', 'DELETE'])
@requires_auth
def medium(gumi):
    if '.' in gumi:
        print 'splitting'
        t = gumi.split('.')
        return download_file(t[0], t[1])
    if request.method == 'DELETE':
        with db.transaction() as conn:
            if conn.root.media.has_key(gumi):
                del conn.root.media[gumi]
                return
        return '', 404
    elif request.method == 'PUT':
        pass
    elif request.method == 'GET':
        with db.transaction() as conn:
            if conn.root.media.has_key(gumi):
                return json.dumps(conn.root.media[gumi].doc)
        return '', 404
#
# cron (run juuust after web service and mDNS start up)
#

t = None
cron_started = False

def start_cron():
    global t, cron_started
    if not t and not cron_started:
        cron_started = True
        t = threading.Timer(2, cron)
        t.daemon = True
        t.start()
    else:
        prnt(1, 'cron already started!')

def cron():
    global t
    prnt(2, 'cron()')
    # delayed startup stuff goes here
    prnt(2, 'end cron()')

#
# mDNS
#

mdns_service = None
zconf = None

def mdns_announce():
    global mdns_service
    t = socket.gethostname().split('.')
    server = t[0] + '-st.' + t[1]
    service_type = '_gopro-media._tcp.local.'
    service_name = t[0] + '-st._gopro-media._tcp.local.'
    service_server = server
    service_port = http_port
    service_properties = {'description': 'a description', 'ip_addr': ip}
    #service_address = socket.gethostname().replace('-', '')
    #service_address = int(socket.inet_aton(ip).encode('hex'),16)
    service_address = socket.inet_aton(ip).encode('hex')[-4:]
    service_weight = 0
    service_priority = 0

    prnt(2, 'service info:')
    prnt(2, '  type:       %s' % service_type)
    prnt(2, '  name:       %s' % service_name)
    prnt(2, '  address:    %s' % service_address)
    prnt(2, '  properties: %s' % service_properties)
    prnt(2, '  server:     %s' % service_server)
    prnt(2, '  port:       %s' % service_port)
    prnt(2, '  weight:     %s' % service_weight)
    prnt(2, '  priority:   %s' % service_priority)

    mdns_service = ServiceInfo(service_type,
                      service_name,
                      server     = service_server,
                      port       = service_port,
                      properties = service_properties,
                      address    = service_address,
                      weight     = service_weight,
                      priority   = service_priority)

    zconf.register_service(mdns_service)
    prnt(1, 'mdns registered')

def mdns_remove():
    global mdns_service
    if (mdns_service):
        zconf.unregister_service(mdns_service)
    mdns_service = None
    prnt(1, 'mdns unregistered')

#
# device management (device id, security keys)
#

def ssl_init():
    prnt(2, 'ssl_init()')
    key = crypto.PKey()
    key.generate_key(crypto.TYPE_RSA, 2048)

    req = crypto.X509Req()
    req.get_subject().CN = 'USA'
    req.get_subject().countryName = 'US'
    req.get_subject().stateOrProvinceName = 'CA'
    req.get_subject().localityName = 'Calsbad'
    req.get_subject().organizationName = 'GoPro'
    req.get_subject().organizationalUnitName = 'SWS'

    # Add in extensions
    x509_extensions = ([
        crypto.X509Extension("keyUsage", False, "Digital Signature, Non Repudiation, Key Encipherment"),
        crypto.X509Extension("basicConstraints", False, "CA:FALSE"),
    ])

    # If there are SAN entries, append the base_constraints to include them.
    #if ss:
    #    san_constraint = crypto.X509Extension("subjectAltName", False, ss)
    #    x509_extensions.append(san_constraint)

    req.add_extensions(x509_extensions)

    req.set_pubkey(key)
    req.sign(key, 'sha256')

    with open(ssl_private_key_filename, 'w') as fp:
        fp.write(crypto.dump_privatekey(crypto.FILETYPE_PEM, key))
    os.chmod(ssl_private_key_filename, 0600)

    with open(ssl_csr_filename, 'w') as fp:
        fp.write(crypto.dump_certificate_request(crypto.FILETYPE_PEM, req))

def provision():
    global device_token, iot_server
    prnt(2, 'provision()')
    if not device_id:
        prnt(0, 'cannot provision; no device id')
        sys.exit(1)
    sat_string = 'aB3Uo982bt@*eauer.jmx=?EE!7)uGGI' + "-" + device_id
    hash = hashlib.sha256(sat_string)
    sat = hash.hexdigest().upper()

    csr = open(ssl_csr_filename).read()
    request_body = {'authentication': {'sat': sat}, 'iot_csr': csr}
    #print json.dumps(request_body)
    headers = {'Content-Type': 'application/json; version=1.1.0'}
    resp = requests.post(cloud_server + '/devices/' + device_id, headers=headers, data=json.dumps(request_body))
    #print resp.text
    r = json.loads(resp.text)
    prnt(2, 'provision status code = %s' % resp.status_code)
    if resp.status_code != 201:
        prnt(0, 'error making provision call')
        prnt(0, resp.text)
    device_token = r['device_access_token']
    config.set('device', 'token', device_token)
    with open(iot_client_cert_filename, 'w') as fp:
        fp.write(r['iot_certificate_pem'])
    iot_server = r['mqtt_url']
    config.set('iot', 'server', iot_server)
    with open(iot_ca_cert_filename, 'w') as fp:
        fp.write(r['root_certificate'])

    prnt(1,'device_id    = %s' % device_id)
    prnt(1,'device_token = %s' % device_token)
    prnt(1,'iot_server   = %s' % iot_server)

#
# MQTT
#

connflag = False

def pretty(s):
    if isinstance(s, basestring):
        return json.dumps(json.loads(s), indent=4, sort_keys=True)
    return json.dumps(s, indent=4, sort_keys=True)

def process_command(msg):
    #print pretty(str(msg.payload))
    sys.stderr.write('formatting drive ')
    for i in range(10):
        sys.stderr.write('.')
        time.sleep(0.5)
    sys.stderr.write(' drive formatted\n')

    sstate = {}
    sstate['state'] = {}
    sstate['state']['reported'] = {'drives': [{'type': 'disk', 'size': 1000, 'uuid': '123-456-78', 'use': 'storage'}]}

    #mqttc.publish('$aws/things/C31613EVT23844-peripherals/shadow/update', json.dumps(sstate), qos=1)

def on_disconnect(client, userdata, rc):
    prnt(0, 'on_disconnect(%d)' % rc)

def on_connect(client, userdata, flags, rc):
    global connflag
    prnt(2, 'on_connect(%s, %d)' % (flags, rc))
    connflag = True
    if (device_id):
        if 0: # cannot connect to shadow topics due to DEV-455
            topic = '$aws/things/%s/shadow/#' % device_id
            client.subscribe(topic, 1)
            prnt(1, 'subscribed to topic %s' % topic)
        if cloud_user_id:
            topic = 'user/%s/shadow/#' % cloud_user_id
            client.subscribe(topic, 1)
            prnt(1, 'subscribed to topic %s' % topic)
        topic = 'device/%s/command/#' % device_id
        client.subscribe(topic, 1)
        prnt(1, 'subscribed to topic %s' % topic)

def on_message(client, userdata, msg):
    prnt(1, 'on_message:')
    prnt(1, '  ' + msg.topic)
    prnt(1, '  ' + str(msg.payload))
    if 'command' in msg.topic:
        process_command(msg)

def mqtt_init():
    prnt(2, 'mqtt_init()')

    if not os.path.exists(ssl_csr_filename) or not os.path.exists(ssl_private_key_filename):
        ssl_init()

    if not os.path.exists(iot_client_cert_filename) or not os.path.exists(iot_ca_cert_filename) or not iot_server or not device_token:
        provision()

    mqttc = paho.Client()
    mqttc.on_connect = on_connect
    mqttc.on_disconnect = on_disconnect
    mqttc.on_message = on_message
    #mqttc.on_log = on_log
    mqttc.tls_set(iot_ca_cert_filename, certfile=iot_client_cert_filename, keyfile=ssl_private_key_filename, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
    r = mqttc.connect(iot_server, iot_port, keepalive=60)
    mqttc.loop_start()

    prnt(1, "mqtt connected")

    #raw_input('press enter to plug in a new hard drive:')
    #sstate = {}
    #sstate['state'] = {}
    #sstate['state']['reported'] = {'drives': [{'type': 'disk', 'size': 1000, 'uuid': '123-456-78', 'use': 'new'}]}
    #mqttc.publish('$aws/things/C31613EVT23844-peripherals/shadow/update', json.dumps(sstate), qos=1)
    #print 'published new shadow state - waiting for response on how to use the drive'

#
# main
#

help_text = '''
 +------------------------------------------------------------------------+
 |                  Supertubes network simulator  %s                      |
 +------------------------------------------------------------------------+
 |                                                                        |
 | This simulator implements the mDNS and HTTP interfaces that Supertubes |
 | will support, allowing the system design to be validated through a     |
 | working prototype.                                                     |
 |                                                                        |
 | For an overview of these APIs, run this tool then use your browser to  |
 | visit the root page of this web server: http://localhost:%d/         |
 |                                                                        |
 | Type Ctrl-C to quit the simulator.                                     |
 |                                                                        |
 | When started, the simulator will by default annouce presence over      |
 | mDNS, connect to the AWS IoT MQTT broker, and start up an HTTP web     |
 | service. But the simulator can be started with other command line      |
 | options to do other things:                                            |
 | - reset_db                         reset all database tables           |
 | - reset_db_media                   reset media database table          |
 | - reset_db_drive                   reset drive database table          |
 | - reset_db_state                   reset state database table          |
 | - reset_db_settings                reset settings database table       |
 | - import_media <file> [<file> ..]  import media from JSON files        |
 | - import_drives <file> [<file> ..] import drive info from JSON files   |
 | - media_template file              create a media import JSON tempalte |
 | - drive_template file              create a media import JSON tempalte |
 |                                                                        |
 | Typical usage, then, looks something like this:                        |
 | 1. import some media                                                   |
 |   ./supertubes.py import_media m1.json m2.json                         |
 | 2. import some drive info                                              |
 |   ./supertubes.py import_drives d1.json d2.json                        |
 | 3. Start the supertubes simulator                                      |
 |   ./supertubes.py                                                      |
 |                                                                        |
 | Working files created by the simulator:                                |
 | - supertubes.cfg - configuration file for the simulator                |
 |   Contains things like device id, IoT settings, web service port, etc. |
 | - db - a directory containing the simulator's database that holds      |
 |   media and drive info                                                 |
 | - *.pem, *.crt SSL certificates used to securely connect to the MQTT   |
 |   message broker                                                       |
 +------------------------------------------------------------------------+
 |                                                                        |
 | Requirements to use:                                                   |
 | - Python 2.7 (NOT 3.0, Jeff)                                           |
 | - Flask python module (pip install flask)                              |
 | - zeroconf python module (pip install zeroconf)                        |
 | - Codernity db python module (pip install CodernityDB)                 |
 | - PAHO MQTT client python module (pip install paho-mqtt)               |
 | - PyCrypto python module (pip install pycrypto)                        |
 |                                                                        |
 +------------------------------------------------------------------------+

''' % (version, http_port)

def initialize():
    global db, device_id, zconf
    if os.environ.get("WERKZEUG_RUN_MAIN") or not debug: # only true if debug is true
        prnt(1, help_text)
        if not device_id:
            device_id = 'G' + uuid.uuid4().hex.upper() # software device id
            config.set('device', 'id', device_id)

        db_init()
        zconf = Zeroconf([ip])

        mdns_announce()
        mqtt_init()
        start_cron()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='supertubes', epilog=help_text, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.set_defaults(action = None, verbose=1, os='', version=False, color=True)
    parser.add_argument('-v', '--verbose', dest='verbose', type=int, help='verbosity')
    parser.add_argument('-q', '--quiet', dest='verbose', action='store_const', const=0, help='quiet')
    parser.add_argument('-V', '--version', dest='version', action='store_const', const=True, help='print version')
    parser.add_argument('--color=no', dest='color', action='store_const', const=False, help='do not colorize output')
    parser.add_argument('action', nargs='?', help='action (optional, see below)')
    parser.add_argument('args', nargs=argparse.REMAINDER)
    args = parser.parse_args()
    verbose = args.verbose

    if args.version:
        print version
        sys.exit(0)
    if args.action == 'import_media':
        print 'importing media'
        if len(args.args) == 0:
            print 'error - no json file provided'
            sys.exit(1)
        for filename in args.args:
            with open(filename) as fp:
                try:
                    data = json.load(fp)
                except:
                    print 'unable to load json file', filename
                    sys.exit(1)
                if not data:
                    print 'could not parse json file', filename
                    sys.exit(1)
                if isinstance(data, list):
                    for m in data:
                        if not m.has_key('gumi'):
                            print 'medium is misisng gumi attribute'
                            print pretty(m)
                            sys.exit(1)
                        gumi = m['gumi']
                        with db.transaction() as conn:
                            conn.root.media[gumi] = DatabaseEntry(m)
                        print 'imported', gumi
                else:
                    if not data.has_key('gumi'):
                        print 'medium is misisng gumi attribute'
                        print pretty(data)
                        sys.exit(1)
                    gumi = data['gumi']
                    with db.transaction() as conn:
                        conn.root.media[gumi] = DatabaseEntry(data)
                        print 'imported', gumi
    elif args.action == 'reset_db_media':
        reset_db_media()
    elif args.action == 'reset_db_drive':
        reset_db_drive()
    elif args.action == 'reset_db_state':
        reset_db_state()
    elif args.action == 'reset_db_settings':
        reset_db_settings()
    elif args.action == 'reset_db':
        reset_db()
    else: # normal operation
        initialize()
        app.run(host='0.0.0.0', port=http_port, debug=debug)

