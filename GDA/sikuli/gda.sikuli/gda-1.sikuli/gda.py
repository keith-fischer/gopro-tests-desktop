
import java.lang.System
import java
import sys
import os
import shutil
#import math
#import ast
import json
from time import strftime
from sikuli import Sikuli
from sikuli import *
from __builtin__ import True, False
import org.sikuli.basics.SikulixForJython
import org.sikuli.script.ImagePath
#import results
setShowActions(True)
Debug.setDebugLevel(3)
#autogda00@gmail.com
#access4auto=gmail.com
#autogda00 = gopro account
#import HelperLib
#from guide import *
failcount=0
failexit=3
testcount = 0
d_gda_settings={}
d_similarity={}
startupcnt=0
jenkins = "C:\\Win_GDA-Studio_3a_BAT\\"
screen_seq = 0

def DirExists(dpath):
    return os.path.isdir(dpath)
def FileExists(fpath):
    return os.path.exists(fpath)

####################################################
### getDatetime
####################################################
def getDatetime():
    return strftime("%Y%m%d_%H%M%S") 
def getDate():
    return strftime("%Y%m%d")
def getTime():
    return strftime("%H%M%S")

def set_results_folder():
    global d_gda_settings
   


####################################################
### get_extension
####################################################
def get_extension(filename):
    #print filename
    if '.' in filename:
        ext = str(filename).split('.', 1)
        if len(ext)>0:
            return '.' + ext[1].lower()
        
    return ''
##########################################
#ScreenShot
##########################################
def ScreenShot(imgRegion, FileName, info=""):
    global d_gda_settings
    global screen_seq
    print "Screenshot>>>>>>>"
    if not imgRegion:
        print "region not defined"
        print "Screenshot<<<<<<"
        return
    if not FileName or len(FileName)==0:
        fname = "screenshot.png"
    else:
        fname = os.path.basename(FileName)
    print getRegionInfo(imgRegion)
    #d = d_gda_settings["path_del"]
    ext = get_extension(fname)
    if len(ext) != 0:
        print ext
        fname = fname.replace(ext,"")
        print fname
    else:
        ext = '.png'
    screen_seq += 1
    _info="_"
    if len(info)>0:
        _info = "_" + info + "_"
    trimfname = "srn_" + str(screen_seq) + _info + fname
    resultsPath = d_gda_settings["RESULTS"]
    newfname = trimfname+ext
    newpath = os.path.join(resultsPath,newfname)
    print newpath
    #print os.path.join(ResultsPath,newfname)
    if FileExists(newpath):
        for i in range(1,99,1): #index a new file name
            newfname = trimfname+str(i)+ext
            newpath = os.path.join(resultsPath,newfname)
            print newpath
            if not FileExists(newpath):
                break
        
    print newpath
    #imgRegion.highlight(2)
    srnfile = capture(imgRegion) #return temp path to png file
    #wait(1)
    #Log("ScreenShot:path - " + fullpath)
    shutil.move(str(srnfile),newpath) #file copy and delete src
    #Log("ScreenShot:Moved - " + FileName)
    print "Screenshot<<<<<<"
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
def getdatetime():
    return strftime("%Y%m%d_%H%M%S")
##########################################
#
##########################################
def gettime():
    return strftime("%H:%M:%S")
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

def getDictFromFile():
    global d_gda_settings
    print "getDictFromFile>>>>"
    _dict ={}
    
    fpath = d_gda_settings["SIMILARITY"]
#    if d_gda_settings["isWindows"]:
#        fpath = d_gda_settings["HOME"]+"\\workspace\\d_similarity.json"
#        print "win d_similarity="+fpath
#    else:
#        print "mac d_similarity="+fpath
    print fpath
    _json=fileread(fpath)
    if _json and len(_json)>0:       
        _dict = json.loads(_json)
        if _dict:
            return _dict
        else:
            print "Error: Failed to set Dict"
    else:
        print "Error: Failed to set JSON"  
    print "getDictFromFile<<<"       
    return _dict
     
def putDictToFile(_dict):
    global d_gda_settings
    if _dict and len(_dict)>0:
        s_dict=json.dumps(_dict)
        fpath = d_gda_settings["SIMILARITY"]
        print "putDictToFile:d_similarity="+fpath
        if not filewrite(fpath,s_dict,'w'):
            print "FAILED: putDictToFile similarity index file save"
            print "Automation needs to save these values for subsequent test runs for faster run times"
            exit(1)
        return True
    else:
        return False

    
##########################################
# passfail 1=fail, 0=pass,-1 error, status
##########################################
def reportstatus(passfail,testinfo,gpr = None,imgName = None):
    global failcount
    global failexit
    global testcount
    if passfail==0:
        testcount+=1
        print "=========================================="
        print "Test Number: " +str(testcount)
        log( "PASSED: " + testinfo)
        print "=========================================="
        failcount = 0
        if gpr and imgName:
            ScreenShot(gpr,imgName,"T"+str(testcount)+"PASS")        
    elif passfail==1:
        testcount+=1
        print "******************************************"
        print "Test Number: " +str(testcount)
        log( "FAILED: " + testinfo)
        print "******************************************"
        failcount += 1
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
        print "###########################################"
        print "Test Number: " +str(testcount)
        log( "ERROR: " + testinfo)
        print "###########################################"
        failcount += 1
        if gpr and imgName:
            ScreenShot(gpr,imgNamee,"T"+str(testcount)+"ERROR")        
    else:
        print "------------------------------------------"
        log("STATUS: " + testinfo)
        #print "STATUS: " + testinfo
        print "------------------------------------------"
    if failcount>failexit: # cuts BAT tests short when too many fails
        print "###########################################"        
        log( "Aborting Test Run: Too many subsequent fails")
        print "###########################################"
        printreport()
        exit(1)
    
