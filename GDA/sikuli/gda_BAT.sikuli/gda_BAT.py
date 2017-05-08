import gda_utils

from sikuli import Sikuli
from sikuli import *
from __builtin__ import True, False
import org.sikuli.basics.SikulixForJython
import org.sikuli.script.ImagePath


##########################################
#
##########################################
def create_your_acct(REGION,willfail=True,fname="john",lname="doe",email="jdoe@jdoe.zzz",pw="1234567890"):
    gda_utils.WAIT(REGION,Pattern("createacct_txt_title.png").exact()) #createacct_txt_title.png
    
    gda_utils.FIND(REGION,Pattern("createacct_txt_subtitle.png").similar(0.90)) #createacct_txt_subtitle.png

    gda_utils.TYPE(REGION,Pattern("createacct_txtbox_email.png").exact().targetOffset(-232,23),fname) #createacct_txtbox_email.png
    gda_utils.TYPE(REGION,Pattern("createacct_txtbox_email.png").exact().targetOffset(51,26),lname) #createacct_txtbox_email.png
    gda_utils.TYPE(REGION,Pattern("createacct_txtbox_email.png").exact().targetOffset(-245,-32),email) #createacct_txtbox_email.png
    gda_utils.TYPE(REGION,Pattern("createacct_txtbox_password.png").exact().targetOffset(-216,-29),pw) #createacct_txtbox_password.png
    gda_utils.TYPE(REGION,Pattern("createacct_txtbox_password.png").exact().targetOffset(-247,28),pw) #createacct_txtbox_password.png

    if gda_utils.d_gda_settings["isWindows"]=="True":
        gda_utils.CLICK(REGION,Pattern("createacct_unchecked_getnews.png").exact().targetOffset(-240,-4)) #createacct_unchecked_getnews.png
        gda_utils.FIND(REGION,Pattern("createacct_checked_getnews.png").exact().targetOffset(-246,-5)) #createacct_checked_getnews.png
        gda_utils.CLICK(REGION,Pattern("createacct_unchecked_iacknowledge.png").similar(0.98).targetOffset(-275,-7)) #createacct_unchecked_iacknowledge.png
        gda_utils.FIND(REGION,Pattern("createacct_checked_iacknowledge.png").similar(0.91).targetOffset(-272,-2)) #createacct_checked_iacknowledge.png
    
    if gda_utils.d_gda_settings["isMac"]=="True":
        gda_utils.CLICK(REGION,Pattern("createacct_unchecked-mac_getnews.png").exact().targetOffset(-249,7)) #createacct_unchecked-mac_getnews.png
        gda_utils.FIND(REGION,Pattern("createacct_checked-mac_getnews.png").exact().targetOffset(-248,2)) #createacct_checked-mac_getnews.png
        gda_utils.CLICK(REGION,Pattern("createacct_unchecked-mac_iacknowledge.png").similar(0.98).targetOffset(-270,-5)) #createacct_unchecked-mac_iacknowledge.png
        gda_utils.FIND(REGION,Pattern("createacct_checked-mac_iacknowledge.png").similar(0.98).targetOffset(-271,-5)) #createacct_checked-mac_iacknowledge.png


        
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
    gda_utils.WAIT(REGION,Pattern("signin_txt_title.png").similar(0.90),30)

    gda_utils.FIND(REGION,Pattern("signin_img_logo.png").similar(0.90))

    gda_utils.TYPE(REGION,Pattern("signin_txtbox_emailpw.png").similar(0.90).targetOffset(-185,-38),email)
    gda_utils.TYPE(REGION,Pattern("signin_txtbox_emailpw.png").similar(0.90).targetOffset(-211,22),pw)


    gda_utils.FIND(REGION,Pattern("signin_btn_forgot.png").similar(0.90))
  

    gda_utils.FIND(REGION,Pattern("signin_btn_resendemail.png").similar(0.90))

    gda_utils.CLICK(REGION,Pattern("signin_btn_signin.png").similar(0.90))
    #test invalid acct
    if willfail==True:

        gda_utils.WAIT(REGION,Pattern("signin_txt_invalidemail.png").similar(0.92),30) #signin_txt_invalidemail.png

        gda_utils.FIND(REGION,Pattern("signin_txtbox_emailpw_blankpw.png").similar(0.91))
        cleanfld=Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE+Key.BACKSPACE
        gda_utils.TYPE(REGION,Pattern("signin_txtbox_emailpw.png").similar(0.90).targetOffset(210,-38),cleanfld)
        
        #CLICK(REGION,Pattern("signin_btn_needacct.png").similar(0.90).targetOffset(67,9))
        #WAIT(REGION,Pattern("createacct_txt_title-1.png").similar(0.90)) #createacct_txt_title.png
        #CLICK(REGION,Pattern("createacct_btn_signin-1.png").similar(0.91)) #createacct_btn_signin.png

        #WAIT(REGION,Pattern("signin_txt_title.png").similar(0.90),30)
        
        
    #else: #is valid acct
        #CLICK(REGION,Pattern("signin_btn_needacct.png").similar(0.90).targetOffset(67,9))

