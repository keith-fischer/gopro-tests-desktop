import gda_utils

from sikuli import Sikuli
from sikuli import *
from __builtin__ import True, False
import org.sikuli.basics.SikulixForJython

class CloudSettings:
    def __init__(self):
        self.auto_launch=False
        self.auto_download=False
        self.auto_play=False
        self.auto_sync=False
        self.import_location=""
        self.media_folder=[]
        self.fails="\nCloudSettings: REPORT TESTS FAILED"
        self.passes="\nCloudSettings: REPORT TESTS PASSED"
        
    def evalcloudsettings(self):
        p=Pattern("gensettings_btn_backtomedia.png").similar(0.69) # gensettings_btn_backtomedia
        rsettings=gda_utils.EXISTS3("CLOUDSETTINGS","TOP",p,5)
        if not rsettings:
            self.fails += "\nFAILED to find: %s" % str(p)
        else:
            self.passes += "\nPASSED: %s" % str(p)

        p=Pattern("cloudsettings_btn_gensettings-unselected.png").similar(0.68) # cloudsettings_btn_gensettings-unselected
        rsettings=gda_utils.EXISTS3("CLOUDSETTINGS","LEFTPANEL",p,5)
        if not rsettings:
            self.fails += "\nFAILED to find: %s" % str(p)
        else:
            self.passes += "\nPASSED: %s" % str(p)
            
        p=Pattern("cloudsettings_btn_selected.png").similar(0.69) # cloudsettings_btn_selected
        rsettings=gda_utils.EXISTS3("CLOUDSETTINGS","LEFTPANEL",p,5)
        if not rsettings:
            self.fails += "\nFAILED to find: %s" % str(p)
        else:
            self.passes += "\nPASSED: %s" % str(p)
            
        p=Pattern("gensettings_btn_feedback.png").similar(0.68) # gensettings_btn_feedback
        rsettings=gda_utils.EXISTS3("CLOUDSETTINGS","LEFTPANEL",p,5)
        if not rsettings:
            self.fails += "\nFAILED to find: %s" % str(p)
        else:
            self.passes += "\nPASSED: %s" % str(p)
            
        p=Pattern("gensettings_lbl_title-settings.png").similar(0.69) #gensettings_lbl_title-settings
        rsettings=gda_utils.EXISTS3("CLOUDSETTINGS","TITLE",p,5)
        if not rsettings:
            self.fails += "\nFAILED to find: %s" % str(p)
        else:
            self.passes += "\nPASSED: %s" % str(p)
        
        p=Pattern("cloudsettings_lbl_mediatransfer.png").similar(0.69) # cloudsettings_lbl_mediatransfer
        rsettings=gda_utils.EXISTS3("CLOUDSETTINGS","SETTINGS_MEDIATRANSFER",p,5)
        if not rsettings:
            self.fails += "\nFAILED to find: %s" % str(p)
        else:
            self.passes += "\nPASSED: %s" % str(p)
            
        
        p=Pattern("cloudsettings_chk_autoupload-unchecked.png").similar(0.69) # cloudsettings_chk_autoupload-unchecked
        rsettings=gda_utils.EXISTS3("CLOUDSETTINGS","SETTINGS_MEDIATRANSFER",p,5)
        if not rsettings:
            self.fails += "\nFAILED to find: %s" % str(p)
        else:
            self.passes += "\nPASSED: %s" % str(p)
            rsettings.click()
        
        p=Pattern("cloudsettings_chk_autoupload-checked.png").similar(0.68) # cloudsettings_chk_autoupload-checked
        rsettings=gda_utils.EXISTS3("CLOUDSETTINGS","SETTINGS_MEDIATRANSFER",p,5)
        if not rsettings:
            self.fails += "\nFAILED to find: %s" % str(p)
        else:
            self.passes += "\nPASSED: %s" % str(p)
            rsettings.click()
        
        p=Pattern("cloudsettings_chk_allowmediaupload-unchecked.png").similar(0.69) # cloudsettings_chk_allowmediaupload-unchecked
        rsettings=gda_utils.EXISTS3("CLOUDSETTINGS","SETTINGS_MEDIATRANSFER",p,5)
        if not rsettings:
            self.fails += "\nFAILED to find: %s" % str(p)
        else:
            self.passes += "\nPASSED: %s" % str(p)
            rsettings.click()
        
        p=Pattern("cloudsettings_chk_allowmediaupload-checked.png").similar(0.69) # cloudsettings_chk_allowmediaupload-checked
        rsettings=gda_utils.EXISTS3("CLOUDSETTINGS","SETTINGS_MEDIATRANSFER",p,5)
        if not rsettings:
            self.fails += "\nFAILED to find: %s" % str(p)
        else:
            self.passes += "\nPASSED: %s" % str(p)
            rsettings.click()
    
        
        p=Pattern("cloudsettings_btn_managesubscriptions.png").similar(0.69) #  cloudsettings_btn_managesubscriptions
        rsettings=gda_utils.EXISTS3("CLOUDSETTINGS","SETTINGS_MEDIATRANSFER",p,5)
        if not rsettings:
            self.fails += "\nFAILED to find: %s" % str(p)
        else:
            self.passes += "\nPASSED: %s" % str(p)




######################################
# Assumes automation window size Mac{x35,y35,w1280, h836}
# for windows using Autoit we need to identify the inner region w,h relative to mac and set the win size accordingly
# Win,Mac window container border widths are different
# this is global region list for more accurate image query
######################################
def set_cloudsettings_regions(REGION):
    
    screenregion="CLOUDSETTINGS"
    subregion="TOP"
    rx=REGION.getX()
    ry=REGION.getY()#+REGION.getH()-80
    rw=REGION.getW()
    rh=80
    r=Region(rx,ry,rw,rh)
    #r.highlight(1)
    gda_utils.add_region(screenregion,subregion,r)
    
    subregion="LEFTPANEL"
    rx=REGION.getX()
    ry=REGION.getY()+80
    rw=238    
    rh=REGION.getH()-80
    r=Region(rx,ry,rw,rh)
    #r.highlight(5)
    gda_utils.add_region(screenregion,subregion,r)
    
    subregion="TITLE"
    rx=REGION.getX()+ 238
    ry=REGION.getY()+90
    rw=REGION.getW()-238
    rh=80
    r=Region(rx,ry,rw,rh)
    #r.highlight(5)
    gda_utils.add_region(screenregion,subregion,r)

    subregion="SETTINGS_MEDIATRANSFER"
    r=r.below(300)
    r.highlight(5)
    gda_utils.add_region(screenregion,subregion,r)




    
######################################
# for debugging in sikuli ide
# 
# 
######################################
def test_module():
    gda_utils.GetEnvInfo()
    gpa,gpr=gda_utils.AppStart("GoPro")
    set_cloudsettings_regions(gpr)
    g=CloudSettings()
    if not g:
        print "Error: failed to create CloudSettings class"
        return
    g.evalcloudsettings()
    print g.passes
    print g.fails
    
######################################
# for debugging in sikuli ide
# 
# KEEP THIS COMMENTED when checking in to GIT
######################################    
test_module()    