##########################################
#
##########################################
def printreport():
    global d_similarity
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
        if "error" in region and region["error"]>0:
            e+=1
            print "ERROR: " +png
            print "msg: " +str(region["errmsg"])            
        else:
            p+=1
    passcount = testcount - failcount            
    print "Summary Report =================================="
    print "PNG Mismatches:"+str(l) 
    print "PASSED:"+str(passcount)
    print "FAILED:"+str(failcount)
    print "----------------------------------------------"
    print "TOTAL:"+str(passcount+failcount)  

    if failcount==0:
        print "BAT TEST PASSED"
    else:
        print "BAT TEST FAILED"
        exit(1)  # fail process exit so jenkins detects as failed bat
    print "=============================================="
##########################################
#
##########################################
def PATTERN(image):
#    SmartyLib.Log("SmartyLib.PATTERN:"+str(image) )
    return Pattern(image).similar(Pattern_Similar_Value)

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
            f = float(_dict["similarity"])
            print str(f)
            newpattern = PATTERN.similar(f)
            #MATCH = REGION.find(newpattern)
            try:
                MATCH = REGION.find(newpattern)            
                if MATCH:
                    newf=MATCH.getScore()
                    newf="%.2f" % newf
                    if newf>f: #keep highest found similarity index
                        d_similarity[PATTERN.getFilename()]=_dict
                    print "similarity:"+str(f)+">"+str(newf)+" Found from dict"
                    _dict["similarity"]=str(newf) 
                    cm = compare_match(MATCH,_dict, 10)
                    #MATCH.highlight(1)        
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
                errmsg = str(f)+" Error Not Found in Dict" +str(e)
                error=1
                #failed re-identify the similarity index
    f = 0.90
    print "Learning new similarity threshold"

    for s in range(99, 50, -5):
        f = float(s)*(.01)
        newpattern = PATTERN.similar(f)
        #REGION.highlight(1)
        ftrim = "0.90"
        try:
            print "search "+ str(f)
            MATCH = REGION.find(newpattern)
            if MATCH:
                print str(f)+" Found"
                #MATCH.highlight(1)
                region ={}
                newf=MATCH.getScore()
                ftrim = "%.2f" % f
                print "similarity:"+str(ftrim)+">"+str(newf)+" Found from dict"
                region["similarity"]=str(newf-5) #decreament by 5 to remove near threshold values which would force repeat of the similarity search
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
                region["errmsg"]=errmsg
                d_similarity[PATTERN.getFilename()]=region  
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
        r0.highlight(1)
        return r0
    
##########################################
#
##########################################
def setsettings(name,data,dtype = ""):
    if not data:
        print " No data"
        
    else:
        d_gda_settings[name]=data
        if dtype=="array":
            print name+"="
            arr = d_gda_settings[name]       
            for item in arr:
                print "-->"+str(item)
        else:
            print name + "=" + d_gda_settings[name]

##########################################
# Need to add args for build number info
##########################################
def GetEnvInfo():
    global d_gda_settings
    setsettings("isMac",str(Env.isMac()))
    setsettings("isWindows",str(Env.isWindows()))
    dd = getDate()
    tt = getTime()
    dt = dd+"_"+tt
    if d_gda_settings["isWindows"]=="True":
        print "GetEnvInfo>isWindows"
        setsettings("JENKINS","C:\\Win_GDA-Studio_3a_BAT")
        setsettings("JOBNAME","C:\\Win_GDA-Studio_3a_BAT")
        setsettings("HOME", "C:\\Users\\" + os.getenv("USERNAME"))
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
        setsettings("HOME",os.getenv("HOME"))
        setsettings("RESULTS",d_gda_settings["HOME"] + "/workspace/Results/" + dd + "/" + tt)
        setsettings("JENKINS",d_gda_settings["HOME"] + "/workspace")
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
    print "<GetEnvInfo"

    
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
# http://sikulix-2014.readthedocs.org/en/latest/appclass.html#App.App
##########################################
def waitforappstartup(apppath,appname,retry=3):
    print "waitforappstartup>:"+apppath+ appname
    wait(1)
    ap = App(appname)
    #ap.open(30)
    wait(15)
    
    if not ap or not ap.window():
        print "App not found: Sikuli starting GDA"
        if d_gda_settings["isMac"]=="True":
            App.open(appname+".app")
        else: #assume win
            App.open(apppath+appname) 
        
        wait(5)          
    for i in range(1,retry,1):
        print "wait for appstartup:"+str(i)
        if ap:
            for ii in range(1,10,1):
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
    return


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
##########################################
#
##########################################
def AppStart(appname):
    global d_gda_settings
    print "openApp>"
    ext=""
    ap=None
    apprun=appname   

    if d_gda_settings["isWindows"]=="True":
        ext=".exe"
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
            exit(1) 
        print "window title:"+title
#        ap.focus()
        #ap.focus("GoPro")
