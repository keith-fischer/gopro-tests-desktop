##########################################
#IMPORT Start  ---->
##########################################
import os
import sys
#Set the current test path
CurrentTestCase = "GDA_OSX"

# get the directory containing your running .sikuli
zRootProjectDir = os.path.dirname(getBundlePath())

print "RootProjectDir:",zRootProjectDir
if not zRootProjectDir in sys.path:
    sys.path.append(zRootProjectDir)

#Set the framework path
LibPath = zRootProjectDir + "/HelperLib.sikuli"

print "LibPath:",LibPath
if not LibPath in sys.path:
    sys.path.append(LibPath)

ThisTestCase = zRootProjectDir+ "/" + CurrentTestCase+".sikuli"

print "ThisTestCase:",ThisTestCase
if not ThisTestCase in sys.path:
    sys.path.append(ThisTestCase)

# all systems
print "SYS=",sys.path
# now you can import every .sikuli in the same directory
#from Lib import *

import HelperLib
reload(HelperLib)
HelperLib.Log(CurrentTestCase +" Startup")
##########################################
#IMPORT End
##########################################


##########################################
#START Test Suite Script Functions  ---->
##########################################

##########################################
#SetVideoResolution
##########################################
def SetVideoResolution(Res):
    global Pattern_Similar_Value
    global debug
    global printReport
    global vncregion
    try:

        HelperLib.Log("SetVideoResolution_" + Res)
        #click the video setting

        #Cam setting top icon and camera title settings header
        #VerifyLabelSetting="CamSettings_Label_Camera.png"
        #VerifyLabelSettingP = HelperLib.PATTERN(VerifyLabelSetting)
        #HelperLib.debugPrint(VerifyLabelSetting)
        #Camera Settings Title
        #printReport = False
        #FindCamSetting("CamSettings_Title",vncregion,VerifyLabelSettingP)  

        #HelperLib.debugPrint("CamSettings_Title"+VerifyLabelSetting)
        Pattern_Similar_Value=0.90
        #Video Res label

        selectVideoResolution="CamSettings_Button_VideoResolution.png"
        selectVideoResolutionP =HelperLib.PATTERN(selectVideoResolution)
        #Video Resolution Settings Label
        foundImg = FindCamSetting("CamSettings_Button_VideoResolution",vncregion,selectVideoResolutionP)

        if foundImg:
            HelperLib.Log("SetVideoResolution FOUND:"+selectVideoResolution)
            wait(2)
            if HelperLib.CLICK(vncregion,selectVideoResolutionP) == True:
                HelperLib.Log("SetVideoResolution CLICKED: "+selectVideoResolution)
                #wait(2)

                #video  res dialog title
                VidResTitle = "CamSettings_SetVideoRes_Title.png"
                #VidResTitleP = HelperLib.PATTERN(VidResTitle)
                HelperLib.Log("SetVideoResolution: "+VidResTitle)
                #foundImg = HelperLib.WAIT(vncregion,VidResTitle)
                foundImg = AutoThresholdWait(vncregion,VidResTitle)
                if foundImg:
                    HelperLib.Log("SetVideoResolution FOUND: "+VidResTitle)

                    #Res dialog value to select
                    setVidRes = "CamSettings_SetVideoRes_" + Res  +".png"
                    setVidResP = HelperLib.PATTERN(setVidRes)
                    HelperLib.Log("SetVideoResolution FindCamSetting:"+setVidRes)
                    if Res == "4K-17-9":
                        HelperLib.SwipeDown(vncregion)
                        wait(2)
                    elif Res == "WVGA":
                        HelperLib.SwipeUp(vncregion)
                        wait(2)
                    foundImg = FindCamSetting("SetVideoResolution-"+Res,vncregion,setVidResP)
                    if foundImg:
                        HelperLib.Log("SetVideoResolution FOUND:"+setVidRes)
                        wait(2)
                        if HelperLib.CLICK(vncregion,setVidRes) == True:
                            HelperLib.Log("SetVideoResolution Clicked:"+setVidRes)

                            #foundImg.hightlight(1)
                            wait(3)

                            #Verify Video Res label and value
                            verifyVidRes = "CamSettings_Selected_VideoResolution_" + Res + ".png"
                            #verifyVidResP = HelperLib.PATTERN(verifyVidRes)
                            #HelperLib.debugPrint("foundImg")

                            foundImg = HelperLib.WAIT(vncregion,verifyVidRes)
                            if foundImg:
                                HelperLib.Log("SetVideoResolution FOUND:"+verifyVidRes)
                                #foundImg.hightlight(1)
                                return True
                            else:
                                HelperLib.Log("SetVideoResolution FAILED:"+verifyVidRes)
                                vncregion.hightlight(1)
                                return False

                        else:
                            HelperLib.Log("SetVideoResolution FAILED CLICK:"+setVidRes)
                            vncregion.hightlight(1)
                            HelperLib.CLICK(vncregion,"Android_Menu_Back.png")
                            return False
                    else:
                        vncregion.hightlight(1)
                        HelperLib.Log("SetVideoResolution NOT FOUND:"+setVidRes)
                        if HelperLib.CLICK(vncregion,"Android_Menu_Back.png") == True:
                            return False
                        else:
                            HelperLib.CLICK(vncregion,"Android_Menu_Back.png")
                            return False
                else:
                    HelperLib.Log("SetVideoResolution NOT FOUND::"+VidResTitle)
                    vncregion.hightlight(1)
                    HelperLib.CLICK(vncregion,"Android_Menu_Back.png")
                    vncregion.hightlight(1)
                    return False
            else:
                vncregion.hightlight(1)
                HelperLib.Log("SetVideoResolution NOT CLICKED:"+selectVideoResolution)
                return False
        else:
            vncregion.hightlight(1)
            HelperLib.Log("SetVideoResolution NOT FOUND:"+selectVideoResolution)
            return False
    except Exception, err:
        HelperLib.Log("SetVideoResolution ===>ERROR: " +str(err))
        HelperLib.Log("===>SetVideoResolution ERROR:"+"SetVideoResolution_" + Res)
        vncregion.hightlight(1)
        HelperLib.CLICK(vncregion,"Android_Menu_Back.png")
        return False


    ##########################################
    #SetVideoResolution
    ##########################################
    #def SetVideoResolutionOLD(Res):
    #    global Pattern_Similar_Value
    #    HelperLib.Log("SetVideoResolution_" + Res)

    #    #click the video setting
    #    Pattern_Similar_Value=0.90
    #    setVidRes=HelperLib.PATTERN("CamSettings_Button_VideoResolution.png")
    #    FindCamSetting("CamSettings_Button_VideoResolution",vncregion,setVidRes)

    #    #Pattern_Similar_Value=0.95

    #    #wait for dialog title
    #    VidResTitleP=HelperLib.PATTERN("CamSettings_SetVideoRes_Title.png")
    #    vncregion.wait(VidResTitleP)

    #    setVidRes = "CamSettings_SetVideoRes_" + Res  +".png"
    #    setVidResP =HelperLib.PATTERN(setVidRes)
    #    FindCamSetting("CamSettings_Button_VideoResolution",vncregion,setVidResP)

    #    setVidCancel = HelperLib.PATTERN( "CamSettings_SetVideoRes_Cancel.png")
    #    setVidCancelP =HelperLib.PATTERN(setVidCancel)
    #    try:
    #        vncregion.click(setVidResP)
    #    except:
    #        vncregion.click(setVidCancelP)
    #    FindCamSetting("CamSettings_Button_VideoResolution",vncregion,setVidRes)

    #    #Verify
    #    verifyVidRes="CamSettings_Selected_VideoResolution_" + Res + ".png"
    #    verifyVidResP =HelperLib.PATTERN(verifyVidRes)

    #    VerifyLabelSetting="CamSettings_Label_Camera.png"
    #    VerifyLabelSettingP =HelperLib.PATTERN(VerifyLabelSetting)

    ##    FindCamSetting("CamSettings_Title",vncregion,VidResTitleP)
    #    VidResSettingP =HelperLib.PATTERN(verifyVidRes)
    ##    FindCamSetting("CamSettings_Button_VideoResolution",vncregion,setVidRes)
    #    wait(3)




    #    Pattern_Similar_Value=0.95
    #    vncregion.wait(setVidRes)

    #return True


