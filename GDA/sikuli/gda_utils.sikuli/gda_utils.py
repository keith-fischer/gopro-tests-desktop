import java.lang.System
import java
import sys
import traceback
import sys.argv
import os
import os.path
import urllib2
from os.path import expanduser
import shutil
import json
from time import strftime
from types import *
import subprocess
from sikuli import Sikuli
from sikuli import *
from __builtin__ import True, False
import org.sikuli.basics.SikulixForJython
import org.sikuli.script.ImagePath
import testrail

setShowActions(False)
Debug.setDebugLevel(3)
DO_HIGHLIGHT = True
MIN_SIMILIARITY=50
failcount=0 #tests failed
passcount=0 #tests passed
passtotal=0
failtotal=0
errorcount=0
failexit=3 #Stop test after number of fails
testcount = 0 #number of tests
d_gda_settings = {}
d_similarity = {}
startupcnt=0
jenkins = "C:\\Win_GDA-Studio_3a_BAT\\"
screen_seq = 0
d_screen_regions = {}

######################################
# 
# 
# 
######################################
def add_region(region_screen, region_name, REGION):
    global d_screen_regions
    print "addregion >>> %s - %s\n%s" % (region_screen,region_name,str(REGION))
    if not region_screen in d_screen_regions:
        d_screen_regions[region_screen]={} #dict of sub regions to the screen
    d_screen_regions[region_screen][region_name]=REGION
    m=d_screen_regions[region_screen][region_name]

    if m:
        m.highlight(1)
        print "addregion OK <<<<"
        return True
    
    print "addregion FAIL <<<<"
    return False
        
######################################
# 
# 
# 
######################################
def getregion(region_screen,region_name):
    global d_screen_regions
    if not region_screen in d_screen_regions:
        return None
    if region_name in d_screen_regions[region_screen]:
        return d_screen_regions[region_screen][region_name]
    return None
######################################
# 
# 
# 
######################################
def do_highlight(REGION_MATCH,seconds=1):
    global DO_HIGHLIGHT
    try:
        if REGION_MATCH and DO_HIGHLIGHT:
            REGION_MATCH.highlight(seconds)
    except:
        print "Error in do_highlight"
######################################
# 
# 
# 
######################################
def eval_argsv():
    global d_gda_settings
    d_gda_settings['runtest'] = 'default'
    d_gda_settings['version']="Quik missing ver arg"
    print str(sys.argv)
    d_gda_settings['exclusive_songs']=False
    
    for i in range(1,len(sys.argv)):
        if i==1: #required
            d_gda_settings['runtest'] = sys.argv[1]
        elif i==2: #required
            d_gda_settings['version'] = sys.argv[2]
            print "================"
            print "QUIK VERSION=%s" % d_gda_settings['version']
            print "================"
        elif i>2:
            arg=sys.argv[i].split("=")
            if arg and len(arg)==2:
                if len(arg[0])==0 or len(arg[1])==0:
                    continue
                d_gda_settings[arg[0]]=arg[1]
                #basepath=
                #testpath=
            elif arg and len(arg)==1:
                if len(arg[0])==0:
                    continue
                if arg[0]=="ex_songs":
                    d_gda_settings['exclusive_songs']=True
                    print "================"
                    print "EXCLUSIVE SONG MODE=%s" % str(d_gda_settings['exclusive_songs'])                  
                    print "================"
                else:
                    d_gda_settings[arg[0]]=True
            
######################################
# 
# 
# 
######################################
def resetglobals():
    global failcount
    failcount = 0 #tests failed
    global passcount
    passcount = 0 #tests passed
    global passtotal
    passtotal=0
    global failtotal
    failtotal = 0
    global errorcount
    errorcount = 0
    global testcount 
    testcount = 0 #number of test
    global startupcnt
    startupcnt = 0
######################################
# 
# 
# 
######################################
def setregionrelative(REGION,relx,rely,relw,relh):
    rx=REGION.getX()+relx
    ry=REGION.getY()+rely
    rw=REGION.getW()+relw
    rh=REGION.getH()+relh
    return Region(rx,ry,rw,rh)

######################################
# 
# 
# for .png failed files only
######################################
def copyfile(src,dst,prefix,post=".png"):
    name1=prefix+os.path.basename(dst).replace(".png",post)
    bname = os.path.join("FAILED",name1)
    
    _dir = os.path.dirname(dst)      
    newpath = os.path.join(_dir,bname)
    print "copyfile: "+newpath
    shutil.move(str(src),newpath) #file copy and delete src
######################################
# 
# 
# for .png failed files only
######################################
def copyfile_to_results(src,dst,prefix,post=".png"):
    global d_gda_settings
    name1=prefix+os.path.basename(dst).replace(".png",post)
    #bname = os.path.join("FAILED",name1)
    
    _dir = d_gda_settings["RESULTS"]     
    newpath = os.path.join(_dir,name1)
    print "copyfile_to_results: "+newpath
    shutil.move(str(src),newpath) #file copy and delete src
    
######################################
# 
# testregion.H must be larger than verifypngpath.H
# testregion.W must be larger than verifypngpath.W
######################################
def verifyregion(testregion,verifypngpath,similarity=0.80):
    print "verifyregion >>>>>> "
    rc=False
    m_match=None
    try:
        if not os.path.isfile(verifypngpath):
            print "Error: Invalid pngPath: %s" % verifypngpath
            print "verifyregion <<<<<<< "
            return rc, m_match
        if not testregion:
            print "Error: Invalid testregion: %s" % verifypngpath
            print "verifyregion <<<<<<< "
            return rc, m_match        
        rtest=testregion#.grow(5)
        p=Pattern(verifypngpath).similar(similarity)
        m_match=testregion.exists(p)
        #ftest=capture(rtest)
        #rc,m_match=compare_img1path_img2path(ftest,verifypngpath,similarity)
        if m_match:
            rc=True
            m_match=testregion.getLastMatch()
            print "MATCH SCORE=%f" % m_match.getScore()
        if not rc:
            print "Failed verifyregion in compare_img1path_img2path"
            ftest=capture(testregion)
            copyfile_to_results(str(ftest),verifypngpath,"FAILED_","_screenshot.png")
            
    except Exception as e:
        print "Error in verifyregion\n%s" % str(e)
    finally:
        print "verifyregion <<<<<<< "
        return rc, m_match

def cleantxt(txt):
    txt=txt.replace("/","")
    txt=txt.replace(":","")
    txt=txt.replace("\\","")
    return txt