#        wait(5)
#        r0 = ap.window(0)
#        r0 = ap.window(0)
#        print str(r0.getScreen())+"Main:"+str(r0.x) + ":" + str(r0.y)+":"+str(r0.w) + ":" + str(r0.h)
        ap.focus()
        r0=App.focusedWindow()        
        
        id=-1
        if not r0:
            cx,cy = centerwindow()
            if not cx or not cy:
                print "FAILED: Center window location X, Y values"
                exit(1)
            for i in range(100):
                ap.focus()
                r0 = ap.window(i)
                if not r0: break
                r0.highlight(1)      
                print str(i)+". " + str(r0.getScreen()) + ">" + str(i) + ":" + str(r0.x) + ":" + str(r0.y) + ":" + str(r0.w) + ":" + str(r0.h)
                if r0.w >= 1290 and r0.w < 1440 and r0.h >= 750 and r0.h < 767: #and r0.x >= cx and r0.y >= cy:
                    print "found window id="+str(i)
    
                    if id>=0:
                        print "old id=" + str(id)
                    id=i
                    break
            print "============"
    #        for i in range(100):
    #            r0 = ap.window(i)
    #            if not r0: break
    #            print str(r0.getScreen())+">"+str(i)+":"+str(r0.x) + ":" + str(r0.y)+":"+str(r0.w) + ":" + str(r0.h)
    #            r0.highlight(1) 
                #wait(1)
            
    #            r0.highlight(2)
    #            if r0.w==1296: break
            if(id<0):
                print "FAILED to find target window"
            r0 = ap.window(id)
        
        if not r0:
            print "Failed: Window region not found"
            exit(1)
        if r0.w<1200:
            print "Failed: Window region width not correct main window:" + str(r0.w) + "<900"
            exit(1)
        ap.focus()
        switchApp(d_gda_settings["app_path"])
        r0.highlight(3)
        
        print str(r0.getScreen())+"Main:"+str(r0.x) + ":" + str(r0.y)+":"+str(r0.w) + ":" + str(r0.h)
        setsettings("getWindow",title)
        setsettings("PID",str(ap.getPID()))
        setsettings("getName",ap.getName())
        ap.focus()
        r0.highlight(3)
        print "<openApp"
        #ap.close()
        return ap, r0        
    elif d_gda_settings["isMac"]=="True":
        ext=".app"
        reportstatus(-2,"MAC:"+d_gda_settings["OSVersion"])
        apprun = appname+ext
        d_gda_settings["app_path"]=apprun
        #ap = openApp(apprun)
        ap = waitforappstartup("",appname,3)
        if not ap:
            print "App " + appname + " failed to startup"
            exit(1)
        ap.focus()
        r0 = ap.focusedWindow()
        if not r0:
            print "Failed: Window region not found"
            exit(1)
        
        if r0.w<1200: #1200
            print "Failed: Window region width not correct main window:" + str(r0.w) + "<1200"
            for i in range(100):
                ap.focus()
                rn = ap.window(i)
                if rn:
                    rn.highlight(1) 
                    print str(rn.w) + "x"+str(rn.h)
                else:
                    r0=rn
                    break
 
            exit(1)
        r0.highlight(3)    
        switchApp(d_gda_settings["app_path"])
        r0.highlight(3)
        print str(r0.getScreen())+"Main:"+str(r0.x) + ":" + str(r0.y)+":"+str(r0.w) + ":" + str(r0.h)
        title = ap.getWindow()

        setsettings("getWindow",title)
        setsettings("PID",str(ap.getPID()))
        setsettings("getName",ap.getName())
        print "<openApp"

        return ap, r0        
    else:
        print "No platform info [mac|win]"
        return



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
def Test_Welcome(r0):
    #wait("GoProDesktopApp_GPLogo.png").find("Welcome_GDA_Title.png")
    r1 = r0.find("Welcome_getstarted.png")
    r1.find("GoproLogo.png")

    r1.find("Welcome GDA.png")
    r1.find("Welcome_Manage.png")
    r1.find("Welcome_Edit.png")
    r1.find("Welcome_Share.png")

    r2 = r1.find(Pattern("Welcome_AutoLaunch.png").similar(0.80))
    # enable
    r2.find(Pattern("Welcome_UnChecked_AutoLaunch.png").similar(0.90)).click("Welcome_Unchecked_btn.png")

    # disable
    r2.find(Pattern("Welcome_UnChecked_AutoLaunch.png").similar(0.90)).click("Welcome_Checked_btn.png")

    r1.click("Welcome_GetStarted_btn.png")

        
##########################################
#
##########################################
def ChangePatternsimilarity(MATCH,PATTERN):
    if MATCH and PATTERN:
        newpat = PATTERN.similar(MATCH.getScore())
        return newpat
        
##########################################
#
##########################################
def CLICK(REGION, PATTERN,sleeep=1):
    print "CLICK: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    MATCH = FIND_Similarity(REGION,PATTERN,40)

    if MATCH:
        newPATTERN = ChangePatternsimilarity(MATCH, PATTERN)
        MATCH.highlight(1)
        if REGION.click(newPATTERN)>0:
            reportstatus(0,"CLICK:"+" similar:"+str(("%.2f" % MATCH.getScore()))+"-"+newPATTERN.getFilename(),REGION,newPATTERN.getFilename())
        else:
            reportstatus(1,"CLICK:"+PATTERN.getFilename(),REGION,newPATTERN.getFilename())  
    else:
        reportstatus(1,"CLICK:"+PATTERN.getFilename(),REGION,PATTERN.getFilename())  
	
    wait(sleeep)
    print "CLICK: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
    
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
def FIND(REGION,PATTERN,sleeep=1):
    print "WAIT: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    
    #Pattern("startupCreateAcct_title.png").similar(0.91)
    #if REGION.find(PATTERN).highlight(1):
    MATCH = FIND_Similarity(REGION,PATTERN,40)
    if MATCH:
        MATCH.highlight(1)
        reportstatus(0,"FIND:"+str(("%.2f" % MATCH.getScore()))+"-"+PATTERN.getFilename(),REGION,PATTERN.getFilename())
    else:
        reportstatus(1,"FIND:"+PATTERN.getFilename(),REGION,PATTERN.getFilename())    
    wait(sleeep)
    print "FIND: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"