##########################################
#VerifyFPS
##########################################
#def VerifyFPS2(Res):
#    HelperLib.Log("VerifyFPS2" + Res)
#    VerifyFPS2(Res,False,False)


def VerifyFPS(Res):
    global Pattern_Similar_Value
    try:
        Pattern_Similar_Value = 0.90
        HelperLib.Log("VerifyFPS" + Res +" - "+ str(IsProTune) + " - "+str(IsPAL))
        selectFPS = "CamSettings_Button_FrameRate.png"
        setFPSCancel =  "CamSettings_DefaultDialog_Button_FrameRate_Cancel.png"
        protune = ""
        NTSCPAL = ""

        if IsProTune == True:
            protune = "_ProTune"

        #default is NTSC not labeled. PAL is labeled as "PAL" for images
        if IsPAL == True:
            NTSCPAL = "_PAL"

        verifyfpsImg = "CamSettings_DefaultDialog_FrameRate_"+Res+protune+NTSCPAL+".png"
        verifyfpsImgP = HelperLib.PATTERN( verifyfpsImg)


        verifyfpsTitleImg = "CamSettings_SetFPS_Title.png"
        verifyfpsTitleImgP = HelperLib.PATTERN( verifyfpsTitleImg)

        HelperLib.Log("VerifyFPS image file = " + str(verifyfpsImg))

        #click the FPS setting to show FPS select list
        if HelperLib.CLICK(vncregion,selectFPS) == True:
            #Verify FPS Title visible
            foundImg = AutoThresholdWait(vncregion,verifyfpsTitleImg)
            if foundImg:
                #Verify all FPS are visible
                foundImg = HelperLib.WAIT(vncregion,verifyfpsImgP)
                if foundImg:
                    HelperLib.Log("VerifyFPS image file = " + str(setFPSCancel))
                    if HelperLib.CLICK(vncregion,setFPSCancel) == True:
                        return True
                    else:
                        HelperLib.CLICK(vncregion,"Android_Menu_Back.png")
                        return False
                else:
                    HelperLib.CLICK(vncregion,"Android_Menu_Back.png")
                    return False
            else:
                HelperLib.CLICK(vncregion,"Android_Menu_Back.png")
                return False
        else:
            return False
    except Exception, err:
        HelperLib.Log("===>ERROR: " +str(err))
        HelperLib.CLICK(vncregion,"Android_Menu_Back.png")
        return False