##########################################
# ScreenShot
##########################################
def ScreenShot(imgRegion, FileName, info=""):
    global d_gda_settings
    global screen_seq
    
    print "ScreenShot>>>>>>> %s\nregion=%s\n%s" % (FileName,getRegionInfo(imgRegion),info)
    info=cleantxt(info)
    print info
    if not imgRegion:
        print "region not defined"
        print "ScreenShot<<<<<<"
        return
    if not FileName or len(FileName)==0:
        fname = "screenshot.png"
    else:
        fname = os.path.basename(FileName)
    print fname
    ext = get_extension(fname)
    if len(ext) != 0:
        fname = fname.replace(ext,"")
    else:
        ext = '.png'
    screen_seq += 1
    _info="_"
    if len(info)>0:
        _info = "_" + info + "_"
    trimfname = "srn_" + str(screen_seq) + _info + fname
    resultsPath = d_gda_settings["RESULTS"]
    newfname = trimfname+ext
    print resultsPath
    print newfname
    newpath = os.path.join(resultsPath,newfname)
    # should not happen with screen seq num
    if FileExists(newpath):
        for i in range(1,99,1): #index a new file name
            newfname = trimfname+"_"+str(i)+ext
            newpath = os.path.join(resultsPath,newfname)
            #print newpath
            if not FileExists(newpath):
                break
    print newpath    
    srnfile = capture(imgRegion) #return temp path to png file
    shutil.move(str(srnfile),newpath) #file copy and delete src
    print "ScreenShot<<<<<<"


######################################
# 
# 
# 
######################################
def getDictFromFile(jsonpath=None):
    global d_gda_settings
    print "getDictFromFile>>>>"
    _dict ={}
    fpath=jsonpath
    if not fpath:
        fpath = d_gda_settings["SIMILARITY"]

    print "getDictFromFile:"+fpath
    _json=fileread(fpath)
    if _json and len(_json)>0:       
        _dict = json.loads(_json)
        if _dict:
            print "getDictFromFile<<< ok"
            return _dict
        else:
            print "Error: Failed to set Dict"
    else:
        print "Error: Failed to set JSON"  
    print "getDictFromFile<<< failed"       
    return _dict
     
######################################
# 
# 
# 
######################################
def putDictToFile(_dict,jsonpath=None):
    global d_gda_settings
    if _dict and len(_dict)>0:
        s_dict=json.dumps(_dict)
        fpath=jsonpath
        if not fpath:
            fpath = d_gda_settings["SIMILARITY"]
        print "putDictToFile:"+fpath
        if not filewrite(fpath,s_dict,'w'):
            print "FAILED: putDictToFile similarity index file save"
            print "Automation needs to save these values for subsequent test runs for faster run times"
            exit(1)
        return True
    else:
        return False

##########################################
#
##########################################
def PATTERN(image,Pattern_Similar_Value = 0.69):
#    SmartyLib.Log("SmartyLib.PATTERN:"+str(image) )
    return Pattern(image).similar(Pattern_Similar_Value)
######################################
# 
# 
# clickoffsetfromcenterX/Y is integer
######################################
def getPattern(pngname,similarity,clickoffsetfromcenterX=None,clickoffsetfromcenterY=None):
    if not clickoffsetfromcenterX:
        return Pattern(pngname).similar(similarity)
    else:
        if clickoffsetfromcenterY:
            return Pattern(pngname).similar(similarity).targetOffset(clickoffsetfromcenterX,clickoffsetfromcenterY)
    
    print "Error in getPattern: invalid params"
    return None
######################################
# 
# 
# 
######################################
def evaltolerance(oldnum,newnum,tolerance):
    print "evaltolerance"+str(oldnum)+":"+str(newnum)
    if oldnum == newnum: return 0
    v = abs(oldnum - newnum)
    print str(tolerance)+":"+str(v)
    if v>tolerance:
        print str(v)
        return v
    else:
        return 0

######################################
# 
# 
# 
######################################
def printjson(JSON):
    try:
        return str(json.dumps(JSON))
    except:
        print "Error Invalid json: %s" % str(JSON)
        
##########################################
# orig_match is a dict
##########################################
def compare_match(new_match,orig_match, tolerance):
    print "compare_match:tolerance="+str(tolerance)
    matchreport=""
    mc=0
    if not new_match:
        return
    x=new_match.getX()
    _x=orig_match["X"]
    if evaltolerance(_x,x,tolerance)>0:
        matchreport+= "\ncompare_match:Failed X-"+str(_x)+":"+str(x)
        mc+=1
    y=new_match.getY()
    _y=orig_match["Y"]
    if evaltolerance(_y,y,tolerance)>0:
        matchreport+= "\ncompare_match:Failed Y-"+str(_y)+":"+str(y)        
        mc+=1
    w=new_match.getW()
    _w=orig_match["W"]
    if evaltolerance(_w,w,tolerance)>0:
        matchreport+= "\ncompare_match:Failed W-"+str(_w)+":"+str(w)
        mc+=1
    h=new_match.getH()
    _h=orig_match["H"]
    if evaltolerance(_h,h,tolerance)>0:
        matchreport+= "\ncompare_match:Failed H-"+str(_h)+":"+str(h)
        mc+=1

    sim = "%.2f" % new_match.getScore()
    _sim = float(_dict["similarity"])
    if evaltolerance((_sim*100),(sim*100),(tolerance+5))>0:
        matchreport+= "\ncompare_match:Failed similarity-"+str(_sim)+":"+str(sim)
        mc+=1

    if mc>0:
        #matchreport = "Match location Failed *****************************"+matchreport
        return matchreport
    return ""

######################################
# 
# 
# 
######################################
def util_read_json(jpath):
    mj = None
    with open(jpath, 'r') as f:
        mj = json.load(f)
    return mj
######################################
# 
# 
# 
######################################
def DirExists(dpath):
    return os.path.isdir(dpath)
######################################
# 
# 
# 
######################################
def FileExists(fpath):
    return os.path.exists(fpath)


####################################################
### getDatetime
####################################################
def getDatetime():
    return strftime("%Y%m%d_%H%M%S")

################################################
#
#
#
################################################
def getdatetime():
    return strftime("%Y%m%d_%H%M%S") 
######################################
# 
# 
# 
######################################
def getDate():
    return strftime("%Y%m%d")
######################################
# 
# 
# 
######################################
def getdate():
    return strftime("%m/%d/%Y")
######################################
# 
# 
# 
######################################
def getTime():
    return strftime("%H%M%S")

##########################################
#
##########################################
def gettime():
    return strftime("%H:%M:%S")

####################################################
### this is dumb use os.path.ext
####################################################
def get_extension(filename):
    #print filename
    if '.' in filename:
        ext = str(filename).split('.', 1)
        if len(ext)>0:
            return '.' + ext[1].lower()
        
    return ''

####################################################
### getRegionInfo
####################################################
def getRegionInfo(thisRegion):
    rc = ""
    if not thisRegion:
        return rc

    rc += "X=" + str(thisRegion.getX()) + ","
    rc += "Y=" + str(thisRegion.getY()) + ","
    rc += "W=" + str(thisRegion.getW()) + ","
    rc += "H=" + str(thisRegion.getH()) + ","
    rc+= "CX=" + str(thisRegion.getCenter().getX())+","
    rc+= "CY=" + str(thisRegion.getCenter().getY())+","
    
    return rc