##########################################
#
##########################################
def media_getstarted_gopro(REGION):
    gda_utils.WAIT(REGION,Pattern("media_txt_title.png").similar(0.91),30) #media_txt_title.png
    
    gda_utils.FIND(REGION,Pattern("media_btn_choosefolder.png").similar(0.92).targetOffset(0,86)) #media_btn_choosefolder.png
    gda_utils.FIND(REGION,Pattern("media_btn_connectcam.png").similar(0.90).targetOffset(-2,85)) #media_btn_connectcam.png
    #if gda_utils.d_gda_settings["isMac"]=="True": #no popup in win
    #    CLICK(REGION,Pattern("popup_btn_indexinfo.png").similar(0.91).targetOffset(143,-2)) #popup_btn_indexinfo.png


    gda_utils.FIND(REGION,Pattern("media_selected_media.png").similar(0.91)) #media_selected_media.png
    gda_utils.FIND(REGION,Pattern("media_unselected_recentlyadd.png").similar(0.91)) #media_unselected_recentlyadd.png

    gda_utils.FIND(REGION,Pattern("media_unselected_edits.png").similar(0.91)) #media_unselected_edits.png
    gda_utils.FIND(REGION,Pattern("media_img_addmedia.png").similar(0.91)) #media_img_addmedia.png

    gda_utils.FIND(REGION,Pattern("media_btn_settings.png").similar(0.91)) #media_btn_settings.png

    gda_utils.FIND(REGION,Pattern("media_txt_autogdasignin.png").exact())  #media_txt_autogdasignin.png
    
    gda_utils.CLICK(REGION,Pattern("media_txt_media-editor.png").exact().targetOffset(46,1)) #media_txt_media-editor
    
    gda_utils.WAIT(REGION,Pattern("popup_txt_pleasechoose.png").exact(),10) #popup_txt_pleasechoose.png
    gda_utils.FIND(REGION,Pattern("popup_txt_pleasevideos.png").exact()) #popup_txt_pleasevideos.png
    
    gda_utils.FIND(REGION,Pattern("popup_txt_theeditorcanonlyopenvideos.png").exact()) #popup_txt_theeditorcanonlyopenvideos.png
    gda_utils.FIND(REGION,Pattern("popup_txt_pleaseselect.png").exact()) #popup_txt_pleaseselect.png
    gda_utils.FIND(REGION,Pattern("popup_txt_andtryagain.png").exact()) #popup_txt_theeditorcanonlyopenvideos.png
    
    gda_utils.CLICK(REGION,Pattern("popup_btn_choosevideos-OK.png").exact()) #popup_btn_choosevideos-OK
    
    gda_utils.WAIT(REGION,Pattern("media_txt_title.png").similar(0.91),10) #media_txt_title.png

    gda_utils.FIND(REGION,Pattern("media_txt_media-editor.png").exact().targetOffset(-38,-1)) #media_txt_media-editor

    