##########################################
#
##########################################
def WAIT(REGION,PATTERN,timeout=10,sleeep=1):
    print "WAIT: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    MATCH = None
    try:
        MATCH = REGION.wait(PATTERN,timeout)
    except:
        print "WAIT: not found"
    MATCH = FIND_Similarity(REGION,PATTERN,40)    
    if MATCH:
        MATCH.highlight(1)
        reportstatus(0,"WAIT:"+str(("%.2f" % MATCH.getScore()))+"-"+PATTERN.getFilename(),REGION,PATTERN.getFilename())
    else:
        reportstatus(1,"WAIT:"+PATTERN.getFilename(),REGION,PATTERN.getFilename())  
        
    wait(sleeep)
    print "WAIT: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
##########################################
#
##########################################
def TYPE(REGION,PATTERN,txt,sleeep=1):
    print "TYPE: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

    if txt:
        MATCH = FIND_Similarity(REGION,PATTERN,40)
        if MATCH:
            MATCH.highlight(1)
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
    print "WAIT: <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<"
   
##########################################
#
##########################################
def signout(region):

    try:     
        CLICK(region,Pattern("signout_tool.png").similar(0.90).targetOffset(14,2))
        CLICK(region,Pattern("signout_signout.png").similar(0.90).targetOffset(-24,-8))
    except:
        print "Sign Out not found"
        


##########################################
#
##########################################
def create_your_acct(REGION,willfail=True,fname="john",lname="doe",email="jdoe@jdoe.zzz",pw="1234567890"):
    WAIT(REGION,Pattern("createacct_txt_title.png").exact()) #createacct_txt_title.png
    
    FIND(REGION,Pattern("createacct_txt_subtitle.png").similar(0.90)) #createacct_txt_subtitle.png

    TYPE(REGION,Pattern("createacct_txtbox_email.png").exact().targetOffset(-232,23),fname) #createacct_txtbox_email.png
    TYPE(REGION,Pattern("createacct_txtbox_email.png").exact().targetOffset(51,26),lname) #createacct_txtbox_email.png
    TYPE(REGION,Pattern("createacct_txtbox_email.png").exact().targetOffset(-245,-32),email) #createacct_txtbox_email.png
    TYPE(REGION,Pattern("createacct_txtbox_password.png").exact().targetOffset(-216,-29),pw) #createacct_txtbox_password.png
    TYPE(REGION,Pattern("createacct_txtbox_password.png").exact().targetOffset(-247,28),pw) #createacct_txtbox_password.png
    CLICK(REGION,Pattern("createacct_unchecked_getnews.png").similar(0.96).targetOffset(-147,2)) #createacct_unchecked_getnews.png
    FIND(REGION,Pattern("createacct_checked_getnews.png").similar(0.91).targetOffset(-145,2)) #createacct_checked_getnews.png
    #CLICK(REGION,Pattern("createacct_unchecked_getnews.png").similar(0.96).targetOffset(-147,2)) #createacct_unchecked_getnews.png
    CLICK(REGION,Pattern("createacct_unchecked_iacknowledge.png").similar(0.98).targetOffset(-275,-7)) #createacct_unchecked_iacknowledge.png
    FIND(REGION,Pattern("createacct_checked_iacknowledge.png").similar(0.91).targetOffset(-277,-12)) #createacct_checked_iacknowledge.png
    #CLICK(REGION,Pattern("createacct_unchecked_iacknowledge.png").similar(0.98).targetOffset(-275,-7)) #createacct_unchecked_iacknowledge.png
    CLICK(REGION, Pattern("createacct_btn_getacct.png").similar(0.98)) #createacct_btn_getacct.png
    wait(15) # wait for message
    #invalid acct info
    if willfail==True:
        WAIT(REGION,Pattern("createacct_txt_invalidemail.png").exact(),30)
    
        CLICK(REGION,Pattern("createacct_btn_signin.png").similar(0.91)) #createacct_btn_signin.png
    else:
        CLICK(REGION,Pattern("createacct_btn_signin.png").similar(0.91)) #createacct_btn_signin.png
        
     