##########################################
#
##########################################
def log(info):
    print(getdatetime()+" "+info)


##########################################
# fmode w|a
##########################################
def filewrite(fpath,txt,fmode='w'):
    f = None
    rc = False
    try:
        f=open(fpath, fmode)
        f.write(txt)
        rc=True
    except:
        print "***Failed: filewrite - "+str(fmode)+"-"+fpath
    finally:
        if f:
            f.close()
    return rc

##########################################
#
##########################################
def fileread(fpath):
    txt = None
    f = None
    try:
        f=open(fpath)
        txt=f.read()
    except:
        print "***Failed: fileread - "+fpath
    finally:
        if f:
            f.close()

    return txt

##########################################
#
##########################################
def setsettings(name,data,dtype = ""):
    global d_gda_settings
    if not data:
        print "setsettings: No data"
        
    else:
        d_gda_settings[name]=data
        if dtype == "setsettings: array":
            print name+"="
            arr = d_gda_settings[name]       
            for item in arr:
                print "-->" + str(item)
        else:
            s=""
            try:
                s=str(d_gda_settings[name])
            except:
                s=str(type(d_gda_settings[name]))
            #if (type(d_gda_settings[name]) is not types.StringType) or (type(d_gda_settings[name]) is not types.IntType):
            #    s="Other type"
            #else:
                #s=str(d_gda_settings[name])
            print "setsettings: %s=%d % (name,s)

##########################################
# main test framework config setup
# individual test modules have seperate config 
# init which build from GetEnvInfo                    
##########################################
def GetEnvInfo():
    global d_gda_settings
    eval_argsv()
    setsettings("isMac",str(Env.isMac()))
    setsettings("isWindows",str(Env.isWindows()))
    dd = getDate()
    tt = getTime()
    dt = dd+"_"+tt
    if d_gda_settings["isWindows"]=="True":
        print "GetEnvInfo>isWindows"
        setsettings("PLATFORM_KEY_CTRL",Key.CTRL)
        setsettings("JENKINS","C:\\Win_GDA-Studio_3a_BAT")
        setsettings("JOBNAME","C:\\Win_GDA-Studio_3a_BAT")
        setsettings("HOME", "C:\\Users\\" + os.getenv("USERNAME")+"\\")
        setsettings("RESULTS",d_gda_settings["JENKINS"] + "\\Results\\" +dd+"\\"+tt)
        setsettings("SIMILARITY",d_gda_settings["JENKINS"]+"\\d_similarity.json")
        setsettings("AUTOMATION",d_gda_settings["JENKINS"] + "\\Automation")
        setsettings("TEMP",d_gda_settings["JENKINS"] + "\\temp")
        setsettings("ARTIFACTS",d_gda_settings["JENKINS"] + "\\temp\\artifacts")
        
        if not os.path.exists(d_gda_settings["RESULTS"]):
            os.makedirs(d_gda_settings["RESULTS"])
        if not os.path.exists(d_gda_settings["AUTOMATION"]):
            os.makedirs(d_gda_settings["AUTOMATION"])
        if not os.path.exists(d_gda_settings["ARTIFACTS"]):
            os.makedirs(d_gda_settings["ARTIFACTS"])             
    elif d_gda_settings["isMac"]=="True":
        print "GetEnvInfo>isMac"
        setsettings("PLATFORM_KEY_CTRL",Key.CMD)
        setsettings("HOME",os.getenv("HOME")+"/")
        setsettings("JENKINS",d_gda_settings["HOME"] + "/workspace")
        setsettings("RESULTS",d_gda_settings["JENKINS"] + "/Results/" + dd + "/" + tt)
        setsettings("SIMILARITY",d_gda_settings["JENKINS"]+"/d_similarity.json")
        setsettings("JOBNAME",d_gda_settings["JENKINS"] + "/Mac_GDA-Studio_3a_BAT")
        setsettings("AUTOMATION",d_gda_settings["JENKINS"] + "/Mac_GDA-Studio_3a_BAT/Automation")
        setsettings("TEMP",d_gda_settings["JENKINS"] + "/Mac_GDA-Studio_3a_BAT/Automation/temp")
        setsettings("ARTIFACTS",d_gda_settings["TEMP"] + "/temp/artifacts")
        if not os.path.exists(d_gda_settings["RESULTS"]):
            os.makedirs(d_gda_settings["RESULTS"])
        if not os.path.exists(d_gda_settings["AUTOMATION"]):
            os.makedirs(d_gda_settings["AUTOMATION"]) 
        if not os.path.exists(d_gda_settings["ARTIFACTS"]):
            os.makedirs(d_gda_settings["ARTIFACTS"])             
    else:
        print "Error: Invalid platform, not Mac or Win"
        exit(1)
    if not os.path.isdir(d_gda_settings["HOME"]):
        print "Invalid HOME directory: Test cant continue"
        exit(1)
    setsettings("junitxml",d_gda_settings["ARTIFACTS"] + os.path.sep + "junit-results_"+dt+".xml")
    setsettings("SikuliVersion",Env.getSikuliVersion())
    setsettings("SikuliDataPath",Env.getSikuliDataPath())
    #java.lang.System.getProperty('os.name')
    setsettings("BundleFolder",getBundleFolder())
    setsettings("ParentPath",getParentPath())
    setsettings("OS",str(Settings.getOS()))
    setsettings("OSVersion",str(Settings.getOSVersion()))
    setsettings("ImagePath",getImagePath(),"array")
    temp = str(d_gda_settings["HOME"])                
    imgdir = os.path.join(temp, "gda_music_images")
    setsettings("gda_music_images",imgdir)
                    
    if d_gda_settings['runtest']=="gda_create_tests-record":
        imgdir = os.path.join(temp, ("gda_music_images-"+str(d_gda_settings['version'])))            
        setsettings("gda_music_images",imgdir)
    if not os.path.exists(d_gda_settings["gda_music_images"]):
        os.makedirs(d_gda_settings["gda_music_images"])
    imgdir = os.path.join(d_gda_settings["gda_music_images"], "FAILED")
    if not os.path.exists(imgdir):
        os.makedirs(imgdir)
    if "NO-TestRail" not in d_gda_settings:
        if not init_testrail():
            print "FAILED TO INIT TESTRAIL"
            exit(1)
        print "TESTRAIL IS READY ================================"
    else:
        print "[NO-TestRail] Reporting ================================"
    print str(d_gda_settings)
    print "<GetEnvInfo"
                    