def media_settings(REGION):
    gda_utils.CLICK(REGION,Pattern("media_btn_settings.png").exact().targetOffset(17,1)) #media_btn_settings.png

    gda_utils.WAIT(REGION,Pattern("media-settings_txt_settings.png").exact(),20) #media-settings_txt_settings.png
    gda_utils.FIND(REGION,Pattern("media-settings_btn_generalsettings-enable.png").exact()) #media-settings_btn_generalsettings-enable.png   
    gda_utils.FIND(REGION,Pattern("media-settings_txt_importlocation.png").exact()) #media-settings_txt_importlocation.png 
    gda_utils.FIND(REGION,Pattern("media-settings_txt_mediafolders.png").exact()) #media-settings_txt_mediafolders.png
    #removed
    #FIND(REGION,Pattern("media-settings_btn_camsettings-disable.png").exact()) #media-settings_btn_camsettings-disable.png 
    gda_utils.FIND(REGION,Pattern("media-settings_btn_cloudsettings-disable.png").exact()) #media-settings_btn_cloudsettings-disable.png 
    gda_utils.CLICK(REGION, Pattern("gensettings_checked_autodownload.png").exact().targetOffset(-157,-1))  #gensettings_checked_autodownload.png
    gda_utils.CLICK(REGION,Pattern("gensettings_uncheck_autodownload.png").exact().targetOffset(-157,-1))  #gensettings_uncheck_autodownload.png
    
    gda_utils.CLICK(REGION,Pattern("gensettings_checked_autolaunchapp.png").exact().targetOffset(-225,-2))  #gensettings_checked_autolaunchapp.png
    gda_utils.CLICK(REGION,Pattern("gensettings_uncheck_autolaunchapp.png").exact().targetOffset(-232,-2))  #gensettings_uncheck_autolaunchapp.png
    
    gda_utils.CLICK(REGION,Pattern("gensettings_uncheck_autoplay.png").exact().targetOffset(-225,-2))  #gensettings_uncheck_autoplay.png
    gda_utils.CLICK(REGION,Pattern("gensettings_checked_autoplay.png").exact().targetOffset(-224,-4))  #gensettings_checked_autoplay.png
    
    gda_utils.CLICK(REGION,Pattern("gensettings_checked_autosync.png").exact().targetOffset(-202,-1))  #gensettings_checked_autosync.png
    gda_utils.CLICK(REGION,Pattern("gensettings_uncheck_autosync.png").exact().targetOffset(-209,-2))  #gensettings_uncheck_autosync.png
    
    if gda_utils.d_gda_settings["isWindows"]=="True":
        gda_utils.CLICK(REGION,Pattern("media-settings_btn_selectfolder.png").exact()) #media-settings_btn_selectfolder.png
        wait(3)
        gda_utils.CLICK(REGION,Pattern("popup_btn_selectfolder-select-cancel.png").exact().targetOffset(57,-2)) #popup_btn_selectfolder-select-cancel.png
        gda_utils.WAIT(REGION,Pattern("media-settings_txt_settings.png").exact(),20) #media-settings_txt_settings.png    
        gda_utils.CLICK(REGION,Pattern("media-settings_btn_addnew.png").exact()) #media-settings_btn_selectfolder.png
        wait(3)    
        gda_utils.CLICK(REGION,Pattern("popup_btn_selectfolder-select-cancel.png").exact().targetOffset(57,-2)) #popup_btn_selectfolder-select-cancel.png
        
    gda_utils.WAIT(REGION,Pattern("media-settings_txt_settings.png").exact(),20) #media-settings_txt_settings.png

    #CLICK(REGION, Pattern("media-settings_btn_camsettings-disable.png").exact())  #media-settings_btn_camsettings-disable.png
    #FIND(REGION,Pattern("media-settings_btn_camsettings-enable.png").exact())  #media-settings_btn_camsettings-enable.png
    gda_utils.FIND(REGION,Pattern("media-settings_btn_generalsettings-disable.png").exact())  #media-settings_btn_generalsettings-disable.png
    gda_utils.CLICK(REGION,Pattern("media-settings_btn_cloudsettings-disable.png").exact())  #media-settings_btn_cloudsettings-disable.png
    gda_utils.FIND(REGION,Pattern("media-settings_btn_cloudsettings-enable.png").exact())  #media-settings_btn_cloudsettings-enable.png
    gda_utils.CLICK(REGION,Pattern("media-settings_btn_generalsettings-disable.png").exact())  #media-settings_btn_generalsettings-disable.png
    gda_utils.CLICK(REGION, Pattern("media-settings_btn_backtomedia.png").exact())  #media-settings_btn_backtomedia.png
    gda_utils.WAIT(REGION, Pattern("media_selected_media.png").exact(),10)  #media_selected_media.png


def test_getGDAVersion(REGION):
    
    gda_utils.FIND(REGION, Pattern("popup_txt_version200.png").exact()) #popup_txt_version200
    
    gda_utils.FIND(REGION, Pattern("popup_txt_versiongdainfo.png").exact()) #popup_txt_versiongdainfo
    m=gda_utils.FIND(REGION, Pattern("popup_txt_version_ocr.png").exact()) #popup_txt_version_ocr
    if m:
        print m.text()
    