##########################################
#AutoThresholdWait
##########################################
def AutoThresholdWait(imgRegion,imageName):
    global Pattern_Similar_Value
    HelperLib.Log("AutoThresholdWait: " + imageName)
    Pattern_Similar_Value = 0.99
    imageP = HelperLib.PATTERN( imageName)
    foundImg = HelperLib.WAIT(imgRegion,imageP)
    while not foundImg:
        if Pattern_Similar_Value < 0.60:
            break
        HelperLib.Log("AutoThresholdWait: " + str(Pattern_Similar_Value))
        Pattern_Similar_Value = Pattern_Similar_Value -0.5
        imageP = HelperLib.PATTERN( imageName)
        foundImg = HelperLib.WAIT(imgRegion,imageP)

    HelperLib.Log("AutoThresholdWait: EXIT" + str(Pattern_Similar_Value))
    Pattern_Similar_Value = 0.90
    if foundImg:
        HelperLib.Log("AutoThresholdWait: FOUND" + str(foundImg))
        return foundImg
    else:
        return

##########################################
#SetFPS
##########################################
def SetFPS(Res,FPS):
    global Pattern_Similar_Value
    try:
        Pattern_Similar_Value = 0.90
        HelperLib.Log("SetFPS" + FPS +" - "+ str(IsProTune) + " - "+str(IsPAL))

        selectFPS = HelperLib.PATTERN( "CamSettings_Button_FrameRate.png")
        setFPSCancel = HelperLib.PATTERN( "CamSettings_DefaultDialog_Button_FrameRate_Cancel.png")

        protune = ""
        NTSCPAL = ""

        if IsProTune == True:
            protune = "_ProTune"

        #default is NTSC not labeled. PAL is labeled as "PAL" for images
        if IsPAL == True:
            NTSCPAL = "_PAL"

        verifyfpsImg = "CamSettings_DefaultDialog_FrameRate_"+Res+protune+NTSCPAL+".png"
        #verifyfpsImgP = HelperLib.PATTERN( verifyfpsImg) 

        verifyIsfpsImg = "CamSettings_Selected_FrameRate_"+FPS+"FPS.png"
        #verifyIsfpsImgP = HelperLib.PATTERN( verifyIsfpsImg) 

        Pattern_Similar_Value = 0.80
        clickfpsImg = "CamSettings_SetFPS_"+FPS+".png"
        #clickfpsImgP = HelperLib.PATTERN( clickfpsImg) 
        Pattern_Similar_Value = 0.90

        HelperLib.Log("SetFPS image file = " + str(verifyfpsImg))

        #click the FPS setting to show FPS select list
        IsFound = HelperLib.CLICK(vncregion,selectFPS)

        if IsFound == True:
            #Verify all FPS are visible
            foundImg = HelperLib.WAIT(vncregion,verifyfpsImg)
            if foundImg:
                #click FPS
                foundImg = AutoThresholdWait(vncregion,clickfpsImg)
                if foundImg:
                    foundImg.click()
                    wait(3)
                    #Verify FPS is set
                    foundImg = HelperLib.WAIT(vncregion,verifyIsfpsImg)
                    if foundImg:
                        return True
                    else:
                        HelperLib.Log("SetFPS Failed:  image file = " + verifyIsfpsImg)
                        return False
                else:
                    HelperLib.Log("SetFPS Failed:  image file = " + clickfpsImg)
                    if HelperLib.CLICK(vncregion,setFPSCancel) == True:
                        return False
                    else:
                        HelperLib.CLICK(vncregion,"Android_Menu_Back.png")
                        return False
            else:
                HelperLib.Log("SetFPS Failed:  image file = " + verifyfpsImg)
                if HelperLib.CLICK(vncregion,setFPSCancel) == True:
                    return False
                else:
                    HelperLib.CLICK(vncregion,"Android_Menu_Back.png")
                    return False
        else:
            return False
    except Exception, err:
        HelperLib.Log("SetFPS Error:" + str(err))
        #Try to back out of fps dialog
        HelperLib.CLICK(vncregion,"Android_Menu_Back.png")
        return False


