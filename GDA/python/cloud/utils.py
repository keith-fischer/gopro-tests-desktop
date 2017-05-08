
import sys
#import subprocessmgr
import os
from time import sleep
import datetime
import logging
import csv
import json
import platform
import collections
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
            logging.info("Failed to load json, invalid path:%s" % jpath)
            return None
        try:
            with open(jpath, 'r') as f:
                mj = json.load(f)
                return mj
        except Exception, e:
            logging.error("json_load: Exception")
            logging.error(str(e))
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
                logging.info("Failed to write json:%s" % jpath)
            else:
                rc=True
        except Exception, e:
            logging.error("json_save: Exception")
            logging.error(str(e))
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

    def merge_two_dicts(self,d1, d2):
        '''Given two dicts, merge them into a new dict as a shallow copy.'''
        d3 = d1.copy()
        d3.update(d2)
        return d3
    def flatendictlist(self,prefixname,dictlist):
        flatdict={}
        keylist=[]
        for i in range(0,len(dictlist)):
            for key1, value1 in dictlist[i].iteritems():
                fld="%s-%d-%s" % (prefixname,i,key1)
                flatdict[fld]=value1
                keylist.append(fld)
        return flatdict

    def evalmediaitem(self,mediaitem):
        dates=['client_updated_at','updated_at','captured_at','upload_completed_at','created_at']
        blacklist=['gopro_user_id','token']
        sublists=['derivativeList']

        newitem={}
        subitems = {}
        sublist = []

        for key1, value1 in mediaitem.iteritems():
            if key1 in blacklist:
                continue
            if type(value1) is list:
                if key1 in sublists:
                    subitems={}
                    for item in mediaitem[key1]:
                        sublist.append(self.evalmediaitem(item))
                    mediaitem[key1]=None
                    if len(sublist)>0:
                        subitems = self.flatendictlist("Derived",sublist)
                        continue
            elif key1 in dates:
                if value1:
                    value1 = value1.replace("T"," ").replace("Z","")
                else:
                    value1=""
            else:
                if not value1:
                    value1=""
            newitem[key1]=value1
        newitem1=self.merge_two_dicts(newitem,subitems)

        return newitem1


    def dict_to_csv(self,jsonpath,csvpath):
        mdict=self.json_load(jsonpath)
        count=0
        keylen=0
        maxfldid=0
        for i in range(0,len(mdict['medialist'])):
            klen=len(mdict['medialist'][i].keys())
            if klen>keylen:
                keylen=klen
                maxfldid=i
            newitem = self.evalmediaitem(mdict['medialist'][i])
            if newitem:
                newitem2 = newitem #collections.OrderedDict(sorted(newitem.items()))
                mdict['medialist'][i]=newitem2
                count += 1
                print "%d %s" % (count, newitem2['filename'])
        count=0
        print csvpath
        with open(csvpath, 'wb') as f:  # Just use 'w' mode in 3.x  with open(csvpath, 'wb') as f:
            w = csv.DictWriter(f, mdict['medialist'][maxfldid].keys())
            w.writeheader()
            eitem=None
            for item in mdict['medialist']:
                try:
                    w.writerow(item)
                    eitem=item
                    msg=""
                except Exception, e:
                    msg="\n=========\n%s\n%s\n-----------\n%s" % (str(e),str(item),str(eitem))
                count += 1
                print "%d %s %s" % (count,item['filename'],msg)



    def makecsv(self,jsonobj,blacklist,nodelist,outpath):

        headers=[]
        subheaders=[]
        fldname=""
        c1=0
        for node in nodelist:
            if node in jsonobj:
                itemlist=jsonobj[node]
                for item in itemlist:
                    for key1, value1 in item.iteritems():
                        if key1 in blacklist:
                            continue
                        fld1=key1.replace(" ","_")
                        if type(value1) is list:
                            c2=0
                            for subitem in value1:
                                c2+=1
                                for key2, value2 in subitem.iteritems():
                                    if key2 in blacklist:
                                        continue
                                    fld2=key2.replace(" ","_")
                                    fldname="%s-%d-%s" & (fld1,c2,fld2)
                                    if fldname not in subheaders:
                                        subheaders.append(fldname)





def testutils():
    ut=Utils()
    #ut.addtracks()
    ut.dict_to_csv("/Users/keithfisher/Downloads/autogda00_prod.json","/Users/keithfisher/Downloads/autogda00_prod.csv")
    exit(0)
#testutils()