def startup(region):
   
    #######################################
    ###  firststartup    
    #
    gda_utils.WAIT(region,Pattern("startup_txt_title.png").exact(),10)

    gda_utils.FIND(region,Pattern("startup_img_logo.png").similar(0.91))

    gda_utils.CLICK(region,Pattern("startup_checked_autolaunchcam.png").similar(0.91).targetOffset(-190,0))

    gda_utils.CLICK(region,Pattern("startup_unchecked_autolaunchcam.png").similar(0.91).targetOffset(-190,0))

    gda_utils.FIND(region,Pattern("startup_img_camhappy.png").similar(0.91)) #startup_img_camhappy.png

    gda_utils.FIND(region,Pattern("startup_img_findmoments.png").similar(0.92)) #startup_img_findmoments.png

    gda_utils.FIND(region,Pattern("startup_img_importmedia.png").similar(0.91)) #startup_img_importmedia.png

    gda_utils.CLICK(region,Pattern("startup_btn_continue.png").similar(0.90)) #startup_btn_continue.png

    #CLICK(region,Pattern("startup_autoLaunchCamOnGP.png").similar(0.90))

    #CLICK(region,Pattern("startup_unslectedAutoLaunchGP.png").similar(0.91))


    #CLICK(region,Pattern("startup_continue.png").similar(0.90))


def startup_newAcct(region):
    gda_utils.WAIT(region,Pattern("startupCreateAcct_title.png").similar(0.91))
    
    gda_utils.FIND(region,Pattern("startupCreateAcct_form1.png").similar(0.90))

    gda_utils.FIND(region,Pattern("startupCreateAcct_form2.png").similar(0.91))
    
    gda_utils.FIND(region,Pattern("startupCreateAcct_form3.png").similar(0.90))

    gda_utils.CLICK(region,Pattern("startupCreateAcct.png").similar(0.90))


##########################################
#
##########################################
def signout(region):

    try:     
        gda_utils.CLICK(region,Pattern("signout_tool.png").similar(0.90).targetOffset(14,2))
        gda_utils.CLICK(region,Pattern("signout_signout.png").similar(0.90).targetOffset(-24,-8))
    except:
        print "Sign Out not found"
        

     

##########################################
#
##########################################
def signin_validate(region):
    try:
        gda_utils.WAIT(region,Pattern("signin_logo.png").similar(0.90),10)
    except:
        print "sign in not found"
        signout(region)

    gda_utils.WAIT(region,Pattern("signin_logo.png").similar(0.90),30)
    
    gda_utils.FIND(region,Pattern("signin_form.png").similar(0.90))
    
    gda_utils.FIND(region,Pattern("signin_email.png").similar(0.90).targetOffset(-169,29))
    
    gda_utils.FIND(region,Pattern("signin_pw.png").similar(0.90).targetOffset(-199,-39))
    
    gda_utils.FIND(region,Pattern("signin_needAccountJoinNow.png").similar(0.90).targetOffset(63,2))
    
    gda_utils.FIND(region,Pattern("signin_forgotpw.png").similar(0.90).targetOffset(1,19))
    
    gda_utils.FIND(region,Pattern("signin_resendConfirmation.png").similar(0.90).targetOffset(-3,14))

    gda_utils.FIND(region,Pattern("signin_signin.png").similar(0.90))

    
##########################################
#
##########################################
def signin_Login(region,login,pw):

    gda_utils.TYPE(region,Pattern("signin_email.png").similar(0.90).targetOffset(-169,29),login)

    gda_utils.TYPE(region,Pattern("signin_pw.png").similar(0.90).targetOffset(-199,-39),pw)
    
    gda_utils.CLICK(region,Pattern("signin_signin.png").similar(0.90))
    
    gda_utils.WAIT(region,Pattern("getstarted_getstartedWithGP.png").similar(0.90),15)

      

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
def addmedia_validate(region):
    gda_utils.CLICK(region,Pattern("getstarted_choosefolder.png").similar(0.90).targetOffset(0,96))
    
    gda_utils.WAIT(region,Pattern("dialogFindGPMedia_Title.png").similar(0.90),10)
      
    gda_utils.FIND(region,Pattern("dialogFindGPMedia_ChooseFolders.png").similar(0.90))
      
    gda_utils.CLICK(region,Pattern("dialogFindGPMedia_Addfolder.png").similar(0.90).targetOffset(-6,-19))
    
    #assume the dialog pops up over the GoPro region
    #WAIT(region,Pattern("osxdialog_filedialog.png").similar(0.90).targetOffset(40,2))
    #wait(1)    
    #region.waitVanish(Pattern("osxdialog_filedialog.png").similar(0.90).targetOffset(40,2),5)
    type(Key.ENTER)

    wait(1)

    gda_utils.CLICK(region,Pattern("dialogFindGPMedia_Addfolder.png").similar(0.90).targetOffset(0,37))
    

    gda_utils.CLICK(region,Pattern("GPSettings_seconditem.png").similar(0.90).targetOffset(43,17))
    
    gda_utils.CLICK(region,Pattern("dialogYsure_Remove.png").similar(0.90))
    

    gda_utils.CLICK(region,Pattern("GPSettings_BackToMedia.png").similar(0.90).targetOffset(-29,-30))
    
    # region.click(Pattern("dialogFindGPMedia_Cancel.png").similar(0.90).targetOffset(-15,7))