##########################################
#SetCameraSettingOnOff
##########################################
def SetCamSettingOnOff(SettingName, vncregion, SettingLabel, TargetSetting, CurrentSetting):
    HelperLib.Log(CurrentTestCase +".SetCamSettingOnOff")
    SettingLabelP = HelperLib.PATTERN(SettingLabel)
    imgFound = FindCamSetting(SettingName,vncregion,SettingLabelP)
    CurrentSettingP = HelperLib.PATTERN(CurrentSetting)
    TargetSettingP = HelperLib.PATTERN(TargetSetting)
    wait(4)
    imgFound = vncregion.exists(SettingLabelP)

    if imgFound:
        #imgFound = vncregion.find(SettingLabel)
        #wait(2)

        imgFound = vncregion.find(SettingLabelP)
        imgFound.highlight(1)
        #wait(4)
        if imgFound.right().exists(CurrentSettingP):
            #wait(2)
            imgButton = imgFound.right().find(CurrentSettingP)
            imgButton.highlight(1)
            #wait(2)
            imgButton.click()
            #wait(3)
            #imgFound = vncregion.wait(SettingLabelP)

            #if imgFound:
            wait(3)
            #imgFound.highlight(1) 
            if imgFound.right().exists(TargetSettingP):
                imgButton = imgFound.right().find(TargetSettingP)
                if imgButton:
                    wait(2)
                    HelperLib.Log(SettingName+" ENABLED"+TargetSetting)
                    HelperLib.Report("PASSED: "+SettingName)

            else:
                HelperLib.Log("****FAILED "+SettingName+ " Switch NOT SET*****"+TargetSetting)
                HelperLib.Report("FAILED: "+SettingName)

                #else:
                #    HelperLib.Log("****FAILED "+SettingName+ " NOT FOUND*****")
                #    HelperLib.Report("FAILED: "+SettingName)

        elif imgFound.right().exists(TargetSettingP):
            wait(2)
            imgFound.right().find(TargetSettingP).highlight(1)
            HelperLib.Log(SettingName+" ENABLED"+TargetSetting)
            HelperLib.Report("PASSED: "+SettingName)

        else:
            HelperLib.Log("****FAILED "+SettingName+ " Switch NOT FOUND*****")
            HelperLib.Report("FAILED: "+SettingName)

    else:
        HelperLib.Log("****FAILED "+SettingName+ " NOT FOUND*****")
        HelperLib.Report("FAILED: "+SettingName)

    return imgFound

