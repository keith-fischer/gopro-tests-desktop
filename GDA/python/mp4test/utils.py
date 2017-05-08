
import sys
import subprocessmgr
import os
from time import sleep
import datetime
import logging
import csv
import json
import platform
from os.path import expanduser

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
class Utils:
    def __init__(self):
        self.evalplatform()

    ################################
    # evalplatform
    #
    #
    ################################
    def evalplatform(self):
        self.platform_system = platform.system()  # Darwin = Mac
        self.platform_release = platform.release()
        self.home = expanduser("~")
        if self.platform_system == "Windows":
            self.music_root = "\\AppData\\Local\\GoPro\\Music"
            self.automation_root = "%s\\workspace\\" % self.home
            # self.automation_root = "/Automation/gopro-tests-desktop/GDA/Music_Tests"
            self.isWin = True
        elif self.platform_system == "Darwin":
            self.music_root = "/Library/Application Support/com.GoPro.goproapp.GoProMusicService/Music"
            # self.automation_root = "%s/workspace/" % self.home
            self.automation_root = "/Automation/gopro-tests-desktop/GDA/Music_Tests/"
            self.isMac = True

    ################################
    # json_load
    # validates file exists
    # return json dict or None
    ################################
    def json_load(self, jpath):
        if not os.path.isfile(jpath):
            logging.INFO("Failed to load json, invalid path:%s" % jpath)
            return None
        try:
            with open(jpath, 'r') as f:
                mj = json.load(f)
                return mj
        except Exception, e:
            logging.ERROR("json_load: Exception")
            logging.ERROR(str(e))
        return None

    ################################
    # json_save
    # validates file output
    # return True or False success
    ################################
    def json_save(self,jpath,jdata):
        rc=False
        # Writing JSON data
        try:
            with open(jpath, 'w') as f:
                json.dump(jdata, f, indent=4)
                f.close()
            if not os.path.isfile(jpath):
                logging.INFO("Failed to write json:%s" % jpath)
            else:
                rc=True
        except Exception, e:
            logging.ERROR("json_save: Exception")
            logging.ERROR(str(e))
        return rc

    ################################
    # addtracks hack to insert the mp3 json data tracks
    # fixed in sikuli gda_music_tests.songreport()
    # record now included the tracks
    ################################
    def addtracks(self):
        srcpath = "/Automation/gopro-tests-desktop/GDA/Music_Tests/GDA_musiclist.json"
        dstpath = "/Users/keithfisher/Downloads/gda_music_images-Mac4946-162316/gda_create_tests_record.json"
        srcjson = self.json_load(srcpath)
        dstjson = self.json_load(dstpath)
        for i in range(0,len(dstjson['songs'])):
            dstitem = dstjson['songs'][i]
            png = dstitem['png']
            found = False
            for ii in range(0,len(srcjson['musiclist'])):
                srcitem = srcjson['musiclist'][ii]
                if srcitem['pngsong_name'] == png:
                    dstitem['tracks'] = srcitem['tracks']
                    dstitem['vibes'] = srcitem['vibes']
                    dstitem['version'] = srcitem['version']
                    dstitem['bpm'] = srcitem['beats_per_minute']
                    dstitem['genre'] = srcitem['genre']
                    dstitem['music_title'] = srcitem['music_title']
                    dstjson['songs'][i]=dstitem
                    print "Update: %s" % png
                    found=True
                    break
            if not found:
                print "NOT FOUND: %s" % png


        self.json_save(dstpath,dstjson)
        print "DONE"

def testutils():
    ut=Utils()
    ut.addtracks()

#testutils()