#####################################################
# T E S T R A I L
#####################################################
def init_testrail():
    rc=False
    global d_gda_settings
                    
    d_gda_settings["isTestRail"]=False                
    print "init_testrail >>>>>>>>>>>>>"                
    run_name = d_gda_settings['version']    
    suite_name = "Quik_Music_Story_Output_Regression"
    run_description="SQA Regression Tests"
    run_mode = "run_non-passed"
    baseuri = "http://127.0.0.1:8081/testrail"
    proj_id = 86
    print "Using Testrun: %s" % run_name
    #if testrun does not exist, the TestRailClient class will create the testrun from the derived test suite
    tr = testrail.TestRailClient(run_name,suite_name,run_description,run_mode,baseuri,proj_id)
    d_gda_settings['testrail'] = None
    if tr and tr.ok==True:
        print "TestRail Tests Count=%d" % (len(tr.testcases))
        d_gda_settings['testrail'] = tr          
        
        if  d_gda_settings['testrail'] and  d_gda_settings['testrail'].ok==True:
            print "Testrail is Ready"
            rc=True
            d_gda_settings["isTestRail"]=rc
    else:
        print "Testrail NOT ready"
    print "init_testrail <<<<<<<<<<<<<<<<<<<<"
    return rc


def get_testrail_testrun_testcase_byname(testname):
    global d_gda_settings
    if not d_gda_settings["isTestRail"]:
        return
    testitem = d_gda_settings['testrail'].find_test_name(testname)
    if testitem:
        return testitem
    else:
        return None

def report_testrail_status(passfail, testid, runid, elapsed="5s",comment="sikuli automation reported status"):
    global d_gda_settings
    if not d_gda_settings["isTestRail"]:
        return                
    if "testrail" in d_gda_settings and d_gda_settings["testrail"] and d_gda_settings["testrail"].ok:
        testitem = d_gda_settings["testrail"].setteststatus(passfail, testid, runid, elapsed, comment)
    if testitem:
        return testitem
    else:
        return None

#############################################
#
# Easy testrail object eval
# return functional testrail class or None
#############################################
def get_testrail_object():
    global d_gda_settings
    if not d_gda_settings["isTestRail"]:
        return                     
    if not "testrail" in d_gda_settings:
        print "No testrail eval or reporting"
        return None
    try:
        tr=d_gda_settings["tesrail"]
        if tr and tr.ok==True:
            return tr
        return None
    except:
        print "Testrail object failed"
    return None

                                        
##########################################
# passfail 1=fail, 0=pass,-1 error, status
##########################################
def reportstatus(passfail,testinfo,gpr = None,imgName = None):
    global failcount
    global errorcount
    global passcount
    global passtotal                
    global failexit
    global failtotal
    global testcount
    
    if passfail==0:
        testcount+=1
        passcount+=1
        failtotal=0
        print "=========================================="
        print "Test Number: " +str(testcount)
        log( "PASSED: " + testinfo)
        print "=========================================="
        if gpr and imgName:
            ScreenShot(gpr,imgName,"T"+str(testcount)+"PASS")        
    elif passfail==1:
        testcount+=1
        failcount+=1
        failtotal+=1
        print "******************************************"
        print "Test Number: " +str(testcount)
        log( "FAILED: " + testinfo)
        print "******************************************"
        if gpr and imgName:
            ScreenShot(gpr,imgName,"T"+str(testcount)+"FAIL")
    elif passfail==2:
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        print "Test Number: " +str(testcount)
        log( "WARNING: " + testinfo)
        print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"    
        if gpr and imgName:
            ScreenShot(gpr,imgNamee,"T"+str(testcount)+"WARN")       
    elif passfail==-1:
        errorcount+=1
        print "###########################################"
        print "Test Number: " +str(testcount)
        log( "ERROR: " + testinfo)
        print "###########################################"
        if gpr and imgName:
            ScreenShot(gpr,imgNamee,"T"+str(testcount)+"ERROR")        
    else:
        print "------------------------------------------"
        log("STATUS: " + testinfo)
        #print "STATUS: " + testinfo
        print "------------------------------------------"
    if failtotal>=failexit: # cuts tests short when too many fails
        print "###########################################"        
        log( "Aborting Test Run: Too many subsequent fails")
        print "###########################################"
        printreport()
        exit(1)

def typerepeat(REGION,txt="",count=1):
    for i in range(1,count):
        print "typerepeat:%d" % i
        REGION.type(txt)

    
##########################################
#
##########################################
def printreport(msg = "BAT TEST",exitonfail=True):
    global d_similarity
    global failcount
    global errorcount
    global passcount
    global failexit
    global failtotal
    global testcount    
    print "=============================================="
    print "Test Report =================================="
    p=0
    f=0
    e=0
    l=0
    for png, region in d_similarity.iteritems():
        #print png
        if "failed" in region and region["failed"]>0:
            f+=1
            print "FAILED: " +png
        else:
            p+=1
        if "location" in region and region["location"]>0:
            l+=1
            print "LOCATION: " +png
            print region["location_mismatch"]         
        if "error" in region and region["error"]>1:
            e+=1
            print "WARNING: " +png
            print "msg: " +str(region["errmsg"])
        elif "error" in region and region["error"]>0:
            e+=1
            print "ERROR: " +png
            print "msg: " +str(region["errmsg"])      
        else:
            p+=1
    #passcount = testcount - failcount            
    print "Summary Report =================================="
    print "PNG Location Mismatch:"+str(l) 
    print "PNG Errors:"+str(e) 


    print "TESTS PASSED:"+str(passcount)
    print "TESTS FAILED:"+str(failcount)
    print "SCRIPT ERRORS:"+str(errorcount)
    print "----------------------------------------------"
    print "TOTAL:"+str(passcount+failcount)  

    if failcount==0:
        print "%s PASSED" % msg
    else:
        print "%s FAILED" % msg
        if exitonfail:
            exit(1)  # fail process exit so jenkins detects as failed bat
    print "=============================================="