##########################################
#FindCamSetting
##########################################
def AssertFindCamSetting(SettingName, vncregion, SettingLabel):
    HelperLib.Log(CurrentTestCase +".AssertFindCamSetting:"+SettingName)
    #imgFound = HelperLib.SwipeFind(vncregion,SettingLabel,6)
    imgFound = FindCamSetting(SettingName, vncregion, SettingLabel)
    if imgFound:
        HelperLib.Report("PASSED: "+SettingName)
    else:
        HelperLib.Report("FAILED: "+SettingName)
    return imgFound

##########################################
#FindCamSetting
##########################################
def FindCamSetting(SettingName, vncregion, SettingLabel):
    HelperLib.Log(CurrentTestCase +".FindCamSetting:"+SettingName)
    imgFound = HelperLib.SwipeFind(vncregion,SettingLabel,6)

    if imgFound:
        HelperLib.Log(CurrentTestCase +".FindCamSetting:FOUND - "+SettingName)
        imgFound.highlight(1)
        HelperLib.Log("FindCameraSetting:"+SettingName+ " FOUND "+str(SettingLabel))
    else:
        HelperLib.Log("****FAILED:"+CurrentTestCase +".FindCamSetting: "+SettingName+ " NOT FOUND "+str(SettingLabel))
    return imgFound

##########################################
### TestProTune
##########################################
def TestProTune():
    HelperLib.Log(CurrentTestCase +".TestProTune")


    AssertFindCamSetting("Protune_WhiteBalance",vncregion,"CamSettings_Label_Adv_WhiteBalance.png")
    AssertFindCamSetting("Protune_Color",vncregion,"CamSettings_Label_Adv_Color.png")
    AssertFindCamSetting("Protune_ISOLimit",vncregion,"CamSettings_Label_Adv_ISOLimit.png")
    AssertFindCamSetting("Protune_Sharpness",vncregion,"CamSettings_Label_Adv_Sharpness.png")
    AssertFindCamSetting("Protune_ExposureComp",vncregion,"CamSettings_Label_Adv_ExposureComp.png")
    AssertFindCamSetting("Protune_ResetDefault",vncregion,"CamSettings_Label_Adv_ResetDefault.png")