def startup(region):
   
    #######################################
    ###  firststartup    
    #
    gda_utils.WAIT(region,Pattern("startup_txt_title.png").exact(),10)

    gda_utils.FIND(region,Pattern("startup_img_logo.png").similar(0.91))

    gda_utils.CLICK(region,Pattern("startup_checked_autolaunchcam-1.png").similar(0.91).targetOffset(-190,0))

    gda_utils.CLICK(region,Pattern("startup_unchecked_autolaunchcam-1.png").similar(0.91).targetOffset(-190,0))

    gda_utils.FIND(region,Pattern("startup_img_camhappy-1.png").similar(0.91)) #startup_img_camhappy.png

    gda_utils.FIND(region,Pattern("startup_img_findmoments-1.png").similar(0.92)) #startup_img_findmoments.png

    gda_utils.FIND(region,Pattern("startup_img_importmedia-1.png").similar(0.91)) #startup_img_importmedia.png

    gda_utils.CLICK(region,Pattern("startup_btn_continue-1.png").similar(0.90)) #startup_btn_continue.png

    #CLICK(region,Pattern("startup_autoLaunchCamOnGP.png").similar(0.90))

    #CLICK(region,Pattern("startup_unslectedAutoLaunchGP.png").similar(0.91))


    #CLICK(region,Pattern("startup_continue.png").similar(0.90))



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
def signout(region):

    try:     
        gda_utils.CLICK(region,Pattern("signout_tool.png").similar(0.90).targetOffset(14,2))
        gda_utils.CLICK(region,Pattern("signout_signout.png").similar(0.90).targetOffset(-24,-8))
    except:
        print "Sign Out not found"
        