##########################################
# FIND_Similarity
# We always want the image template similarity highest possible like 99% (0-1)
# images not found, the similarity search is reset to 100 & decremented by 5.
# newley 
##########################################
def FIND_Similarity(REGION,PATTERN,min = 50):
    print "FIND_Similarity>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    #Pattern("signout_tool.png").similar(0.90).targetOffset(14,2)
    global d_similarity
    newpattern = None
    failed = 0
    error=0
    errmsg=""
    location = 0
    cm = ""
    #print PATTERN.getFilename()
    if PATTERN.getFilename() in d_similarity:
        print "Found dict similarity "+str(d_similarity[PATTERN.getFilename()]) 
        _dict = d_similarity[PATTERN.getFilename()]
        if "similarity" in _dict:
            f = round(float(_dict["similarity"]),3)           
            print "d_similarity.similarity="+str(f)
            if f<.50 or f>.99:
                f=0.900
            newpattern = PATTERN.similar(f)
            #MATCH = REGION.find(newpattern)
            try:
                MATCH = REGION.find(newpattern)
                
                if MATCH:
                    MATCH = REGION.getLastMatch()
                    newf=round(MATCH.getScore(),3)
                    #newf="%.2f" % newf
                    
                    _dict["similarity"]=str(f)
                    
                    if newf>f: #keep highest found similarity index
                        newf=round(newf - 0.05,3)
                        _dict["similarity"]=str(newf)
                        d_similarity[PATTERN.getFilename()]=_dict

                    print "similarity:"+str(f)+">"+str(newf)+" Found from dict"
                    cm = compare_match(MATCH,_dict, 10)
                    #do_highlight(MATCH) #.highlight(1)        
                    #d_similarity[PATTERN.getFilename()]=str(f)
                    if len(cm)==0: # no mismatch
                        location+=1
                        _dict["location_mismatch"]=cm
                        _dict["failed"]=0
                        _dict["location"]=0
                        d_similarity[PATTERN.getFilename()]=_dict
                        
                        print "FIND_Similarity<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
                        
                        return MATCH
                    location=1    
                    print cm
                else:
                    print str(f)+"Match Not Found"
                    failed = 1
            except: # Exception, e:
                e = sys.exc_info()[0]
                errmsg = str(f)+" Error:" +str(e)
                error=1
                #failed re-identify the similarity index
    f = 0.90
    print "Learning new similarity threshold"

    for s in range(99, min, -5):
        f = float(s)*(.01)
        newpattern = PATTERN.similar(f)
        #do_highlight(REGION) #.highlight(1)
        ftrim = "0.90"
        try:
            print "search "+ str(f)
            MATCH = REGION.find(newpattern)
            if MATCH:
                MATCH = REGION.getLastMatch()
                print str(f)+" Found"
                #do_highlight(MATCH)#.highlight(1)
                region ={}
                newf=MATCH.getScore()
                ftrim = "%.3f" % f
                newf = round(newf - 0.05,3)
                print "similarity search:"+str(ftrim)+">"+str(newf)+" Found from dict"
                region["similarity"]=str(newf) #decreament by 5 to remove near threshold values which would force repeat of the similarity search
                #region["similarity"]=ftrim
                region["X"]=MATCH.getX()
                region["Y"]=MATCH.getY()
                region["H"]=MATCH.getH()
                region["W"]=MATCH.getW()
                failed = 0
                region["failed"]=failed #1= failed orginal similarity and had to relearn a new similarity
                region["location"]=location #1= location mismatch
                region["location_mismatch"]=cm
                error = 0
                region["error"]=error
                region["errmsg"]=""
                d_similarity[PATTERN.getFilename()]=region
                if newf < 0.4:
                    print "************************************************"
                    print "*** VERY LOW SIMILARITY INDEX ***"
                    print "*** " + str(newf)
                    print "************************************************"
                    region["error"]=error = 2
                    region["errmsg"]="VERY LOW SIMILARITY INDEX=" + str(newf)

                print "FIND_Similarity<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
                return MATCH
            else:
                print str(f)+"Match Not Found"
        except:
            failed+=1
            region={}
            e = sys.exc_info()[0]
            errmsg+= "similarity:"+str(f)+" Error:" + str(e)
            print "ERROR Match Not Found: " + errmsg
            if PATTERN.getFilename() in d_similarity:
                region = d_similarity[ PATTERN.getFilename()]
                region["error"]=error
                region["errmsg"]=errmsg
            else:
                region["X"]=0
                region["Y"]=0
                region["H"]=0                    
                region["W"]=0                    
                region["location"]=location #1= location mismatch
                region["location_mismatch"]=cm                
                region["error"]=error
                region["errmsg"]=errmsg
            d_similarity[PATTERN.getFilename()]=region
    print "FAILED No match found return None"
    print "FIND_Similarity<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"    
##########################################
#
##########################################
def refreshregion(GP):
    global d_gda_settings
    ap = d_gda_settings["app_path"]
    switchApp(ap)
    if not GP:
        print "Failed: App not found"
        return        
    GP.focus()
    r0 = GP.focusedWindow()
    if not r0:
        print "Failed: Window region not found"
        return
    else:
        do_highlight(r0)#.highlight(1)
        return r0

def startapp(path):
    os.system(path)

##########################################
# http://sikulix-2014.readthedocs.org/en/latest/appclass.html#App.App
##########################################
def waitforappstartup(apppath,appname,retry=3):
    global d_gda_settings
    print "waitforappstartup>:"+apppath+ appname
    wait(1)
    ap = App(appname)
    if not ap:
        ap.open(30)
        wait(15)
    
    if not ap or not ap.window():
        print "App not found: Sikuli starting GDA"
        
        if d_gda_settings["isMac"]=="True":
            print "looking for app:%s.app" % appname
            ap = App.open(appname+".app")
        else: #assume win
            print "looking for app:%s%s" % (apppath,appname)
            ap = App.open(apppath+appname) 
        
        wait(1)          
    for i in range(1,retry,1):
        print "wait for app startup:"+str(i)
        if ap:
            for ii in range(1,5,1):
                print "wait for app isRunning:"+str(ii)
                if ap.isRunning(): 
                    print "App Started:"
                    if ap.window():
                        print "Window found"
                        ap.focus()
                    else:
                        print "No windows found"
                    print "<waitforappstartup"
                    return ap 
                else:
                    print "App not running"
                wait(1)
        #ap = open(apppath+appname)
    print "App NOT Started:"
    print "<waitforappstartup"
    return ap


######################################
# 
# 
# 
######################################
def centerwindow():
    scn=Screen(0)
    if not scn:
        print "ERROR centerwindow: screen(0) object not created"
        exit(1)
    print str(scn)
    scnrect=scn.getBounds()
    tw=1296
    th=759
    if scnrect: print str(scnrect)
    srnx = (scnrect.width-tw)/2
    print "X="+str(srnx)
    srny = (scnrect.height-th)/2
    print "Y="+str(srny)
    return srnx,srny


# this works well for mac
######################################
# 
# 
# 
######################################
def getGDARegion(app="GoPro Quik"):
    print "getGDARegion>>>"
    ap = switchApp(app)
    if not ap:
        print "Error: APP not running"
        print "getGDARegion<<<"
        return None, None
    r = ap.focusedWindow()
    if not r:
        print "Error: No App Window"
        print "getGDARegion<<<"
        return None, ap
    do_highlight(r)#.highlight(2)
    print "getGDARegion<<<"
    return r, ap