##########################################
#
##########################################
def signin_test(REGION,willfail=True,email="dog@breath.mut",pw="hatecats"):
    #FIND_Similarity(REGION,PATTERN,min = 50):
    WAIT(REGION,Pattern("signin_txt_title.png").similar(0.90),30)

    FIND(REGION,Pattern("signin_img_logo.png").similar(0.90))

    TYPE(REGION,Pattern("signin_txtbox_emailpw.png").similar(0.90).targetOffset(-185,-38),email)
    TYPE(REGION,Pattern("signin_txtbox_emailpw.png").similar(0.90).targetOffset(-211,22),pw)


    FIND(REGION,Pattern("signin_btn_forgot.png").similar(0.90))
  

    FIND(REGION,Pattern("signin_btn_resendemail.png").similar(0.90))

    CLICK(REGION,Pattern("signin_btn_signin.png").similar(0.90))
    #test invalid acct
    if willfail==True:

        WAIT(REGION,Pattern("signin_txt_invalidemail.png").similar(0.92),30) #signin_txt_invalidemail.png

        FIND(REGION,Pattern("signin_txtbox_emailpw_blankpw.png").similar(0.91))
        cleanfld=Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE
        TYPE(REGION,Pattern("signin_txtbox_emailpw.png").similar(0.90).targetOffset(210,-38),cleanfld)
        
        #CLICK(REGION,Pattern("signin_btn_needacct.png").similar(0.90).targetOffset(67,9))
        #WAIT(REGION,Pattern("createacct_txt_title.png").similar(0.90)) #createacct_txt_title.png
        #CLICK(REGION,Pattern("createacct_btn_signin.png").similar(0.91)) #createacct_btn_signin.png

        #WAIT(REGION,Pattern("signin_txt_title.png").similar(0.90),30)
        
        
    #else: #is valid acct
        #CLICK(REGION,Pattern("signin_btn_needacct.png").similar(0.90).targetOffset(67,9))
##########################################
#
##########################################
def signin_validate(region):
    try:
        WAIT(region,Pattern("signin_logo.png").similar(0.90),10)
    except:
        print "sign in not found"
        signout(region)

    WAIT(region,Pattern("signin_logo.png").similar(0.90),30)
    
    FIND(region,Pattern("signin_form.png").similar(0.90))
    
    FIND(region,Pattern("signin_email.png").similar(0.90).targetOffset(-169,29))
    
    FIND(region,Pattern("signin_pw.png").similar(0.90).targetOffset(-199,-39))
    
    FIND(region,Pattern("signin_needAccountJoinNow.png").similar(0.90).targetOffset(63,2))
    
    FIND(region,Pattern("signin_forgotpw.png").similar(0.90).targetOffset(1,19))
    
    FIND(region,Pattern("signin_resendConfirmation.png").similar(0.90).targetOffset(-3,14))

    FIND(region,Pattern("signin_signin.png").similar(0.90))
    
    
##########################################
#
##########################################
def signin_Login(region,login,pw):

    TYPE(region,Pattern("signin_email.png").similar(0.90).targetOffset(-169,29),login)

    TYPE(region,Pattern("signin_pw.png").similar(0.90).targetOffset(-199,-39),pw)
    
    CLICK(region,Pattern("signin_signin.png").similar(0.90))
    
    WAIT(region,Pattern("getstarted_getstartedWithGP.png").similar(0.90),15)

##########################################
#
##########################################
def getstarted_gopro(REGION):
    WAIT(REGION,Pattern("media_txt_title.png").similar(0.91),30) #media_txt_title.png
    
    FIND(REGION,Pattern("media_btn_choosefolder.png").similar(0.92).targetOffset(0,86)) #media_btn_choosefolder.png
    FIND(REGION,Pattern("media_btn_connectcam.png").similar(0.90).targetOffset(-2,85)) #media_btn_connectcam.png
    #if d_gda_settings["isMac"]=="True": #no popup in win
    #    CLICK(REGION,Pattern("popup_btn_indexinfo.png").similar(0.91).targetOffset(143,-2)) #popup_btn_indexinfo.png


    FIND(REGION,Pattern("media_selected_media.png").similar(0.91)) #media_selected_media.png
    FIND(REGION,Pattern("media_unselected_recentlyadd.png").similar(0.91)) #media_unselected_recentlyadd.png

    FIND(REGION,Pattern("media_unselected_edits.png").similar(0.91)) #media_unselected_edits.png
    FIND(REGION,Pattern("media_img_addmedia.png").similar(0.91)) #media_img_addmedia.png

    FIND(REGION,Pattern("media_btn_settings.png").similar(0.91)) #media_btn_settings.png

    FIND(REGION,Pattern("media_txt_autogdasignin.png").exact())  #media_txt_autogdasignin.png
    
    CLICK(REGION,Pattern("media_txt_media-editor.png").exact().targetOffset(46,1)) #media_txt_media-editor
    
    WAIT(REGION,Pattern("popup_txt_pleasechoosevideos.png").exact(),10) #popup_txt_pleasechoosevideos.png
    
    FIND(REGION,Pattern("popup_txt_theeditorcanonlyopenvideos.png").exact()) #popup_txt_theeditorcanonlyopenvideos.png
    
    CLICK(REGION,Pattern("popup_btn_choosevideos-OK.png").exact()) #popup_btn_choosevideos-OK
    
    WAIT(REGION,Pattern("media_txt_title.png").similar(0.91),10) #media_txt_title.png

    FIND(REGION,Pattern("media_txt_media-editor.png").exact().targetOffset(-38,-1)) #media_txt_media-editor

    