#    SetProTuneOFF()

##########################################
### SetProTuneON
##########################################
def SetProTuneON():
    HelperLib.Log(CurrentTestCase +".SetProTuneON")
    imgFound = SetCamSettingOnOff("Advanced:ProTune:ON",vncregion,"CamSettings_Label_Adv_ProTune.png","CamSettings_Button_ON.png","CamSettings_Button_OFF.png")
    if imgFound:
        IsProTune = True
        #HelperLib.Report("PASSED: SetProTuneON")
        #   else:
        #HelperLib.Report("FAILED: SetProTuneON")

##########################################
### SetProTuneOFF
##########################################    
def SetProTuneOFF():
    HelperLib.Log(CurrentTestCase +".SetProTuneOFF")
    imgFound = SetCamSettingOnOff("Advanced:ProTune:OFF",vncregion,"CamSettings_Label_Adv_ProTune.png","CamSettings_Button_OFF.png","CamSettings_Button_ON.png")
    if imgFound:
        IsProTune = False
        #HelperLib.Report("PASSED: SetProTuneOFF")
        #   else:
        #HelperLib.Report("FAILED: SetProTuneOFF")


##########################################
### TestToggleSettings
##########################################
def TestToggleSettings():
    HelperLib.Log(CurrentTestCase +".TestToggleSettings")

    SetCamSettingOnOff("Capture Settings:Upside Down:ON" ,vncregion,"CamSettings_Label_Capture_UpsideDown.png","CamSettings_Button_ON.png", "CamSettings_Button_OFF.png")
    SetCamSettingOnOff("Capture Settings:Upside Down:OFF",vncregion,"CamSettings_Label_Capture_UpsideDown.png","CamSettings_Button_OFF.png","CamSettings_Button_ON.png")

    SetCamSettingOnOff("Capture Settings:Spot Meter:ON",vncregion,"CamSettings_Label_Capture_SpotMeter.png","CamSettings_Button_ON.png","CamSettings_Button_OFF.png")
    SetCamSettingOnOff("Capture Settings:Spot Meter:OFF",vncregion,"CamSettings_Label_Capture_SpotMeter.png","CamSettings_Button_OFF.png","CamSettings_Button_ON.png")

    SetCamSettingOnOff("Setup:Preview:ON",vncregion,"CamSettings_Label_Setup_Preview.png","CamSettings_Button_ON.png","CamSettings_Button_OFF.png")
    SetCamSettingOnOff("Setup:Preview:OFF",vncregion,"CamSettings_Label_Setup_Preview.png","CamSettings_Button_OFF.png","CamSettings_Button_ON.png")

    SetCamSettingOnOff("CamSettings_CamInfo_Loacation:ON",vncregion,"CamSettings_Label_CamInfo_Location.png","CamSettings_Button_ON.png","CamSettings_Button_OFF.png")
    SetCamSettingOnOff("CamSettings_CamInfo_Loacation:OFF",vncregion,"CamSettings_Label_CamInfo_Location.png","CamSettings_Button_OFF.png","CamSettings_Button_ON.png")