##########################################
#
##########################################
def AppStart(appname, width=1080, height=750):
    global d_gda_settings
    print "AppStart>>>>>>>>>>>>>>"
    ext = ""
    ap = None
    apprun = appname
    r0 = None
    id = int(-1)
    
    if "isWindows" in d_gda_settings and d_gda_settings["isWindows"] == "True":
        ext=".exe"
        width=1280-100
        height=920-60     
        reportstatus(-2,"WINDOWS:"+d_gda_settings["OSVersion"])
        fname=appname+ext
        fpath="C:\\Program Files\\GoPro\\GoPro Desktop App\\"
        apprun = fpath+fname
        d_gda_settings["app_path"]=apprun
        
        print "GDASetAppWindow.exe"
        wait(5)
        #run("C:\\Automation\\gopro-tests-desktop\\GDA\\GDASetAppWindow64.bat")
        ap = waitforappstartup(fpath,fname,3)
        #wait(15)
        if not ap:
            print "App " + appname + " failed to startup"
            exit(1)
        #ap.focus()

        if ap.hasWindow()==False:
            print "Failed: App has no main window"      
            exit(1)  
        #ap.focus()

        title = ap.getWindow()
        if title != appname:
            print "Failed: Window title not found:"+appname+"<>"+title        
#            exit(1) 
        print "window title:"+title
#        ap.focus()
        #ap.focus("GoPro")
#        wait(5)
#        r0 = ap.window(0)
#        r0 = ap.window(0)
#        print str(r0.getScreen())+"Main:"+str(r0.x) + ":" + str(r0.y)+":"+str(r0.w) + ":" + str(r0.h)
        ap.focus()
        #r0=App.focusedWindow()        
        
        id=-1
        if not r0:
            cx,cy = centerwindow()
            if not cx or not cy:
                print "FAILED: Center window location X, Y values"
                exit(1)
            r0=ap.window()
            if not r0:
                for i in range(0,100):
                    ap.focus()
                    r0 = ap.window(i)
                    if not r0:
                        print "%d. No window" % i
                        break
                    do_highlight(r0)#.highlight(1)      
                    print str(i)+". srn:" + str(r0.getScreen()) + ">" + "x" + str(r0.x) + "y" + str(r0.y) + "w" + str(r0.w) + "h" + str(r0.h)
                    #Width=1288,Height=855
                    if (r0.w >= width) and (r0.w < (width+360)) and (r0.h >= height) and (r0.h < (height+150)): #and r0.x >= cx and r0.y >= cy:
                        print "found window id="+str(i)
                        id=i
                        break
                    print "--------------"
                print "============"
                if(id<0):
                    print "FAILED to find target window"
            #r0 = ap.window(id)
        else:
            do_highlight(r0)#.highlight(3)
        if not r0:
            print "Failed: Window region not found"
            exit(1)
        r0.highlight(1)
        w=1000
        if r0.w<width:
            print "Failed: Window region width not correct main window: %i < %i" % (r0.w,width)
            exit(1)
        #ap.focus()
        #switchApp(d_gda_settings["app_path"])
        #do_highlight(r0)#.highlight(3)
        
        print str(r0.getScreen())+"Main:"+str(r0.x) + ":" + str(r0.y)+":"+str(r0.w) + ":" + str(r0.h)
        setsettings("getWindow",title)
        setsettings("PID",str(ap.getPID()))
        setsettings("getName",ap.getName())
        ap.focus()
        do_highlight(r0)#.highlight(3)
        print "<openApp"
        #ap.close()
        return ap, r0        
    elif d_gda_settings["isMac"]=="True":
        ext=".app"
        reportstatus(-2,"MAC:"+d_gda_settings["OSVersion"])
        apprun = appname+ext
        d_gda_settings["app_path"]=apprun
        #ap = openApp(apprun)
        r0, ap = getGDARegion()
        if not ap:
            ap = waitforappstartup("",appname,3)
            if not ap:
                print "App " + appname + " failed to startup"
                exit(1)
            ap.focus()
            if not r0:
                r0 = ap.focusedWindow()
                if not r0:
                    print "Failed: Window region not found"
                    exit(1)
                if width>0:
                    if r0.w<(width+120): #1200
                        print "Failed: Window region width not correct main window:" + str(r0.w) + "<1200"
                        for i in range(100):
                            ap.focus()
                            rn = ap.window(i)
                            if rn:
                                do_highlight(rn)#.highlight(1) 
                                print str(rn.w) + "x"+str(rn.h)
                            else:
                                r0=rn
                                break
     
                               
            do_highlight(r0)#.highlight(3)    
            switchApp(d_gda_settings["app_path"])
            do_highlight(r0)#.highlight(3)
        print str(r0.getScreen())+"Main:"+str(r0.x) + ":" + str(r0.y)+":"+str(r0.w) + ":" + str(r0.h)
        title = ap.getWindow()

        setsettings("getWindow",title)
        setsettings("PID",str(ap.getPID()))
        setsettings("getName",ap.getName())
        print "<AppStart<<<<<<<<<<<<<"

        return ap, r0        
    else:
        print "No platform info [mac|win]"
        return

    
##########################################
#
##########################################
def getmactitle():
    print "getmactitle"
    cmd = """
    tell application "Finder"
	    activate
	
	    delay 1
        get title of front window
    end tell
    """
    txt = runScript(cmd)
    return txt


##########################################
#
##########################################
def AppStartRetry(appname, retry):
    #gp,gpr=AppStartRetry("GoPro",3)
    for x in range(1, retry):
        try:
            gp,gpr = AppStart(appname)
            if gp and gpr:
                return gp,gpr
        except:
            print str(x) + " retry: gp, gpr"
    print "FAILED to start " +appname + " *****************************"
    exit(1)
    return        

##########################################
#
##########################################
def getscreenImageLocationOffset(REGION,MATCH,PATTERN):
    patoffset = PATTERN.getTargetOffset()
    center = MATCH.getCenter()
    clickx = REGION.getX() + MATCH.getX() + center.getX() + patoffset.getX()
    clicky = REGION.getY() + MATCH.getY() + center.getY() + patoffset.getY()
    print "getscreenImageLocationOffset: X=%s, Y=%s" % (clickx,clicky)
    return Location(clickx,clicky)

##########################################
#
##########################################
def ChangePatternsimilarity(MATCH,PATTERN):
    if MATCH and PATTERN:
        newpat = PATTERN.similar(MATCH.getScore()-0.05)
        return newpat
        