##########################################
#
##########################################
def addmedia_validate(region):
    CLICK(region,Pattern("getstarted_choosefolder.png").similar(0.90).targetOffset(0,96))
    
    WAIT(region,Pattern("dialogFindGPMedia_Title.png").similar(0.90),10)
      
    FIND(region,Pattern("dialogFindGPMedia_ChooseFolders.png").similar(0.90))
      
    CLICK(region,Pattern("dialogFindGPMedia_Addfolder.png").similar(0.90).targetOffset(-6,-19))
    
    #assume the dialog pops up over the GoPro region
    #WAIT(region,Pattern("osxdialog_filedialog.png").similar(0.90).targetOffset(40,2))
    #wait(1)    
    #region.waitVanish(Pattern("osxdialog_filedialog.png").similar(0.90).targetOffset(40,2),5)
    type(Key.ENTER)

    wait(1)

    CLICK(region,Pattern("dialogFindGPMedia_Addfolder.png").similar(0.90).targetOffset(0,37))
    

    CLICK(region,Pattern("GPSettings_seconditem.png").similar(0.90).targetOffset(43,17))
    
    CLICK(region,Pattern("dialogYsure_Remove.png").similar(0.90))
    

    CLICK(region,Pattern("GPSettings_BackToMedia.png").similar(0.90).targetOffset(-29,-30))
    
    # region.click(Pattern("dialogFindGPMedia_Cancel.png").similar(0.90).targetOffset(-15,7))
def test_getGDAVersion(REGION):
    
    FIND(REGION, Pattern("popup_txt_version200.png").exact()) #popup_txt_version200
    
    FIND(REGION, Pattern("popup_txt_versiongdainfo.png").exact()) #popup_txt_versiongdainfo
    m=FIND(REGION, Pattern("popup_txt_version_ocr.png").exact()) #popup_txt_version_ocr
    if m:
        print m.text()
    
def startup(region):
   
    #######################################
    ###  firststartup    
    #
    WAIT(region,Pattern("startup_txt_title.png").exact(),10)

    FIND(region,Pattern("startup_img_logo.png").similar(0.91))

    CLICK(region,Pattern("startup_checked_autolaunchcam.png").similar(0.91).targetOffset(-190,0))

    CLICK(region,Pattern("startup_unchecked_autolaunchcam.png").similar(0.91).targetOffset(-190,0))

    FIND(region,Pattern("startup_img_camhappy.png").similar(0.91)) #startup_img_camhappy.png

    FIND(region,Pattern("startup_img_findmoments.png").similar(0.92)) #startup_img_findmoments.png

    FIND(region,Pattern("startup_img_importmedia.png").similar(0.91)) #startup_img_importmedia.png

    CLICK(region,Pattern("startup_btn_continue.png").similar(0.90)) #startup_btn_continue.png

    #CLICK(region,Pattern("startup_autoLaunchCamOnGP.png").similar(0.90))

    #CLICK(region,Pattern("startup_unslectedAutoLaunchGP.png").similar(0.91))


    #CLICK(region,Pattern("startup_continue.png").similar(0.90))

def startup_newAcct(region):
    WAIT(region,Pattern("startupCreateAcct_title.png").similar(0.91))
    
    FIND(region,Pattern("startupCreateAcct_form1.png").similar(0.90))

    FIND(region,Pattern("startupCreateAcct_form2.png").similar(0.91))
    
    FIND(region,Pattern("startupCreateAcct_form3.png").similar(0.90))

    CLICK(region,Pattern("startupCreateAcct.png").similar(0.90))
    
 
    
    