##########################################
### TestResolution_FPS_ProTune
##########################################
def TestResolution_FPS_ProTune():
    global IsProTune
    global IsPAL
    IsProTune = True
    IsPAL = False
    HelperLib.Log(CurrentTestCase+ ".TestResolution_FPS_ProTune:")
    #HelperLib.SwipeDownCount(vncregion,2)
    wait(2)


    setRes = "1080SuperView"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"30")
        TestResolutionFPSSetting(setRes,"24")
        TestResolutionFPSSetting(setRes,"60")
        TestResolutionFPSSetting(setRes,"48")
        wait(2)

    setRes = "4K-17-9"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionSetting(setRes)
        TestResolutionFPSSetting(setRes,"12")
        wait(2)


    setRes = "4K"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"15")
        wait(2)


    setRes = "27K-17-9"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"24")
        wait(2)

    setRes = "27K"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"30")
        wait(2)

    setRes = "1440"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"48")
        TestResolutionFPSSetting(setRes,"30")
        TestResolutionFPSSetting(setRes,"24")
        wait(2)


    setRes = "1080"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"60")
        TestResolutionFPSSetting(setRes,"48")
        TestResolutionFPSSetting(setRes,"30")
        TestResolutionFPSSetting(setRes,"24")
        wait(2)

    setRes = "960"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"100")
        TestResolutionFPSSetting(setRes,"60")
        wait(2)

    setRes = "720SuperView"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"100")
        TestResolutionFPSSetting(setRes,"60")
        wait(2)

    setRes = "720"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"60")
        TestResolutionFPSSetting(setRes,"120")
        wait(2)

##########################################
### TestResolution_FPS
##########################################    
def TestResolution_FPS():
    global IsProTune
    global IsPAL
    IsProTune = False
    IsPAL = False
    HelperLib.Log(""+CurrentTestCase+ ".TestResolution_FPS:")

    #HelperLib.SwipeDownCount(vncregion,1)
    wait(2)
    setRes = "4K-17-9"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"12")

    setRes = "4K"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"15")

    setRes = "960"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"60")
        TestResolutionFPSSetting(setRes,"48")
        TestResolutionFPSSetting(setRes,"100")

    setRes = "27K-17-9"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"24")

    setRes = "27K"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"30")

    setRes = "1440"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"48")
        TestResolutionFPSSetting(setRes,"30")
        TestResolutionFPSSetting(setRes,"24")

    setRes = "1080SuperView"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"60")
        TestResolutionFPSSetting(setRes,"48")
        TestResolutionFPSSetting(setRes,"30")
        TestResolutionFPSSetting(setRes,"24")

    setRes = "1080"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"60")
        TestResolutionFPSSetting(setRes,"48")
        TestResolutionFPSSetting(setRes,"30")
        TestResolutionFPSSetting(setRes,"24")



    setRes = "720SuperView"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"60")
        TestResolutionFPSSetting(setRes,"48")
        TestResolutionFPSSetting(setRes,"100")


    setRes = "720"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"60")
        TestResolutionFPSSetting(setRes,"120")


    setRes = "WVGA"
    if TestResolutionSetting(setRes) == True:
        #if TestVerifyFPS(setRes) == True:
        TestResolutionFPSSetting(setRes,"240")



def TestResolutionSetting(setRes):
    global failCount
    global passCount
    HelperLib.Log(CurrentTestCase+ ".TestResolutionSetting:"+setRes)
    try:
        if SetVideoResolution(setRes) == True:
            passCount+=1
            HelperLib.Report("PASSED: TestResolutionSetting - "+setRes)
            return True
        else:
            HelperLib.Report("FAILED: TestResolutionSetting - "+setRes)
            HelperLib.Log("**** FAILED "+CurrentTestCase+ ".TestResolutionSetting:"+setRes+" *****")
            HelperLib.TakeScreenShot("FAILED_TestResolutionSetting"+setRes+".png")
            return False

    except Exception, err:
        HelperLib.Log("===>ERROR: " +str(err))
        failCount+=1
        HelperLib.Report("FAILED: TestResolutionSetting - "+setRes)
        HelperLib.Log("**** FAILED "+CurrentTestCase+ ".TestResolutionSetting:"+setRes+" *****")
        HelperLib.TakeScreenShot("FAILED_TestResolutionSetting"+setRes+".png")
        return False

