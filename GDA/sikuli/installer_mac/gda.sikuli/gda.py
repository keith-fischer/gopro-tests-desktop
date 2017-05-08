

#import org.sikuli.basics.SikulixForJython
from sikuli import *
import org.sikuli.script.ImagePath
#import HelperLib
#from guide import *

global settings{}

def GetEnvInfo():
    settings["sikuli_ver"]=Env.getSikuliVersion()
    #print "OS:"+getOS()
    #print "OSUtil:"+Env.getOSUtil()
    #print "OSVersion:"+getOSVersion()
    print "DataPath:"+Env.getSikuliDataPath()
    #print "Mac:"+En.isMac()
    #print "Win:"+En.isWindows()
    print "BundleFolder="+getBundleFolder()
    print "ParentPath="+getParentPath()
    
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

def AppStart(appname): 
    print "openApp>"

    a1 = App(appname)
    if not a1:
        a1 = openApp(appname+".app")
        print "openApp"
        
        a1 = App(appname)
        if a1:
            if not a1.isRunning():
                waitcount =10
                while not a1.isRunning():
                    waitcount = waitcount - 1
                    if waitcount == 0:
                        print "failed startup timeout"
                        exit(1)
                    wait(1)
        else:
            print "App " + appname + " failed to startup"
            exit(1)
#    if not a1.isRunning():
#        print "App " + appname + " is not running"
#        exit(1) 

    wait(5)
    a1.focus()
    r0 =a1.focusedWindow()
    if not r0:
        print "Failed: Window region not found"
        return r0
    
    r0.highlight(1)
    print "<openApp"
    return a1, r0



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







GetEnvInfo()
gp,gpr=AppStart("GoPro.")
if not gp:
    print "AppStart Failed"
    exit(1)
print getmactitle()
gp.focus()
print gp.getWindow()
print gp.getPID()
print gp.getName()