##########################################
#
##########################################
def imagerepo():
    #sorted png name order below
    
    find("camsettings_btn_h4blacksettings.png") #camsettings_btn_h4blacksettings.png
    find("camsettings_btn_h4sessionsettings.png") #camsettings_btn_h4sessionsettings.png
    find("camsettings_btn_h4silversettings.png") #camsettings_btn_h4silversettings.png
    find("camsettings_img_h4black.png") #camsettings_img_h4black.png
    find("camsettings_img_h4session.png") #camsettings_img_h4session.png
    find("camsettings_img_h4silver.png") #camsettings_img_h4silver.png
    find("camsettings_txt_title.png") #camsettings_txt_title.png
    find("conncam_btn_getsupport.png") #conncam_btn_getsupport.png
    find("conncam_btn_gotit.png") #conncam_btn_gotit.png
    find("conncam_txt_camon.png") #conncam_txt_camon.png
    find("conncam_txt_plugcam.png") #conncam_txt_plugcam.png
    find("conncam_txt_selectimport.png") #conncam_txt_selectimport.png
    find("conncam_txt_title.png") #conncam_txt_title.png
    find("createacct_btn_getacct.png") #createacct_btn_getacct.png
    find("createacct_btn_signin.png") #createacct_btn_signin.png
    find("createacct_checked_getnews.png") #createacct_checked_getnews.png
    find("createacct_checked_iacknowledge.png") #createacct_checked_iacknowledge.png
    find("createacct_txt_invalidemail.png") #createacct_txt_invalidemail.png
    find("createacct_txt_subtitle.png") #createacct_txt_subtitle.png
    find("createacct_txt_title.png") #createacct_txt_title.png
    find("createacct_txtbox_email.png") #createacct_txtbox_email.png
    find("createacct_txtbox_password.png") #createacct_txtbox_password.png
    find("createacct_unchecked_getnews.png") #createacct_unchecked_getnews.png
    find("createacct_unchecked_iacknowledge.png") #createacct_unchecked_iacknowledge.png
    find("edits_btn_createedit.png") #edits_btn_createedit.png
    find("edits_img_edits.png") #edits_img_edits.png
    find("edits_txt_info.png") #edits_txt_info.png
    find("edits_txt_noedits.png") #edits_txt_noedits.png
    find("findmedia_btn_addfolder.png") #findmedia_btn_addfolder.png
    find("findmedia_btn_cancel.png") #findmedia_btn_cancel.png
    find("findmedia_btn_close.png") #findmedia_btn_close.png
    find("findmedia_btn_managefoldersettings.png") #findmedia_btn_managefoldersettings.png
    find("findmedia_btn_save.png") #findmedia_btn_save.png
    find("findmedia_txt_subtitle.png") #findmedia_txt_subtitle.png
    find("findmedia_txt_title.png") #findmedia_txt_title.png
    find("gensettings_btn_addnew.png") #gensettings_btn_addnew.png
    find("gensettings_btn_importlocation.png") #gensettings_btn_importlocation.png
    find("gensettings_btn_mediafoldersscan.png") #gensettings_btn_mediafoldersscan.png
    find("gensettings_selected_autodownload.png") #gensettings_selected_autodownload.png
    find("gensettings_selected_autolaunchapp.png") #gensettings_selected_autolaunchapp.png
    find("gensettings_selected_autoplay.png") #gensettings_selected_autoplay.png
    find("gensettings_selected_autosync.png") #gensettings_selected_autosync.png
    find("gensettings_txt_importlocation.png") #gensettings_txt_importlocation.png
    find("gensettings_txt_mediafolders.png") #gensettings_txt_mediafolders.png
    find("gensettings_txt_title.png") #gensettings_txt_title.png
    find("gensettings_unseleted_autodownload.png") #gensettings_unseleted_autodownload.png
    find("gensettings_unseleted_autolaunchapp.png") #gensettings_unseleted_autolaunchapp.png
    find("gensettings_unseleted_autoplay.png") #gensettings_unseleted_autoplay.png
    find("gensettings_unseleted_autosync.png") #gensettings_unseleted_autosync.png
    find("media_btn_choosefolder.png") #media_btn_choosefolder.png
    find("media_btn_connectcam.png") #media_btn_connectcam.png
    find("media_btn_settings.png") #media_btn_settings.png
    find("media_img_addmedia.png") #media_img_addmedia.png
    find("media_img_alerts.png") #media_img_alerts.png
    find("media_selected_edits.png") #media_selected_edits.png
    find("media_selected_hero4black.png") #media_selected_hero4black.png
    find("media_selected_hero4session.png") #media_selected_hero4session.png
    find("media_selected_hero4silver.png") #media_selected_hero4silver.png
    find("media_selected_media.png") #media_selected_media.png
    find("media_selected_recentlyadd.png") #media_selected_recentlyadd.png
    find("media_txt_title.png") #media_txt_title.png
    find("media_unselected_edits.png") #media_unselected_edits.png
    find("media_unselected_hero4black.png") #media_unselected_hero4black.png
    find("media_unselected_hero4session.png") #media_unselected_hero4session.png
    find("media_unselected_hero4silver.png") #media_unselected_hero4silver.png
    find("media_unselected_media.png") #media_unselected_media.png
    find("media_unselected_recentlyadd.png") #media_unselected_recentlyadd.png
    find("mediacam_btn_importfiles.png") #mediacam_btn_importfiles.png
    find("mediacam_txt_spaceused.png") #mediacam_txt_spaceused.png
    find("mediacamsettings_btn_cancel.png") #mediacamsettings_btn_cancel.png
    find("mediacamsettings_btn_close.png") #mediacamsettings_btn_close.png
    find("mediacamsettings_btn_save.png") #mediacamsettings_btn_save.png
    find("mediacamsettings_checked_autodelete.png") #mediacamsettings_checked_autodelete.png
    find("mediacamsettings_checked_autoimport.png") #mediacamsettings_checked_autoimport.png
    find("mediacamsettings_unchecked_autodelete.png") #mediacamsettings_unchecked_autodelete.png
    find("mediacamsettings_unchecked_autoimport.png") #mediacamsettings_unchecked_autoimport.png
    find("mediah4black_img_logo.png") #mediah4black_img_logo.png
    find("mediah4black_txt_available.png") #mediah4black_txt_available.png
    find("mediah4black_txt_capacity.png") #mediah4black_txt_capacity.png
    find("mediah4black_txt_subtitle.png") #mediah4black_txt_subtitle.png
    find("mediah4black_txt_title.png") #mediah4black_txt_title.png
    find("mediah4black_txt_used.png") #mediah4black_txt_used.png
    find("mediah4session_img_logo.png") #mediah4session_img_logo.png
    find("mediah4session_txt_available.png") #mediah4session_txt_available.png
    find("mediah4session_txt_capacity.png") #mediah4session_txt_capacity.png
    find("mediah4session_txt_subtitle.png") #mediah4session_txt_subtitle.png
    find("mediah4session_txt_title.png") #mediah4session_txt_title.png
    find("mediah4session_txt_used.png") #mediah4session_txt_used.png
    find("mediah4silver_img_logo.png") #mediah4silver_img_logo.png
    find("mediah4silver_txt_available.png") #mediah4silver_txt_available.png
    find("mediah4silver_txt_capacity.png") #mediah4silver_txt_capacity.png
    find("mediah4silver_txt_subtitle.png") #mediah4silver_txt_subtitle.png
    find("mediah4silver_txt_title.png") #mediah4silver_txt_title.png
    find("mediah4silver_txt_used.png") #mediah4silver_txt_used.png
    find("mediasettingsh4black_txt_cammodel.png") #mediasettingsh4black_txt_cammodel.png
    find("mediasettingsh4black_txtbox_camfolder.png") #mediasettingsh4black_txtbox_camfolder.png
    find("mediasettingsh4session_txt_cammodel.png") #mediasettingsh4session_txt_cammodel.png
    find("mediasettingsh4session_txtbox_camfolder.png") #mediasettingsh4session_txtbox_camfolder.png
    find("mediasettingsh4silver_txt_cammodel.png") #mediasettingsh4silver_txt_cammodel.png
    find("mediasettingsh4silver_txtbox_camfolder.png") #mediasettingsh4silver_txtbox_camfolder.png
    find("popup_btn_indexinfo.png") #popup_btn_indexinfo.png
    find("recentlyadd_btn_addmedia.png") #recentlyadd_btn_addmedia.png
    find("recentlyadd_btn_connectcam.png") #recentlyadd_btn_connectcam.png
    find("recentlyadd_txt_title.png") #recentlyadd_txt_title.png
    find("settings_btn_backtomedia.png") #settings_btn_backtomedia.png
    find("settings_selected_camsettings.png") #settings_selected_camsettings.png
    find("settings_selected_gensettings.png") #settings_selected_gensettings.png
    find("settings_unselected_camsettings.png") #settings_unselected_camsettings.png
    find("settings_unselected_gensettings.png") #settings_unselected_gensettings.png
    find("signin_btn_forgot.png") #signin_btn_forgot.png
    find("signin_btn_needacct.png") #signin_btn_needacct.png
    find("signin_btn_resendemail.png") #signin_btn_resendemail.png
    find("signin_btn_signin.png") #signin_btn_signin.png
    find("signin_img_logo.png") #signin_img_logo.png
    find("signin_txt_invalidemail.png") #signin_txt_invalidemail.png
    find("signin_txt_title.png") #signin_txt_title.png
    find("signin_txtbox_emailpw_blankpw.png") #signin_txtbox_emailpw_blankpw.png
    find("signin_txtbox_emailpw.png") #signin_txtbox_emailpw.png
    find("startup_btn_continue.png") #startup_btn_continue.png
    find("startup_checked_autolaunchcam.png") #startup_checked_autolaunchcam.png
    find("startup_img_camhappy.png") #startup_img_camhappy.png
    find("startup_img_findmoments.png") #startup_img_findmoments.png
    find("startup_img_importmedia.png") #startup_img_importmedia.png
    find("startup_img_logo.png") #startup_img_logo.png
    find("startup_txt_title.png") #startup_txt_title.png
    find("startup_unchecked_autolaunchcam.png") #startup_unchecked_autolaunchcam.png
    find("user_btn_select.png") #user_btn_select.png
    find("user_btn_signoff.png") #user_btn_signoff.png
    find("media_txt_autogdasignin.png")
    find("media_txt_media-editor.png")  #media_txt_media-editor
    
    find("popup_txt_pleasechoosevideos.png") #popup_txt_pleasechoosevideos.png
    
    find("popup_txt_theeditorcanonlyopenvideos.png") #popup_txt_theeditorcanonlyopenvideos.png
    
    find("popup_btn_choosevideos-OK.png") #popup_btn_choosevideos-OK
    
    find("popup_txt_version200.png") #popup_txt_version200
    
    find("popup_txt_versiongdainfo.png") #popup_txt_versiongdainfo
    find("popup_txt_version_ocr.png") #popup_txt_version_ocr
    