def TestVerifyFPS(Res):
    global failCount
    global passCount
    HelperLib.Log(CurrentTestCase+ ".TestVerifyFPS:"+Res)
    try:
        printReport = True
        if VerifyFPS(Res) == True:
            passCount+=1
            HelperLib.Report("PASSED: TestVerifyFPS - "+Res)
            return True
        else:
            HelperLib.Report("FAILED: TestVerifyFPS - "+Res)
            failCount+=1
            HelperLib.Log("**** FAILED "+CurrentTestCase+ ".TestVerifyFPS:"+Res+" *****")
            HelperLib.TakeScreenShot("FAILED_TestVerifyFPS"+Res+".png")
            return False
    except Exception, err:
        HelperLib.Log("===>ERROR: " +str(err))
        failCount+=1
        HelperLib.Report("FAILED: TestVerifyFPS - "+Res)
        HelperLib.Log("**** FAILED "+CurrentTestCase+ ".TestVerifyFPS:"+Res+" *****")
        HelperLib.TakeScreenShot("FAILED_TestVerifyFPS"+Res+".png")
        return False


def TestResolutionFPSSetting(Res,FPS):
    global failCount
    global passCount

    HelperLib.Log(CurrentTestCase+ ".TestResolutionFPSSetting:"+Res+" - " +FPS)
    try:
        if SetFPS(Res,FPS) == True:
            passCount+=1
            HelperLib.Report("PASSED: TestResolutionFPSSetting - "+Res+" - " +FPS)
            return True
        else:
            HelperLib.Report("FAILED: TestResolutionFPSSetting - "+Res+" - " +FPS)
            failCount+=1
            HelperLib.Log("**** FAILED "+CurrentTestCase+ ".SetFPS:"+Res+"_"+FPS+" *****")
            HelperLib.TakeScreenShot("FAILED_TestResolutionFPSSetting"+Res+"_"+FPS+".png")
            return False
    except Exception, err:
        HelperLib.Log("===>ERROR: " +str(err))
        failCount+=1
        HelperLib.Report("FAILED: TestResolutionFPSSetting - "+Res+" - " +FPS)
        HelperLib.Log("**** FAILED "+CurrentTestCase+ ".TestResolutionFPSSetting:"+Res+"_"+FPS+" *****")
        HelperLib.TakeScreenShot("FAILED_TestResolutionFPSSetting"+Res+"_"+FPS+".png")
        return False



##########################################
#END Script Functions  <----
##########################################



##########################################
#Start Framework Init Start  ---->
##########################################


HelperLib.SetTestResultsPath(None,CurrentTestCase, zRootProjectDir)

HelperLib.getEnvironment()
#VNCTitle = "adb:Android_Samsung_Galaxy_S3_412"
VNCTitle = "GoPro Gesktop App"
vncregion = HelperLib.SetVNCAppRegion(VNCTitle)


if not vncregion:
    print "FAILED","vncregion is not defined"
    exit(1)
#MobileAppsLib.TakeScreenShot("Test_Start.png")
HelperLib.OCR(True)
HelperLib.Log("****Framework Init Complete*****")

### GLOBALS
IsProTune = False
IsPAL = False
setRes = ""
failCount=0
passCount=0

##########################################
#END Framework Init  <----
##########################################


#########################################################
### START Script Suite  ---->
#########################################################
HelperLib.Log("****START Script Suite "+CurrentTestCase +"*****")
HelperLib.Report("*************************")
HelperLib.Report("START TEST "+CurrentTestCase)
HelperLib.Report("*************************")
HelperLib.TakeScreenShot(CurrentTestCase+"_Start.png")


#ocrtext = vncregion.text()
#if ocrtext:
#    print ocrtext
#HelperLib.Log("OCR------\n" + ocrtext +"\n---------\n")



HelperLib.Report("*************************")
HelperLib.Report("END TEST "+CurrentTestCase)
HelperLib.Report("*************************")

HelperLib.Report("*************************")
HelperLib.Report("PASSED: "+str(passCount))
HelperLib.Report("FAILED: "+str(failCount))
HelperLib.Report("-------------------------")
HelperLib.Report("Total : "+str((failCount+passCount)))

HelperLib.Report("*************************")


#########################################################
### END Script Suite  <----
#########################################################
