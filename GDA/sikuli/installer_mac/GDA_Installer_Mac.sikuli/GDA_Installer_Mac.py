
from sikuli import *
import org.sikuli.script.ImagePath
import shlex
from subprocess import Popen, PIPE




#Uninstall GDA
#Cleanup
#Install GDA


#hdiutil mount cotvnc-20b4.dmg

# todo -----------------
# mount dmg
# run gopro.pkg
# get process window handle
# set window region
# move window to center
# run sikuli headless on jython
# cmdline args for dmg path
# copy to local
# aquire the build number/version
# cleanup of local dmg
# config property data structure
# 
#------------------------
def RunProc(proc,arg):
    process = Popen(shlex.split(cmd), stdout=PIPE)
    process.communicate()
    exit_code = process.wait()

def AppStart(appname): 
    
    a1 = App(appname)
    if not a1.isRunning():
        print "FAILED: App not running"
        exit(1)
    a1.focus()
    r0 = a1.window(0)
    if not r0:
        print "Failed: Window region not found"
        print r0
        return r0
    r0.highlight(1)
    #r0.wait("Welcome_GDA_Title.png")
    #text("Welcome_GDA_Title.png","Passed")
    return r0

r0=AppStart("Installer")
if not r0:
    exit(1)