##########################################


##########################################
def BAT(gpa, gpr):
    global startup
    global d_similarity
    
    gpr=refreshregion(gpa)
    startup(gpr)
    if not putDictToFile(d_similarity):
        exit(1)
    gpr=refreshregion(gpa)
    create_your_acct(gpr) #fail
    if not putDictToFile(d_similarity):
        exit(1)
    
    gpr=refreshregion(gpa)
    signin_test(gpr) #fail
    if not putDictToFile(d_similarity):
        exit(1)
    
    gpr=refreshregion(gpa)
    signin_test(gpr,False,"autogda00@gmail.com","access4auto") #login
    if not putDictToFile(d_similarity):
        exit(1)

    gpr=refreshregion(gpa)
    getstarted_gopro(gpr) #media screen
    if not putDictToFile(d_similarity):
        exit(1)
         
    #gpr=refreshregion(gp)
    #signin_test(gpr)                
    #if startupcnt == 0:
    #startup(gpr)
    #gpr=refreshregion(gp)
    #startup_newAcct(gpr)
    #startup=1
    #gpr=refreshregion(gp)    
    #signin_validate(gpr)    
    #gpr=refreshregion(gp)
    #signin_Login(gpr,"autogda00@gmail.com","autogda00")
    #gpr=refreshregion(gp)
    #startup=1
    #getstarted_validate(gpr)
    #gpr=refreshregion(gp)
    #addmedia_validate(gpr)
    #signout(gpr) 


def DEBUG(gpa, gpr):
    gpr=refreshregion(gpa)
    test_getGDAVersion(gpr)
    if not putDictToFile(d_similarity):
        exit(1)

    
##########################################
# main script
##########################################

GetEnvInfo()
#gp,gpr=AppStartRetry("GoPro",3)
gpa,gpr=AppStart("GoPro")

if not gpa:
    print "App Start Failed"
    exit(1)
if not gpr:
    print "App Window Region not found"
    if gpa:
        gpa.close()
    exit(1)
print gpr.w    
print gpr.h
d_similarity=getDictFromFile()
if d_similarity:
    print "JSON ====================="
    print json.dumps(d_similarity)
    print "=========================="
else:
    print "JSON ====================="
    print "FAILED TO Load JSON: No file found"
    print "=========================="        
ScreenShot(gpr,"startup")

BAT(gpa,gpr)
#DEBUG(gpa,gpr)
printreport()
#gpa.close()