##########################################
#
##########################################
def CLICK(REGION, PATTERN,sleeep=1,FAST=True,min=70):
    rc = False
    print "CLICK: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    MATCH = FIND_Similarity(REGION,PATTERN,min)

    if MATCH:
        Settings.ClickDelay=2
        Settings.DelayBeforeMouseDown=4
        
        newPATTERN = ChangePatternsimilarity(MATCH, PATTERN)
        do_highlight(MATCH)#.highlight(1)
        #matchclick =getscreenImageLocationOffset(REGION,MATCH,newPATTERN)
        #if not FAST: # mouse hover delay
        REGION.mouseMove(newPATTERN)
        _wait = sleeep+2
        wait(_wait)
        if REGION.click(newPATTERN)>0:
            wait(_wait)           
            REGION.mouseMove(Location(REGION.getX(),REGION.getY()))
            reportstatus(0,"CLICK:"+" similar:"+str(("%.2f" % MATCH.getScore()))+"-"+newPATTERN.getFilename(),REGION,newPATTERN.getFilename())
            rc = True
        else:
            REGION.mouseMove(Location(REGION.getX(),REGION.getY()))
            reportstatus(1,"CLICK:"+PATTERN.getFilename(),REGION,newPATTERN.getFilename())  
    else:
        reportstatus(1,"CLICK:"+PATTERN.getFilename(),REGION,PATTERN.getFilename())  
	
    #wait(sleeep)
    print "CLICK: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    return rc
        
##########################################
#
##########################################
def DCLICK(REGION, PATTERN,sleeep=1,min=70):
    rc = False
    print "DCLICK: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    MATCH = FIND_Similarity(REGION,PATTERN,min)

    if MATCH:
        newPATTERN = ChangePatternsimilarity(MATCH, PATTERN)
        do_highlight(MATCH)#.highlight(1)
        if REGION.doubleClick(newPATTERN)>0:
            wait(2)
            REGION.mouseMove(Location(REGION.getX(),REGION.getY()))
            reportstatus(0,"DCLICK:"+" similar:"+str(("%.2f" % MATCH.getScore()))+"-"+newPATTERN.getFilename(),REGION,newPATTERN.getFilename())
            rc = True
        else:
            REGION.mouseMove(Location(REGION.getX(),REGION.getY()))
            reportstatus(1,"DCLICK:"+PATTERN.getFilename(),REGION,newPATTERN.getFilename())  
    else:
        reportstatus(1,"DCLICK:"+PATTERN.getFilename(),REGION,PATTERN.getFilename())  
	
    wait(sleeep)
    print "DCLICK: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    return rc
##########################################
#
##########################################
def Click_Verify(REGION, PATTERN1,PATTERN2,timeout=10,sleeep=1):
    CLICK(REGION,PATTERN1)
    wait(sleeep)
    WAIT(REGION,PATTERN2,timeout)
    wait(sleeep)
    
##########################################
#
##########################################
def FIND(REGION,PATTERN,sleeep=1,min=50,NOFAIL=False):
    print "FIND: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    rc = False
    #Pattern("startupCreateAcct_title.png").similar(0.91)
    #if REGION.find(PATTERN).highlight(1):
    MATCH = FIND_Similarity(REGION,PATTERN,min)
    if MATCH:
        do_highlight(MATCH)#.highlight(1)
        if not NOFAIL:
            reportstatus(0,"FIND:"+str(("%.2f" % MATCH.getScore()))+"-"+PATTERN.getFilename(),REGION,PATTERN.getFilename())
        rc = True
    else:
        if not NOFAIL:
            reportstatus(1,"FIND:"+PATTERN.getFilename(),REGION,PATTERN.getFilename())    
    wait(sleeep)
    print "FIND: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    return rc
##########################################
#
##########################################
def WAIT(REGION,PATTERN,timeout=10,min=50,sleeep=1):
    rc = False
    print "WAIT: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    MATCH = None
    try:
        MATCH = REGION.wait(PATTERN,timeout)
    except:
        print "WAIT: not found"
    MATCH = FIND_Similarity(REGION,PATTERN,min)    
    if MATCH:
        do_highlight(MATCH)#.highlight(1)
        reportstatus(0,"WAIT:"+str(("%.2f" % MATCH.getScore()))+"-"+PATTERN.getFilename(),REGION,PATTERN.getFilename())
        rc = True
    else:
        reportstatus(1,"WAIT:"+PATTERN.getFilename(),REGION,PATTERN.getFilename())  
        
    wait(sleeep)
    print "WAIT: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    return rc
##########################################
#
##########################################
def TYPE(REGION,PATTERN,txt,sleeep=1,min=50):
    print "TYPE: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

    if txt:
        MATCH = FIND_Similarity(REGION,PATTERN,min)
        if MATCH:
            do_highlight(MATCH)#.highlight(1)
            newPATTERN = ChangePatternsimilarity(MATCH, PATTERN)
            if REGION.type(newPATTERN,txt)>0:
                reportstatus(0,"TYPE:"+txt+" similar:"+str(("%.2f" % MATCH.getScore()))+"-"+newPATTERN.getFilename(),REGION,newPATTERN.getFilename())
            else:
                reportstatus(1,"TYPE:"+txt+" similar:"+str(("%.2f" % MATCH.getScore()))+"-"+newPATTERN.getFilename(),REGION,newPATTERN.getFilename())
        else:
            reportstatus(1,"TYPE:"+txt+" -"+newPATTERN.getFilename(),REGION,PATTERN.getFilename(),"FAIL")
    else:
        reportstatus(1,"TYPE: No Text -"+newPATTERN.getFilename(),REGION,PATTERN.getFilename())
        wait(sleeep)
    print "TYPE: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
   
######################################
# 
# Experimental ocr with sikuli
# not reliable enough for text verfication
# Does not return consistant text on same image
# whether wrong text or correct. 
# Had better results doing Tessaract ocr external on commandline
######################################
def ocr(REGION,txt):
    print "==============================="
#    print REGION.text()
#    print "==============================="
    m=find(Pattern("music_txt_thenightwedanced.png").similar(0.81))
    xtx = m.text()
    uprint(xtx)
    print "==============================="
    m=find("after.png")
    m2=find("glow.png")
    
    m.highlight(1)
    xtx =  m.text()+"|"+m2.text()

    uprint(xtx)
    print "==============================="

    print "==============================="
    m=find("BRINGITEDMDe.png")
    m.highlight(1)
    xtx =  m.text()
    uprint(xtx)
    print "==============================="   

    print "==============================="
    m=find("COMETHRUHipH.png")
    m.highlight(1)
    xtx =  m.text()
    uprint(xtx)
    print "==============================="


def compare_img1path_img2path0(img1,img2,SIMILARITY=0.69):
    rc=False
    m=None
    #imagePath1 = capture()  #snapshots the screen
    image1 = exists(img1)  #Create a Match object
    if not image1:
        print "image1 none"
        return rc,m
    #imagePath2 = capture()  #snapshots the screen
    image2 = Pattern(img2).similar(SIMILARITY)  #Create a Matach Object
    myRegion = Region(image1)  #make new region from the match object
    if not myRegion:
        print "myRegion none"
        return rc,m
    m=myRegion.exists(image2)
    if m: #look in the region
        print "ok" #yeah it's in the region of the screen
        rc=True
    else:
        print "Fail"  #nope not there....    

    return rc, m
