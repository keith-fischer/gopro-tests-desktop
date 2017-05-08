import os
import sys
import traceback
import platform
from os.path import expanduser
import json
import org.sikuli.script.ImagePath
import shutil
from time import strftime
from types import *

from sikuli import Sikuli
from sikuli import *
from __builtin__ import True, False
import org.sikuli.basics.SikulixForJython

import gda_utils
import gda_music_tests
import gda_create_tests
   
################################################
# compare baseline /test image set folders
# creates a report of songs and the story moments pass/fail/missing 
# of the image files
# gda.sikuli calls this module gda_img_regression.compare_image_sets
# 
################################################

################################################
# entry point for image compare
# 
#
################################################
def compare_image_sets(basepath,testpath):
    rc=False
    report=[]
    faillist=[]
    failstatus=[]
    failstatus={"IMAGE_COMPARE":0,"IMAGE_FILE_NAME":0,"IMAGE_FILE_MISSING":0,"MISSING_BASELINE_IMAGES":0,"MISSING_TEST_IMAGES":0}
    msongs=gda_img_init()
    filekeys=['selectedmoments-Video_1-4_15sec_', 
            'selectedmoments-Video_1-4_30sec_',
            'selectedmoments-Video_1-4_60sec_',
            'selectedmoments-Video_13-16_15sec_',
            'selectedmoments-Video_13-16_30sec_',
            'selectedmoments-Video_13-16_60sec_',
            'selectedmoments-Video_5-8_15sec_',
            'selectedmoments-Video_5-8_30sec_',
            'selectedmoments-Video_5-8_60sec_',
            'selectedmoments-Video_9-12_15sec_',
            'selectedmoments-Video_9-12_30sec_',
            'selectedmoments-Video_9-12_60sec_',
            '_viewbeats_15.png',
            '_viewbeats_30.png',
            '_viewbeats_60.png',
            '_viewmoments_15.png',
            '_viewmoments_30.png',
            '_viewmoments_60.png']
    testscount=0        
    for i in range(0,msongs.getGDAsongcount()):
        
        title, png, t15, t30, t60 = msongs.getsortednextsong()
        rcbasepath,d_pngbasepaths=gda_create_tests.getregressionfilelists(png,basepath)
        rctestpath,d_pngtestpaths=gda_create_tests.getregressionfilelists(png,testpath)
        report.append("=================================")
        
        s= "%s | %s t15:%d t30:%d t60:%d" % (title,png,t15,t30,t60)
        print "==========================================="
        print s
        t=""
        report.append(s)
        if rcbasepath and rctestpath:
            #print "BASEPATH: %s" % (str(d_pngbasepaths))
            #print "TESTPATH: %s" % (str(d_pngtestpaths))
            for item in filekeys:
                testscount+=1

                bname=None
                bpath=None
                tname=None
                tpath=None
                if item in d_pngbasepaths:
                    bpath=d_pngbasepaths[item]
                if item in d_pngtestpaths:
                    tpath=d_pngtestpaths[item]
                if bpath:    
                    bname=os.path.basename(bpath)
                if tpath:
                    tname=os.path.basename(tpath)
                if tname and bname:
                    if tname==bname:
                        similarity=0.97                    
                        r,sr = compare(bpath,tpath,similarity)
                        if r:
                            t="PASSED: %s - %s - %s" % (str("%04.2f" % similarity),sr,tname)
                            report.append(t)
                        else:
                            t="FAILED: IMAGE_COMPARE: similarity=%s - %s" % (str("%04.2f" % similarity),bname)
                            report.append("!!!!!!!!!!!!!!!!!!!!!!")
                            report.append(t)
                            report.append("!!!!!!!!!!!!!!!!!!!!!!")
                            faillist.append(t)                         
                            
                    else:
                        t="FAILED: IMAGE_FILE_NAME: %s - %s <> %s" % (item,bname,tname)
                        report.append("!!!!!!!!!!!!!!!!!!!!!!")
                        report.append(t)
                        report.append("!!!!!!!!!!!!!!!!!!!!!!")
                        faillist.append(t)                        
                else:
                    t="FAILED: IMAGE_FILE_MISSING: %s - %s <> %s" % (item,bname,tname)

                    report.append("!!!!!!!!!!!!!!!!!!!!!!")
                    report.append(t)
                    report.append("!!!!!!!!!!!!!!!!!!!!!!")
                    faillist.append(t)
            
                    
        else:
            t=""
            testscount+=1
            report.append("!!!!!!!!!!!!!!!!!!!!!!")
            if not rcbasepath:
                t="FAILED: MISSING_BASELINE_IMAGES: %s" % s
                faillist.append(t)
                report.append(t)

            if not rctestpath:
                t="FAILED: MISSING_TEST_IMAGES: %s" % s
                faillist.append(t)
                report.append(t)

            report.append("!!!!!!!!!!!!!!!!!!!!!!")

            
    if len(faillist)>0:
        report.append("!!!!!!!!!!!!!!!!!!!!!!")
        s="Failed %d of %d" % (len(faillist),testscount)
        report.append(s)
        c=0
        report.append("-----------------------------------")
        for item in faillist:
            c+=1
            s="%i. %s" % (c,item)
            report.append(s)
        report.append("!!!!!!!!!!!!!!!!!!!!!!")
            
    else:
        rc=True
     
    for item in report:
        print item
        failstatus=summaryreport(item,failstatus)

    print str(failstatus)
    print "SUMMARY REPORT =================="
    for key,data in failstatus.iteritems():
        print "%s=%d" % (key,data)
    return rc

def summaryreport(row,d_counts):
    for key,data in d_counts.iteritems():
        if key in row:
            data = data+1
            d_counts[key] = data
    return d_counts

def compare(base,test,similarity):
    rc=False
    bestmatch=None
    rc,bestmatch = gda_utils.compare_img1path_img2path(base,test,similarity)
    d=0
    if rc and bestmatch:
        simi=bestmatch.getScore()
        d=str("%04.2f" % simi)    
    return rc,d
######################################
# 
# 
# 
######################################
def gda_img_init():
    print "gda_img_init >>>>>> " 
    msongs=None    
    msongs=gda_music_tests.GDA_music()
    if not msongs or not msongs.isready:
        print "FAILED gda_img_init: msongs.isready"
        print "gda_img_init <<<<<<<"
        return None

    if msongs.getGDAsongcount()<199:
        print "FAILED invalid number of songs=%i of 199" % msongs.getGDAsongcount()
        print "gda_img_init <<<<<<<"
        exit(-2)
        
        d_report["songs"]=msongs.songreport()
        
    gda_music_tests.testmusic_init(msongs)

    print "gda_img_init <<<<<<<"
        
    return msongs