##########################################
#
##########################################
def imagerepo():
    #sorted png name order below   
    find("camsettings_btn_h4blacksettings.png")  #camsettings_btn_h4blacksettings.png
    find("camsettings_btn_h4sessionsettings.png")  #camsettings_btn_h4sessionsettings.png
    find("camsettings_btn_h4silversettings.png")  #camsettings_btn_h4silversettings.png
    find("camsettings_img_h4black.png")  #camsettings_img_h4black.png
    find("camsettings_img_h4session.png")  #camsettings_img_h4session.png
    find("camsettings_img_h4silver.png")  #camsettings_img_h4silver.png
    find("camsettings_txt_title.png")  #camsettings_txt_title.png
    find("conncam_btn_getsupport.png")  #conncam_btn_getsupport.png
    find("conncam_btn_gotit.png")  #conncam_btn_gotit.png
    find("conncam_txt_camon.png")  #conncam_txt_camon.png
    find("conncam_txt_plugcam.png")  #conncam_txt_plugcam.png
    find("conncam_txt_selectimport.png")  #conncam_txt_selectimport.png
    find("conncam_txt_title.png")  #conncam_txt_title.png
    find("createacct_btn_getacct.png")  #createacct_btn_getacct.png
    find("createacct_btn_signin.png")  #createacct_btn_signin.png
    find("createacct_checked_getnews.png")  #createacct_checked_getnews.png
    find("createacct_checked_iacknowledge.png")  #createacct_checked_iacknowledge.png
    find("createacct_txt_invalidemail.png")  #createacct_txt_invalidemail.png
    find("createacct_txt_subtitle.png")  #createacct_txt_subtitle.png
    find("createacct_txt_title.png")  #createacct_txt_title.png
    find("createacct_txtbox_email.png")  #createacct_txtbox_email.png
    find("createacct_txtbox_password.png")  #createacct_txtbox_password.png
    find("createacct_unchecked_getnews.png")  #createacct_unchecked_getnews.png
    find("createacct_unchecked_iacknowledge.png")  #createacct_unchecked_iacknowledge.png
    find("edits_btn_createedit.png")  #edits_btn_createedit.png
    find("edits_img_edits.png")  #edits_img_edits.png
    find("edits_txt_info.png")  #edits_txt_info.png
    find("edits_txt_noedits.png")  #edits_txt_noedits.png
    find("findmedia_btn_addfolder.png")  #findmedia_btn_addfolder.png
    find("findmedia_btn_cancel.png")  #findmedia_btn_cancel.png
    find("findmedia_btn_close.png")  #findmedia_btn_close.png
    find("findmedia_btn_managefoldersettings.png")  #findmedia_btn_managefoldersettings.png
    find("findmedia_btn_save.png")  #findmedia_btn_save.png
    find("findmedia_txt_subtitle.png")  #findmedia_txt_subtitle.png
    find("findmedia_txt_title.png")  #findmedia_txt_title.png
    find("gensettings_btn_addnew.png")  #gensettings_btn_addnew.png
    find("gensettings_btn_importlocation.png")  #gensettings_btn_importlocation.png
    find("gensettings_btn_mediafoldersscan.png")  #gensettings_btn_mediafoldersscan.png
    find("gensettings_checked_autodownload.png")  #gensettings_checked_autodownload.png
    find("gensettings_checked_autolaunchapp.png")  #gensettings_checked_autolaunchapp.png
    find("gensettings_checked_autoplay.png")  #gensettings_checked_autoplay.png
    find("gensettings_checked_autosync.png")  #gensettings_checked_autosync.png
    find("gensettings_txt_importlocation.png")  #gensettings_txt_importlocation.png
    find("gensettings_txt_mediafolders.png")  #gensettings_txt_mediafolders.png
    find("gensettings_txt_title.png")  #gensettings_txt_title.png
    find("gensettings_uncheck_autodownload.png")  #gensettings_uncheck_autodownload.png
    find("gensettings_uncheck_autolaunchapp.png")  #gensettings_uncheck_autolaunchapp.png
    find("gensettings_uncheck_autoplay.png")  #gensettings_uncheck_autoplay.png
    find("gensettings_uncheck_autosync.png")  #gensettings_uncheck_autosync.png
    find("media_btn_choosefolder.png")  #media_btn_choosefolder.png
    find("media_btn_connectcam.png")  #media_btn_connectcam.png
    find("media_btn_settings.png")  #media_btn_settings.png
    find("media_img_addmedia.png")  #media_img_addmedia.png
    find("media_img_alerts.png")  #media_img_alerts.png
    find("media_selected_edits.png")  #media_selected_edits.png
    find("media_selected_hero4black.png")  #media_selected_hero4black.png
    find("media_selected_hero4session.png")  #media_selected_hero4session.png
    find("media_selected_hero4silver.png")  #media_selected_hero4silver.png
    find("media_selected_media.png")  #media_selected_media.png
    find("media_selected_recentlyadd.png")  #media_selected_recentlyadd.png
    find("media_txt_autogdasignin.png")  #media_txt_autogdasignin.png
    find("media_txt_media-editor.png")  #media_txt_media-editor.png
    find("media_txt_title.png")  #media_txt_title.png
    find("media_unselected_edits.png")  #media_unselected_edits.png
    find("media_unselected_hero4black.png")  #media_unselected_hero4black.png
    find("media_unselected_hero4session.png")  #media_unselected_hero4session.png
    find("media_unselected_hero4silver.png")  #media_unselected_hero4silver.png
    find("media_unselected_media.png")  #media_unselected_media.png
    find("media_unselected_recentlyadd.png")  #media_unselected_recentlyadd.png
    find("media-settings_btn_addnew.png")  #media-settings_btn_addnew.png
    find("media-settings_btn_backtomedia.png")  #media-settings_btn_backtomedia.png
    find("media-settings_btn_camsettings-disable.png")  #media-settings_btn_camsettings-disable.png
    find("media-settings_btn_camsettings-enable.png")  #media-settings_btn_camsettings-enable.png
    find("media-settings_btn_cloudsettings-disable.png")  #media-settings_btn_cloudsettings-disable.png
    find("media-settings_btn_cloudsettings-enable.png")  #media-settings_btn_cloudsettings-enable.png
    find("media-settings_btn_generalsettings-disable.png")  #media-settings_btn_generalsettings-disable.png
    find("media-settings_btn_onlinesupport.png")  #media-settings_btn_onlinesupport.png
    find("media-settings_btn_sendfeedback.png")  #media-settings_btn_sendfeedback.png
    find("media-settings_checked_autoplay.png")  #media-settings_checked_autoplay.png
    find("media-settings_checked_autosynch.png")  #media-settings_checked_autosynch.png
    find("media-settings_img_scanning.png")  #media-settings_img_scanning.png
    find("media-settings_img_scan.png")  #media-settings_img_scan.png
    find("media-settings_btn_selectfolder.png") #media-settings_btn_selectfolder.png
    find("media-settings_txt_importlocation.png")  #media-settings_txt_importlocation.png
    find("media-settings_txt_mediafolders.png")  #media-settings_txt_mediafolders.png
    find("media-settings_txt_settings.png")  #media-settings_txt_settings.png
    find("media-settings_unchecked_autoplay.png")  #media-settings_unchecked_autoplay.png
    find("media-settings_unchecked_autosynch.png")  #media-settings_unchecked_autosynch.png
    find("mediacam_btn_importfiles.png")  #mediacam_btn_importfiles.png
    find("mediacam_txt_spaceused.png")  #mediacam_txt_spaceused.png
    find("mediacamsettings_btn_cancel.png")  #mediacamsettings_btn_cancel.png
    find("mediacamsettings_btn_close.png")  #mediacamsettings_btn_close.png
    find("mediacamsettings_btn_save.png")  #mediacamsettings_btn_save.png
    find("mediacamsettings_checked_autodelete.png")  #mediacamsettings_checked_autodelete.png
    find("mediacamsettings_checked_autoimport.png")  #mediacamsettings_checked_autoimport.png
    find("mediacamsettings_unchecked_autodelete.png")  #mediacamsettings_unchecked_autodelete.png
    find("mediacamsettings_unchecked_autoimport.png")  #mediacamsettings_unchecked_autoimport.png
    find("mediah4black_img_logo.png")  #mediah4black_img_logo.png
    find("mediah4black_txt_available.png")  #mediah4black_txt_available.png
    find("mediah4black_txt_capacity.png")  #mediah4black_txt_capacity.png
    find("mediah4black_txt_subtitle.png")  #mediah4black_txt_subtitle.png
    find("mediah4black_txt_title.png")  #mediah4black_txt_title.png
    find("mediah4black_txt_used.png")  #mediah4black_txt_used.png
    find("mediah4session_img_logo.png")  #mediah4session_img_logo.png
    find("mediah4session_txt_available.png")  #mediah4session_txt_available.png
    find("mediah4session_txt_capacity.png")  #mediah4session_txt_capacity.png
    find("mediah4session_txt_subtitle.png")  #mediah4session_txt_subtitle.png
    find("mediah4session_txt_title.png")  #mediah4session_txt_title.png
    find("mediah4session_txt_used.png")  #mediah4session_txt_used.png
    find("mediah4silver_img_logo.png")  #mediah4silver_img_logo.png
    find("mediah4silver_txt_available.png")  #mediah4silver_txt_available.png
    find("mediah4silver_txt_capacity.png")  #mediah4silver_txt_capacity.png
    find("mediah4silver_txt_subtitle.png")  #mediah4silver_txt_subtitle.png
    find("mediah4silver_txt_title.png")  #mediah4silver_txt_title.png
    find("mediah4silver_txt_used.png")  #mediah4silver_txt_used.png
    find("mediasettingsh4black_txt_cammodel.png")  #mediasettingsh4black_txt_cammodel.png
    find("mediasettingsh4black_txtbox_camfolder.png")  #mediasettingsh4black_txtbox_camfolder.png
    find("mediasettingsh4session_txt_cammodel.png")  #mediasettingsh4session_txt_cammodel.png
    find("mediasettingsh4session_txtbox_camfolder.png")  #mediasettingsh4session_txtbox_camfolder.png
    find("mediasettingsh4silver_txt_cammodel.png")  #mediasettingsh4silver_txt_cammodel.png
    find("mediasettingsh4silver_txtbox_camfolder.png")  #mediasettingsh4silver_txtbox_camfolder.png
    find("popup_btn_choosevideos-OK.png")  #popup_btn_choosevideos-OK.png
    find("popup_btn_indexinfo.png")  #popup_btn_indexinfo.png
    find("popup_txt_pleasechoosevideos.png")  #popup_txt_pleasechoosevideos.png
    find("popup_txt_theeditorcanonlyopenvideos.png")  #popup_txt_theeditorcanonlyopenvideos.png
    find("popup_txt_version_ocr.png")  #popup_txt_version_ocr.png
    find("popup_txt_version200.png")  #popup_txt_version200.png
    find("popup_txt_versiongdainfo.png")  #popup_txt_versiongdainfo.png
    find("recentlyadd_btn_addmedia.png")  #recentlyadd_btn_addmedia.png
    find("recentlyadd_btn_connectcam.png")  #recentlyadd_btn_connectcam.png
    find("recentlyadd_txt_title.png")  #recentlyadd_txt_title.png
    find("settings_btn_backtomedia.png")  #settings_btn_backtomedia.png
    find("settings_selected_camsettings.png")  #settings_selected_camsettings.png
    find("settings_selected_gensettings.png")  #settings_selected_gensettings.png
    find("settings_unselected_camsettings.png")  #settings_unselected_camsettings.png
    find("settings_unselected_gensettings.png")  #settings_unselected_gensettings.png
    find("signin_btn_forgot.png")  #signin_btn_forgot.png
    find("signin_btn_needacct.png")  #signin_btn_needacct.png
    find("signin_btn_resendemail.png")  #signin_btn_resendemail.png
    find("signin_btn_signin.png")  #signin_btn_signin.png
    find("signin_img_logo.png")  #signin_img_logo.png
    find("signin_txt_invalidemail.png")  #signin_txt_invalidemail.png
    find("signin_txt_title.png")  #signin_txt_title.png
    find("signin_txtbox_emailpw_blankpw.png")  #signin_txtbox_emailpw_blankpw.png
    find("signin_txtbox_emailpw.png")  #signin_txtbox_emailpw.png
    find("startup_btn_continue.png")  #startup_btn_continue.png
    find("startup_checked_autolaunchcam.png")  #startup_checked_autolaunchcam.png
    find("startup_img_camhappy.png")  #startup_img_camhappy.png
    find("startup_img_findmoments.png")  #startup_img_findmoments.png
    find("startup_img_importmedia.png")  #startup_img_importmedia.png
    find("startup_img_logo.png")  #startup_img_logo.png
    find("startup_txt_title.png")  #startup_txt_title.png
    find("startup_unchecked_autolaunchcam.png")  #startup_unchecked_autolaunchcam.png
    find("user_btn_select.png")  #user_btn_select.png
    find("user_btn_signoff.png")  #user_btn_signoff.png
    find("popup_btn_selectfolder-select-cancel.png") #popup_btn_selectfolder-select-cancel.png

    find("media-settings-cam_img_camera.png")  #media-settings-cam_img_camera.png

    find("media-settings-cam_txt_pleaseconnectyourgopro.png") #media-settings-cam_txt_pleaseconnectyourgopro.png
    find("media-settings-cam_txt_settings-title.png") #media-settings-cam_txt_settings-title.png
    
    find("media-settings-cam_txt_plugcamintocomputer.png")  #media-settings-cam_txt_plugcamintocomputer.png

    find("media-settings-cloud_txt_goproupsell.png") #media-settings-cloud_txt_goproupsell.png
    
    find("media-popup_txt_letsfindgopromedia.png")  #media-popup_txt_letsfindgopromedia.png

    find("media-popup_txt_choosefolderstoadd.png") #media-popup_txt_choosefolderstoadd.png
    
    find("media-popup_btn_addfolder.png")  #media-popup_btn_addfolder

    find("media-popup_btn_managefoldersinsettings.png")  #media-popup_btn_managefoldersinsettings.png

    find("media-popup_btn_save.png") #media-popup_btn_save.png

    find("media-popup_btn_cancel.png")  #media-popup_btn_cancel.png
    
    find("media-popup_txt_connectyourcamera.png")  #media-popup_txt_connectyourcamera.png
    
    find("media-popup_txt_cameraconnectsteps.png")  #media-popup_txt_cameraconnectsteps.png

    find("media-popup_btn_gotit.png")  #media-popup_btn_gotit

    find("media-popup_btn_getsupport.png")  #media-popup_btn_getsupport.png
    
    find("media-edits_img_noeditsyet.png")  #media-edits_img_noeditsyet.png
    
    find("media-edits_btn_createanedit.png")  #media-edits_btn_createanedit.png

    find("media-edits_txt_seeallyoursharableedits.png")  #media-edits_txt_seeallyoursharableedits.png
    
##########################################


##########################################
def BAT(gpa, gpr):
    #global startupcnt
    #global d_similarity
    
    gpr=refreshregion(gpa)
    startup(gpr)
    if not putDictToFile(gda_utils.d_similarity):
        exit(1)

    gpr=refreshregion(gpa)
    create_your_acct(gpr) #fail
    if not putDictToFile(gda_utils.d_similarity):
        exit(1)
    
    gpr=refreshregion(gpa)
    signin_test(gpr) #fail
    if not putDictToFile(gda_utils.d_similarity):
        exit(1)
    
    gpr=refreshregion(gpa)
    signin_test(gpr,False,"autogda00@gmail.com","access4auto") #prod login, staging = "autogda00@gmail.com","Access4auto"
    if not putDictToFile(gda_utils.d_similarity):
        exit(1)

    gpr=refreshregion(gpa)
    media_getstarted_gopro(gpr) #media screen
    putDictToFile(gda_utils.d_similarity)


    gpr=refreshregion(gpa)
    media_settings(gpr) #media settings
    putDictToFile(gda_utils.d_similarity)


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
    