##########################################
# img1 must be >= img2 in WxH size
# img1 is verfication region to search img2
##########################################
def compare_img1path_img2path(img1,img2,SIMILARITY=0.69):
    print "compare_img1path_img2path >>>>> similarity=%f\n%s\n%s" % (SIMILARITY,img1,img2)
    rc=False
    matches=[]
    img1f = None
    bestmatch = None
    bs=-1
    try:
        img1f=Finder(img1)
        if not img1f:
            print "ERROR img1:%s" % img1
            print "compare_img1path_img2path <<<<<<"
            return rc, bestmatch
        else:
            #print "img1-Finder=%s" % str(img1f)
            p=Pattern(img2).similar(SIMILARITY)
            print "img2-Pattern=%s" % str(p)
            img1f.findAll(p)
        
            while img1f.hasNext():
                m=None
                m=img1f.next()
                if m:
                    matches.append(m)
            img1f.destroy()# is obsolete but docs ref this    
            if len(matches)==0:
                print "FAILED compare: no matches with similarity=%f" % SIMILARITY
                print "img1:%s\nimg2:%s" % (img1,img2)
                print "compare_img1path_img2path <<<<<<"
            else:
                bestmatch=matches[0]
                bs=bestmatch.getScore()
                mlen=len(matches)
                print "FindAll matches=%d" % mlen
                for i in range(0,mlen):
                    mm=matches[i]
                    ms=mm.getScore()
                    print "score=%f-%f" % (bs,ms)
                    if ms>bestmatch.getScore():
                        bestmatch=mm
                        bs=bestmatch.getScore()
                    rc = True
    except Exception as e:
            print "Error compare_img1path_img2path: %s" % str(e)
            
    finally:
        if bestmatch:
            print "bestmatch=%s" % str(bestmatch)
        print "compare_img1path_img2path <<<<<<"            
        return rc, bestmatch
    
##########################################
#
##########################################    
def CLICK3(screen,subreg,PATTERN,timeout=5,bslow=False):
    rc=False
    print "CLICK3 slow=%s >>>>>> %s" % (str(bslow),str(PATTERN))
    r=getregion(screen,subreg)
    if not r:
        print "CLICK3: region not found"
        return False
    rc = CLICK2(r,PATTERN,timeout,bslow)
    print "CLICK3 <<<<<<"    
    return rc

##########################################
#
##########################################
def CLICK2(REGION,PATTERN,timeout=5,bslow=False,retry=0):
    print "CLICK2 slow=%s >>>>>> %s" % (str(bslow),str(PATTERN))
    rc = False
    r = EXISTS2(REGION,PATTERN,timeout)
    if r:
        try:
            i=0
            if bslow==True:
                #print "CLICK2: slow pattern found"
                REGION.mouseMove(PATTERN)
                #r.mouseDown(Button.LEFT)
                wait(4)
                i=r.click()
                wait(1)
            else:
                #print "CLICK2: fast pattern found"
                i=r.click()
                
            if i==1:
                #print "CLICK2: OK"
                rc=True
            else:
                print "CLICK2: No mouse click"
                retry+=1
                if retry>3:
                    print "Failed CLICK2: retry=3"
                else:
                    rc= CLICK2(REGION,PATTERN,timeout,bslow,retry)        
                   
        except:
            print "CLICK2: mouse error"

        wait(1)
        REGION.mouseMove(Location(REGION.getX(),REGION.getY()))

    else:
        print "CLICK2: pattern not found"

    print "CLICK2 <<<<<<"
    return rc

##########################################
#
##########################################
def EXISTS3(screen,subreg,pngPATTERN,timeout=5,similarity=0.69):   
    print "EXISTS3 >>>>> %s" % str(pngPATTERN)

    r=getregion(screen,subreg)
    if not r:
        print "region not found"
        print "EXISTS3 <<<<<<"
        return None
    if isinstance(pngPATTERN,str): #assume is str png file name
        print "make pattern"
        pngPATTERN=gda_utils.PATTERN(pngPATTERN,similarity)
    if r:
        #r.highlight(1)
        print "EXISTS3 <<<<<<"
    else:
        print "EXISTS3 <<<<<<!"
    return EXISTS2(r,pngPATTERN,timeout)

##########################################
#
##########################################
def EXISTS2(REGION,PATTERN,timeout=5):
    print "EXISTS2 >>>>> %s" % str(PATTERN)
    r = REGION.exists(PATTERN,timeout)
    if r:
        m=REGION.getLastMatch()
        #print "EXISTS2:PATTERN FOUND <<<<<<"
        return m
    else:
        print "EXISTS2:PATTERN NOT FOUND !!!!!!!"
    print "EXISTS2 <<<<<<"
    return None


##########################################
#
##########################################
def testmodule():
    #p=PATTERN("dog.png",0.23)
    #s=str(isinstance(p,str))
    #print s
    #os.system("open /Applications/GDASetWinSize.app")
    #process_one = subprocess.Popen("/Applications/sikuli/StartSikuliX.sh")
    #startapp("/Applications/GDASetWinSize.app")
    #startapp("/Applications/sikuli/StartSikuliX.sh")
    #startapp("/Applications/Quik.app/Contents/MacOS/Quik")
    GetEnvInfo()
    gpa,gpr=AppStart("GoPro Quik",0,0)
    print str(gpr)
    exit(0)
    #gda_create_tests.set_CREATE_SCREEN_regions(REGION)
#    "srn_6_PASSED-SCORE=1.000000 - VERIFY MOMENTS SELECTIONS selectedmoments-Video_1-4_60sec_20cnt_song_AFTERGLOW.png"
#    "selectedmoments-Video_1-4_60sec_20cnt_song_AFTERGLOW.png"
    #Pattern("selectedmoments-Video_1-4_60sec_20cnt_song_AFTERGLOW.png").similar(SIMILARITY)
    img1="/Users/keithfisher/workspace/Results/20160825/150015/srn_7_FAILED-VERIFY MOMENTS SELECTIONS selectedmoments-Video_5-8_60sec_20cnt_song_AFTERGLOW.png_screenshot.png"
    img2="/Users/keithfisher/gda_music_images/selectedmoments-Video_1-4_60sec_20cnt_song_AFTERGLOW.png"
    SIMILARITY=0.0
    for i in range(0,10):
        SIMILARITY +=0.1
        rc, bestmatch=verifyregion(gpr,img2,SIMILARITY)
        p=Pattern(img2).similar(SIMILARITY)
        m=gpr.exists(p)
        if m:
            print "m=%f" % m.getScore()
            m.highlight(1)
            
        if rc:
            print "rc true"
            if bestmatch:
                                
                print str(bestmatch)
                d=bestmatch.getScore()        
                print "Found score=%f" % d

            else:
                print "Match not found"
        else:
            print "rc false"

#testmodule()