import org.sikuli.script.ImagePath
from sikuli import Sikuli
from sikuli import *
from __builtin__ import True, False
import org.sikuli.basics.SikulixForJython
import gda_utils


def script_init():
    gda_utils.GetEnvInfo()
    app_gda, region_gda = gda_utils.AppStart("Quik",0,0)

    if app_gda and region_gda:
        print("target region is ready")
        return app_gda,region_gda
    print "Failed to init Quik region"
    exit(-1)
    
def gda_signin(region,login,pw):
    rc = False
    try: #marks code
        #region.find("signInEmailAddress.png")
        region.click("signInEmailAddress.png")
        region.type(login)
        #region.find("SignIn_Password.png")
        region.click("SignIn_Password.png")
        region.type(pw)
        #region.find("SignIn_Button.png")
        region.click("SignIn_Button.png")
        if region.exists("view_title_media.png",30):
            rc=True
    except:
        print "Failed: gda_signin"
    return rc
def do_test1(region):
    rc=False
      
    rc=gda_signin(region,"mmyers@gopro.com","Jeep_4me")
    if rc:
        print "gda_signin PASSED=%s" % rc
    else:
        print "gda_signin FAILED=%s" % rc
                                
def main():
    app_gda,region_gda=script_init()
    do_test1(region_gda)
main()