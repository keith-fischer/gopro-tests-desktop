
import java
import sys
import os
import shutil
from time import strftime
from sikuli import *
from __builtin__ import True, False
#from sikuli.Sikuli import *

#need the guide extension
#from guide import *

VNCTitle = ""
targetApp = ""
TestScriptName = ""
RootProjectDir = ""
LibPath = ""
TestResultsPath = ""
TestFolderName = ""
Pattern_Similar_Value = 0.90
logpath = "" #script errors
LogScriptPath = "" #test script transaction
reportpath = "" #test results
vncregion = ""
debug = True
printReport = True
Settings.ClickDelay = 0.5
Settings.setShowActions = 1.0
Settings.SlowMotionDelay = 1.0

##########################################
#debugPrint
##########################################
def debugPrint(info):
    if debug == True:
        print "*** DEBUG:",str(info)


##########################################
#AutoThresholdWait
##########################################
def AutoThresholdWait(imgRegion,imageName):
    global Pattern_Similar_Value
    try:
        SmartyLib.Log("AutoThresholdWait: " + imageName)
        Pattern_Similar_Value = 0.99
        
        #imageP = SmartyLib.PATTERN( imageName)
        foundImg = SmartyLib.WAIT(imgRegion,imageName)
        while not foundImg:
            if Pattern_Similar_Value < 0.60:
                break
            SmartyLib.Log("AutoThresholdWait: " + str(Pattern_Similar_Value))
            Pattern_Similar_Value = Pattern_Similar_Value -0.5
            imageP = SmartyLib.PATTERN( imageName)
            foundImg = SmartyLib.WAIT(imgRegion,imageP)

        SmartyLib.Log("AutoThresholdWait: EXIT" + str(Pattern_Similar_Value))
        Pattern_Similar_Value = 0.90
        if foundImg:
            SmartyLib.Log("AutoThresholdWait: FOUND" + str(foundImg))
            return foundImg
        else:
            return None
    except Exception, err:
        SmartyLib.Log("===>ERROR AutoThresholdWait: " +str(err))
        SmartyLib.CLICK(vncregion,"Android_Menu_Back.png")
        return False




##########################################
#WAIT
##########################################
def WAIT(imgregion,image):
    try:
        if not image:
            Log("WAIT ERROR image is null: ")
            return None
        foundimg = None
        imageP = image
        if not isinstance( image , Pattern):
            Log("WAIT Set Pattern: "+ str(image))
            imageP = PATTERN(image)
  
            foundimg = imgregion.exists(imageP,10)
            if foundimg is Nothing:
                foundimg = None
        #    foundimg = imgregion.wait(image)
        #    if foundimg is not None:
        #        foundimg = Region(foundimg)
        #        Log("WAIT Pattern FOUND: "+ str(image))
        #    else:
        #        Log("WAIT NOT FOUND: "+ str(image))
        #        imgregion.hightlight(1)
        #        return None
        #else:
        #    Log("WAIT Image: "+ str(image))
        #    foundimg = imgregion.wait(PATTERN(image))
        #    #foundimg = imgregion.find(PATTERN(image))
        #    if foundimg is not None:
        #        foundimg = Region(foundimg)
        #        Log("WAIT Image FOUND: "+ str(image))

        if foundimg is not None:
            Log("WAIT FOUND: "+ str(foundimg))
            foundimg.highlight(1)
            return foundimg
        else:
            Log("WAIT NOT FOUND: "+ str(image))
            imgregion.hightlight(1)
            return None
    except Exception, err:
        Log("ERROR WAIT: " +str(err))
        return None

##########################################
#CLICK
##########################################
def CLICK(imgregion,image):
    try:
        Log("CLICK: "+ str(image))
        wait(1)
        foundimg = WAIT(imgregion,image)
    
        if foundimg:
            Log("CLICKED: "+ str(image))
            foundimg.click()
            wait(1)
            return True
        else:
            Log("NOT CLICKED: "+ str(image))
            imgregion.hightlight(3)
            return False
    except Exception, err:
        Log("ERROR CLICK: " +str(err))
        return False

##########################################
#TakeScreenShot
##########################################
def TakeScreenShot(ScreenName):
    Log("TakeScreenShot: "+ ScreenName)
    ScreenShot(TestResultsPath,vncregion,ScreenName)


##########################################
#OCR(EnableTrue_OR_DisableFalse
##########################################
def OCR(EnableTrue_OR_DisableFalse):
    Settings.OcrTextSearch=EnableTrue_OR_DisableFalse
    Settings.OcrTextRead=EnableTrue_OR_DisableFalse

##########################################
#PATTERN
##########################################
def PATTERN(image):
#    SmartyLib.Log("SmartyLib.PATTERN:"+str(image) )
    return Pattern(image).similar(Pattern_Similar_Value)

##########################################
#ScreenShot
##########################################
def ScreenShot(ResultsPath, imgRegion, FileName):
    Log("ScreenShot:" + ResultsPath +"/"+FileName+":"+str(imgRegion))  

    #srn=imgRegion.getScreen()
    #srnfile = srn.capture(imgRegion)
    switchAppVNC()
    #bounds = imgRegion.getBounds()

    #srn0 = Screen(0)
    #srnfile = capture()
    #srnfile=srn0.capture(imgRegion)
    imgRegion.highlight(1)
    srnfile=capture(imgRegion)
    wait(1)
    fullpath=os.path.join(ResultsPath,FileName)
    Log("ScreenShot:path - " + fullpath)
    shutil.move(str(srnfile),fullpath ) 
    Log("ScreenShot:Moved - " + FileName)

##########################################
#set app object
##########################################
def SetApp(appTitle):
    Log("SetApp")
    a=App(appTitle)
    a.focus()
    return a

##########################################
#set region object
#assumes ultravnc single window(0)
##########################################

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

####################################################
### SetAppRegion
####################################################
def SetAppRegion(AppObject,RegWidth,RegHeight):
    Log("SetAppRegion: Find W=" + str(RegWidth)+" - H="+str(RegHeight))
    AppObject.focus()
    wait(1)
    # r = AppObject.window(2)
    #Found: HUAWEI(7448) Region[1181,56 496x914]@Screen(0)[0,0 1680x1050] E:Y, T:3.0 E:Y, T:3.0
    for i in range(100):
        w = AppObject.window(i)
        if not w: 
            Log(str(i)+" - SetAppRegion:Window Not Found" )
            break
            #exit("Window Not Found")
        else:
            Log(str(i) +" - SetAppRegion - W="+str(w.getW())+" - H="+ str(w.getH()))
            if w.exists("global_vncregion_title.png"):
                print i, " # ", w   
                Log("SetAppRegion:Found by Title: " + getRegionInfo(w))
                w.highlight(3)
                break
            elif w.getW() >= RegWidth:
                if w.getH() >= RegHeight:
                    w.highlight(3)
                    print i, " # ", w   
                    Log("SetAppRegion:Found by Size: " + getRegionInfo(w))
                    break
    return w

####################################################
### SetAppRegionExitOnNull
####################################################
def SetAppRegionExitOnNull(AppObject,RegWidth,RegHeight):
    Log("SetAppRegionExitOnNull")
    r = SetAppRegion(AppObject,RegWidth,RegHeight)
    #Validate region not null
    if not r: 
        print "Not Found: " ,AppObject, r
        r = selectRegion("Select the VNC window region")
        if not r:
            exit("Not Found") #exit script target app window region is invalid
        else:
            print "Found: " ,AppObject, r
    else: 
        print "Found: " ,AppObject, r
        return r

 
####################################################
### SetVNCAppRegion
####################################################   
def SetVNCAppRegion(VNCTitle):
    global targetApp
    global vncregion
    AppTitle = VNCTitle #"LG-E980" #"HUAWEI"
    Log("SetVNCAppRegion:Find "+AppTitle)
    targetApp = SetApp(AppTitle)
    vncregion = SetAppRegionExitOnNull(targetApp, 496,914)
    if vncregion:
        Log("SetVNCAppRegion: Found")
    else:
        Log("SetVNCAppRegion: NOT Found")
    return vncregion



##########################################
#SetTestResultsPath
##########################################
def SetTestResultsPath(self,testname,ProjectDir):
    global TestFolderName
    global TestScriptName
    global LogScriptPath
    global logpath
    global TestResultsPath
    global RootProjectDir
    global reportpath

    RootProjectDir = ProjectDir
    print "SetTestResultsPath:*****************"
    dt = strftime("%Y%m%d_%H%M%S")    
    print "DATETIME",dt
    TestScriptName = testname
    
    #set test results folder name
    TestFolderName = TestScriptName + "_" + dt
    TestResultsPath = RootProjectDir + "\\TestResults\\" + TestFolderName
    imgroot=RootProjectDir+"\\SmartyLib"
    addImagePath(imgroot)
    print "SetTestResultsPath:addImagePath",imgroot
    
    imgroot=RootProjectDir + "\\Images"
    addImagePath(imgroot)
    print "SetTestResultsPath:addImagePath",imgroot
    imgtest=RootProjectDir+"\\"+TestScriptName+".sikuli"
    addImagePath(imgtest)
    print "SetTestResultsPath:addImagePath",imgtest
    #create the new test results folder
    os.makedirs(TestResultsPath)
    #Set the log file path
    LogScriptPath = TestResultsPath + "\\" + TestScriptName + "_ScriptLog.txt"    
    logpath = TestResultsPath + "\\" + TestScriptName + "_Log.txt"
    reportpath  = TestResultsPath + "\\" + TestScriptName + "_Report.txt"
    print "SetTestResultsPath:TestScriptName",TestScriptName    
    print "SetTestResultsPath:TestResultsPath",TestResultsPath    
    print "SetTestResultsPath:LogScriptPath",LogScriptPath    
    print "SetTestResultsPath:logpath",logpath    
    print "SetTestResultsPath:reportpath",reportpath    
    Log("****Framework Init Started*****")
    Report("****TEST REPORT *****")
####################################################
### getEnvironment
####################################################
def getEnvironment():
    Log("getEnvironment")
    envOS=Env.getOS()
    envOSVer=Env.getOSVersion()
    envSikuliVer=Env.getSikuliVersion()
    print "OS",envOS
    print "OS Version",envOSVer
    print "Sikuli Ver: ",envSikuliVer
    # getImagePath() returns a Java array of unicode strings
    imgPath = list(getImagePath()) # makes it a Python list
    # to loop through
    if imgPath:
        for p in imgPath:
            print "IMAGE PATH: " + p
    else:
        print "imgPath not found"

####################################################
### Log2
####################################################
def Report(msg):
    if printReport == False:
        Log("Report Skipped:"+str(printReport))
        return
    if not reportpath:
        Log("Report:INVALID Path")
        return
    else:
        print "Report:",reportpath
    if not msg:
        return
    s = strftime("%H:%M:%S")+"\t"
    output = "\n"+s+msg+ "\r\n"
    print "Report:",output
    try:
        f=open(reportpath, 'a')
        f.write(output  )
    except:
        print "***Failed: Report write - "+reportpath
    finally:
        f.close()

####################################################
### Log2
####################################################
def Log2(pathname,msg):
    if not pathname:
        return
    if not msg:
        return
    print "\n"+msg
    try:
        f=open(pathname, 'a')
        f.write(msg+"\r\n")
    except:
        print "***Failed: Log2 write - "+pathname
    finally:
        f.close()

####################################################
### Log
####################################################
def Log(msg):
    #global logpath
    s = strftime("%H:%M:%S")+"\t"
    try:
        Log2(logpath,s+msg)
    except:
        print "\n"+s+msg

####################################################
### strCharBlock
####################################################
def strCharBlock(char,count):
    rc=""
    for x in range(count):
        rc+=char
    return rc

####################################################
### switchAppVNC
####################################################
def switchAppVNC():
    Log("switchAppVNC:"+VNCTitle)
    switchApp(VNCTitle)
    #Log("switchAppVNC:"+VNCTitle)


####################################################
### 
####################################################
#def getRegionInfo(imageregion):
#    info = vncregion.find(imageregion).getFileName()
#    return info


####################################################
### TabFields
####################################################
def TabFields(imgRegion,TabCount):
    #App.focus("vncviewer.exe")
    Log("TabFields:")
    switchAppVNC()
    
    for i in range(TabCount):
        imgRegion.type(Key.TAB)

####################################################
### KeyUp
####################################################
def KeyUp(imgRegion,keyDownCount):
    Log("KeyUp:")
    switchAppVNC()
    
    LocStart =  imgRegion.getCenter().above(20)
    LocStop  =  imgRegion.getCenter().above(280)
    imgRegion.mouseMove(LocStart)
    for i in range(keyDownCount):
        type(Key.UP)
        wait(1)


####################################################
### KeyDown
####################################################
def KeyDown(imgRegion,keyDownCount):
    Log("KeyDown:")
    switchAppVNC()
    
    LocStart =  imgRegion.getCenter().above(20)
    LocStop  =  imgRegion.getCenter().above(280)
    imgRegion.mouseMove(LocStart)
    for i in range(keyDownCount):
        type(Key.DOWN)
        wait(1)
####################################################
### SwipeUp
####################################################
def SwipeUp2(imgRegion):
    Log("SwipeUp:")
    #App.focus("vncviewer.exe")#App.focus method does not work
    switchAppVNC()
    
    LocStart =  imgRegion.getCenter().above(20)
    LocStop  =  imgRegion.getCenter().above(250)
    
#    imgRegion.mouseUp()
#    imgRegion.mouseMove(LocStart)
#    imgRegion.mouseUp()
#    imgRegion.dragDrop(LocStart,LocStop)
#    imgRegion.drag(LocStart)
#    imgRegion.dropAt(LocStop)
#    imgRegion.mouseUp(Button.LEFT)
#    imgRegion.mouseMove(LocStart)
#    wait(1)
#    imgRegion.mouseDown(Button.LEFT)
##    wait(1)
#    imgRegion.mouseMove(LocStop)
#    wait(1)
#    imgRegion.mouseUp()
#    imgRegion.mouseUp()
    wait(2)


####################################################
### WheelUp(imgRegion): scroll list up
####################################################
def WheelUp(imgRegion):
    Log("WheelUp:")
    switchAppVNC()
    LocStart =  imgRegion.getCenter().above(20)
    LocStop  =  imgRegion.getCenter().above(280)
    imgRegion.mouseMove(LocStart)
    imgRegion.wheel(LocStart,WHEEL_UP, 1)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)    
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)    
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)    

#    imgRegion.wheel(LocStart,WHEEL_DOWN, 1)  
#    imgRegion.wheel(LocStart,WHEEL_UP, 1)    
    wait(1)

####################################################
### WheelDown(imgRegion): scroll list down
####################################################
def WheelDown(imgRegion):
    Log("WheelDown:")
    switchAppVNC()
    LocStart =  imgRegion.getCenter().above(20)
    LocStop  =  imgRegion.getCenter().above(280)
    imgRegion.mouseMove(LocStart)
    imgRegion.wheel(LocStart,WHEEL_DOWN, 1)
    type(Key.UP)
    type(Key.UP)
    type(Key.UP)   
    type(Key.UP)
    type(Key.UP)
    type(Key.UP)    
    type(Key.UP)
    type(Key.UP)
    type(Key.UP)    

#    imgRegion.wheel(LocStart,WHEEL_UP, 1)
#    imgRegion.wheel(LocStart,WHEEL_DOWN, 1)    
    wait(1)


#def SwipeUp(imgRegion):
#    for i in range(10):  
#        SwipeUpA(imgRegion)
#def SwipeDown(imgRegion):
#    for i in range(10):  
#        SwipeDownA(imgRegion)

####################################################
### SwipeUp
####################################################
def SwipeUp(imgRegion):
    Log("SwipeUp:")
    #App.focus("vncviewer.exe")#App.focus method does not work
    switchAppVNC()
    
    LocStart =  imgRegion.getCenter().below(20)#20
    LocStop  =  imgRegion.getCenter().above(20)#250
    imgRegion.mouseMove(LocStart)
    wait(.50)
    imgRegion.mouseDown(Button.LEFT)
    #wait(1)
    #imgRegion.drag(LocStart)
    #wait(.50)
    #imgRegion.dropAt(LocStop)
    imgRegion.mouseMove(LocStop)
    #wait(.50)
    imgRegion.mouseUp(Button.LEFT)    

    wait(2)

    
####################################################
### SwipeDown
####################################################
def SwipeDown(imgRegion):
    Log("SwipeDown:")
    #App.focus("vncviewer.exe") #App.focus method does not work
    switchAppVNC()
    LocStart =  imgRegion.getCenter().above(20)
    LocStop  =  imgRegion.getCenter().below(20)
    imgRegion.mouseMove(LocStart)
    wait(.50)
    imgRegion.mouseDown(Button.LEFT)
   # wait(.50)
    #imgRegion.drag(LocStart)
    #imgRegion.dropAt(LocStop)
    imgRegion.mouseMove(LocStop)
    wait(.50)
    imgRegion.mouseUp(Button.LEFT)    
#    imgRegion.mouseMove(LocStart)
#    wait(1)
#    imgRegion.mouseDown(Button.LEFT)
##    wait(1)
#    imgRegion.mouseMove(LocStop)
#    wait(1)
#    imgRegion.mouseUp()
    wait(2)
####################################################
### SwipeDown
####################################################
def SwipeUpCount(imgRegion, swipeCount):
    for i in range(swipeCount):
        SwipeUp(imgRegion)
####################################################
### SwipeDown
####################################################        
def SwipeDownCount(imgRegion, swipeCount):
    for i in range(swipeCount):
        SwipeDown(imgRegion)

####################################################
### SwipeFind
####################################################
def SwipeFind(imgRegion, FindRegion, swipeCount):
    
    for i in range(swipeCount):
        regionFound = WaitHighlight(imgRegion,FindRegion,5)
        if regionFound:
            break
        else:
            SwipeUp(imgRegion)
    if not regionFound:
        for i in range(swipeCount):
            regionFound = WaitHighlight(imgRegion,FindRegion,5)
            if regionFound:
                break
            else:
                SwipeDown(imgRegion)
    return regionFound
    
####################################################
### ClickHighlight
####################################################
def ClickHighlight(imgClick):
    Log("ClickHighlight:")
#    imageFound=WaitHighlight(imgRegion,imgClick,10)
    imgClick.highlight(1)
    ClickImage(imgClick)
    


####################################################
### ClickImage
####################################################
def ClickImage(imgClick):
    #imagecount = imagecount + 1
    #fname="ClickImage"+str(imagecount)+".png"
    Log("*******ClickImage:"+str(imgClick))
   # ScreenShot(TestFolder,imgClick,fname)
    #wait(1)
    imgClick.click()


####################################################
### returns found region, not found is none
### highlights the found region
####################################################
def IsFindImage(imgRegion,imgFind,timeout):
    Log("IsFindImage:" + str(imgFind))
    if imgRegion.exists(imgFind,timeout):
        imgFound=imgRegion.find(imgFind)
        Log("IsFindImage:FOUND" )
        return imgFound
    else:
        Log("IsFindImage:NOT FOUND" )
        return 
    #WAIT(imgRegion,imgFind)

####################################################
### WaitHighlight
####################################################
def WaitHighlight(imgRegion,imgHighlight):
    return WaitHighlight(imgRegion,imgHighlight,2)

####################################################
### WaitHighlight
### returns found match object imgHighlight within imgRegion, not found is none
### highlights the found imgHighlight
####################################################
def WaitHighlight(imgRegion,imgHighlight,timeout):
    Log("WaitHighlight:" + str(imgHighlight))
    foundimg = IsFindImage(imgRegion,imgHighlight,timeout)
    if foundimg:
        foundimg.highlight(1)
        Log("WaitHighlight:Found")
        return foundimg
    else:
        Log("WaitHighlight:Not Found")
        return


####################################################
### TabScroll
### Scrolls list until target is visible and clicks target
####################################################
def TabScroll(imgRegion, imgFind, TabCount):
    Log("TabScroll:" + str(imgFind))

    for x in range(TabCount):
        waitregion = WaitHighlight(imgRegion,imgFind,1)
        if waitregion:
            Log("TabScroll: FOUND")
            return waitregion
        else:
            Log("TabScroll: "+ str(x))
            TabFields(imgRegion,1)


#search failed        
    Log("FAILED:TabScroll:" + str(imgFind))
    return none




####################################################
### FindScroll
### Scrolls list until target region is visible and 
### returns found region for further action
### WHEEL_MOVE is ignored for now
### WHEEL_UP_DOWN = WHEEL_UP OR WHEEL_UP_DOWN = WHEEL_DOWN (sikuli wheel direction constant)
####################################################
def FindScroll(imgRegion, imgFind, WHEEL_UP_DOWN, WHEEL_MOVE, WHEEL_MOVE_COUNT):
    Log("FindScroll:" + str(imgFind))
    switchAppVNC()
    for x in range(WHEEL_MOVE_COUNT):
        waitregion = WaitHighlight(imgRegion,imgFind,2)
        if waitregion:
            wait(3)
            waitregion = WaitHighlight(imgRegion,imgFind,1)            
            Log("FindScroll: FOUND")
            return waitregion
        else:
            if WHEEL_UP_DOWN == WHEEL_DOWN:
                Log("FindScroll: WheelDown" + str(x))
                WheelDown(imgRegion)
                #KeyDown(imgRegion,2)
            else:
                Log("FindScroll: WheelUp" + str(x))
                WheelUp(imgRegion)
                #KeyUp(imgRegion,2)
            wait(1)
            waitregion = WaitHighlight(imgRegion,imgFind,1)
            if waitregion:
                wait(3)
                waitregion = WaitHighlight(imgRegion,imgFind,1)
                Log("FindScroll: FOUND")
                return waitregion
#Try scroll other direction
    Log("FindScroll: Try Opposite direction")
    for x in range(WHEEL_MOVE_COUNT):
        waitregion = WaitHighlight(imgRegion,imgFind,2)
        if waitregion:
            Log("FindScroll: FOUND")
            return waitregion
        else:
            if WHEEL_UP_DOWN == WHEEL_DOWN:
                Log("FindScroll: WheelUp" + str(x))
                WheelUp(imgRegion)
                #KeyUp(imgRegion,2)
            else:
                Log("FindScroll: WheelDown" + str(x))
                WheelDown(imgRegion)
                #KeyDown(imgRegion,2)
            wait(1)
            waitregion = WaitHighlight(imgRegion,imgFind,1)
            if waitregion:
                wait(3)
                waitregion = WaitHighlight(imgRegion,imgFind,1)
                Log("FindScroll: FOUND")
                return waitregion            
#search failed        
    Log("FAILED:FindScroll:" + imgFind)
    return none




####################################################
### ClickScroll
### Scrolls list until target is visible and clicks target
####################################################
def ClickScroll(imgRegion, imgClick, WHEEL_UP_DOWN, WHEEL_MOVE, WHEEL_MOVE_COUNT):
    Log("ClickScroll:" + str(imgClick))

    for x in range(WHEEL_MOVE_COUNT):
        waitregion = FindScroll(imgRegion,imgClick,1,1,WHEEL_MOVE_COUNT)
        #waitregion = WaitHighlight(imgRegion,imgClick,2)
        if waitregion:
            ClickHighlight(waitregion)
            Log("ClickScroll: Clicked")
            return waitregion
        else:
            Log("ClickScroll:" + str(x))
#            SwipeUp(imgRegion)
            #imgRegion.wheel(WHEEL_DOWN, WHEEL_MOVE)
            wait(3)
    Log("FAILED:ClickScroll:" + imgClick)
    exit()

####################################################
### ClickVerify
####################################################
def ClickVerify(imgRegion,imgClick,imgVerify):
    print "ClickVerify",imgClick,imgVerify
    Log("ClickVerify:" + ":"+str(imgClick)+":"+str(imgVerify))
    for x in range(2):
        waitregion = WaitHighlight(imgRegion,imgClick,1)
        if waitregion:
            Log("ClickVerify:Click" )
            ClickHighlight(waitregion)
            waitVregion = WaitHighlight(imgRegion,imgVerify,10)
            if waitVregion:
                Log("ClickVerify:Found" )
                return waitVregion
            else:
                Log("ClickVerify:NOT Found" )
        else:
            Log("ClickVerify:" + str(x))
    Log("FAILED:ClickVerify" + imgClick)
    exit()

####################################################
### ClickScrollVerify
####################################################
def ClickScrollVerify(imgRegion,imgClick,imgVerify,WHEEL_UP_DOWN,WHEEL_MOVE,WHEEL_MOVE_COUNT):
    Log("ClickScrollVerify:"+str(imgClick)+":"+str(imgVerify))
    for x in range(4):
        waitregion = ClickScroll(imgRegion,imgClick,WHEEL_DOWN,WHEEL_MOVE,WHEEL_MOVE_COUNT)
        if waitregion:
            Log("ClickScrollVerify:Clicked")
            waitregion = WaitHighlight(imgRegion,imgVerify,10)
            if waitregion:
                Log("ClickScrollVerify:Found")
                return waitregion
            else:
                Log("FAILED:ClickScrollVerify:Verify:" + imgVerify)
        else:
            Log("ClickScrollVerify:Click:" + str(x))
    Log("FAILED:ClickScrollVerify:Click:" + imgClick)
    exit(1)
####################################################
### AssertScroll
####################################################
def AssertScroll(imgRegion,imgAssert,WHEEL_UP_DOWN,WHEEL_MOVE,WHEEL_MOVE_COUNT):
    Log("AssertScroll:"+str(imgAssert))
    for x in range(2):
        waitregion = FindScroll(imgRegion,imgAssert,WHEEL_DOWN,WHEEL_MOVE,WHEEL_MOVE_COUNT)
        if waitregion:
            Log("PASSED:AssertScroll")
            return waitregion
        else:
            Log("AssertScroll:Search:" + str(x))
    Log("FAILED:AssertScroll:" + imgAssert)
    exit(1)
####################################################
### AssertNotScroll
####################################################
def AssertNotScroll(imgRegion,imgAssert,WHEEL_UP_DOWN,WHEEL_MOVE,WHEEL_MOVE_COUNT):
    Log("AssertNotScroll:"+str(imgAssert))
    for x in range(2):
        waitregion = FindScroll(imgRegion,imgAssert,WHEEL_DOWN,WHEEL_MOVE,WHEEL_MOVE_COUNT)
        if waitregion:
            Log(" FAILED:AssertNotScroll")
            exit(1)
        else:
            Log("AssertNotScroll:Search:" + str(x))

    Log("PASSED:AssertNotScroll")
    return none

####################################################
### FieldInput
####################################################
def FieldInput(imgRegion,imgField,keyText):
    Log("FieldInput:" + keyText)
    imgfound = TabScroll(imgRegion,imgField,10)
    if imgfound:
        click(imgfound)
        imgfound.type(keyText)
        TabFields(imgRegion,1)
        Log("FieldInput: Found")
        return
    Log("FieldInput: FAILED") 
    exit()
    
####################################################
### FieldInputSelectItem
####################################################
def FieldInputSelectItem(imgRegion,imgField,imgFldSelectDefault,imgSelectPick,imgFldSelected):
    Log("FieldInputSelectItem:" )
    #do phone type select first for default phone field image
    TabScroll(vncregion,imgField,10)
    ClickVerify(vncregion,imgFldSelectDefault ,imgSelectPick )
    ClickVerify(vncregion,imgSelectPick   ,imgFldSelected )
    Log("FieldInputSelectItem:Selected" )


##########################################
### TestDebug
##########################################
def TestDebug(vncregion):
    Log("\n\r-------------------------------------")
    Log("START: TestDebug")

#    ocr=vncregion.text()
#    print "OCR=", ocr

#    exit()

    Log("PASSED: TestDebug ")


##########################################
### Script START DEBUG: this is temp code for test debug/construction
##########################################

##########################################
### Script END DEBUG
##########################################


##########################################
#Script Start VoiceMail
##########################################
def TestVoiceMail(vncregion):
    Log("\n\r-------------------------------------")
    Log("START: TestVoiceMail ")
    #ClickVerify(vncregion,"App_PeopleTab.png" , "Apps_PeopleTab.png" )

    #ClickVerify(vncregion, "Apps_AppsTab.png" , "Apps_verifyAppsPeopleTabs.png" )
    
    ClickVerify(vncregion,"Home_Voicemail.png" ,"Home_headVoicemail.png"  )
    wait(5)
    ClickVerify(vncregion,"Home_VoicemailHangup.png"  , "Home_Voicemail.png"  )
    

    Log("PASSED: TestVoiceMail")
##########################################
#Script Start Home
##########################################

#ClickVerify(vncregion,"Home_GreatCall.png" ,"Home_Head-GreatCall.png" )



##########################################
#Script Home Contacts Us
##########################################
def TestContactUs(vncregion):
    Log("\n\r-------------------------------------")
    Log("START: TestContactUs ")
    ClickVerify(vncregion,"Home_GreatCall.png" ,"Home_Head-GreatCall.png" )

    ClickVerify(vncregion,"Home_ContactUs.png","Home_ContactUs_verifyNeedHelpAccount.png")

    ClickVerify(vncregion,"Global_BackButton.png","Home_Head-GreatCall.png")
    
    ClickVerify(vncregion,"Global_BackButton.png","Home_GreatCall.png")
    
    #ClickVerify(vncregion,"Home_GreatCall.png" ,"Home_Head-GreatCall.png" )
    Log("PASSED: TestContactUs")
##########################################
#-->Script Home Featured Apps
##########################################
def TestFeaturedApps(vncregion):

    Log("\n\r-------------------------------------")
    Log("START: TestFeaturedApps ")
    ClickVerify(vncregion,"Home_GreatCall.png" ,"Home_Head-GreatCall.png" )
    
    ClickVerify(vncregion,"Home_FeaturedApps.png","Home_FeaturedApps_headFeaturedApps.png")
    
    ClickVerify(vncregion,"FeaturedApps_5Star.png","FeaturedApps_PlayStore.png")

    
    ClickVerify(vncregion,"Global_BackButton.png","Home_FeaturedApps_headFeaturedApps.png")
    ClickVerify(vncregion,"Global_BackButton.png","Home_Head-GreatCall.png")

    ClickVerify(vncregion,"Global_BackButton.png","Apps_verifyAppsPeopleTabs.png")
    Log("PASSED: TestFeaturedApps")
##########################################
#<--Script Home Featured Apps
##########################################
    
##########################################
#-->Script Home People Add contact
#start from home
##########################################
def TestAddContact(vncregion):
    Log("\n\r-------------------------------------")    
    Log("START: TestAddContact ")
    
    ClickVerify(vncregion,"App_PeopleTab.png" , "Apps_PeopleTab.png" )
#ClickScrollVerify(vncregion,  ,  ,WHEEL_DOWN,10,10)

    #find("Apps_PeopleTab_NoContacts.png")
    
    ClickVerify(vncregion,"global_menu.png" , "home_people_menu_AddNew.png" )

    ClickVerify(vncregion, "home_people_menu_AddNew.png", "people_NewcontactsTitle.png" )


    ClickVerify(vncregion, "people_NewcontactsTitle.png",   "People_NewPhoneContactSelectPhone.png")
    ClickVerify(vncregion,  "People_NewPhoneContactSelectPhone.png",   "people_NewcontactsTitle.png")

    FieldInput(vncregion, "People_AddNewContact_Name.png",    "Contact Name1")

    FieldInput(vncregion,"People_AddNewContact_AddOrganization.png" ,    "")

    FieldInput(vncregion,"People_AddNewContact_Company.png" ,    "Company1")

    FieldInput(vncregion,"People_AddNewContact_Title.png" ,    "Title1")

#People_AddNewContact
    FieldInputSelectItem(vncregion,"People_AddNewPhone.png","people_AddNewMobile.png" ,"people_SelectPhoneType.png","People_AddNewContact_PhoneTypeHomeSelected.png")

    FieldInput(vncregion, "People_AddNewPhone.png","555-555-5555")

#TabScroll(vncregion,"People_AddNewPhone.png",10)

#do phone type select first for default phone field image
#ClickVerify(vncregion,"people_AddNewMobile.png"  ,"people_SelectPhoneType.png"  )
#ClickVerify(vncregion,"people_SelectPhoneType.png"   ,"People_AddNewContact_PhoneTypeHomeSelected.png" )


    FieldInputSelectItem(vncregion,"People_AddNewContact_Email-1.png","People_AddNewContact_PhoneTypeHomeSelected.png","People_AddNewContact_pickMobile.png","people_AddNewMobile.png" )


#ClickVerify(vncregion,"people_AddNewMobile.png"  ,"people_SelectPhoneType.png"  )

    FieldInput(vncregion,"People_AddNewContact_Email-1.png" ,"email1@email1.com")

    TabScroll(vncregion,"People_AddNewContact_PhoneTypeHomeSelected.png",10)#default

    FieldInputSelectItem(vncregion,"people_AddContact_Address.png","People_AddNewContact_PhoneTypeHomeSelected.png","people_NewContact_SelectItem_Work.png","People_AddNewContact_SelectedWork.png" )

    FieldInput(vncregion,"people_AddContact_AddressEdit.png" ,"123 street, city state zip")

    FieldInputSelectItem(vncregion,"people_NewContactSelectGroupName.png","people_NewContactSelectGroupName.png","people_NewContactSelectGrpName_Work.png","people_SelectedGrpNameWork.png" )

    ClickVerify(vncregion, "people_GroupNameItemFieldSeleted_Work.png" ,"people_GroupNameItemFieldSeleted_Work.png")

#FieldInput(vncregion, "people_AddContactEventsDate.png","02/03/2013")

#FieldInput(vncregion, "people_AddContact_DateGroups.png","01/05/2013")

#FieldInput(vncregion,"people_AddContact_GroupName.png","My group name")


    #ClickVerify(vncregion, "home_people_Addnew_verifyDoneContact.png" ,"newContact_Save.png" )
    
    #ClickVerify(vncregion, "newContact_Save.png" ,"home_people_Addnew_verifyDoneContact.png" )
    
    ClickVerify(vncregion, "global_menu.png" ,"Apps_ExitContacts_Cancel.png" )    
    
    ClickVerify(vncregion ,"Apps_ExitContacts_Cancel.png"   ,"Apps_ExitContacts_Cancel.png" )    

    #ClickVerify(vncregion, "global_menu.png" ,"Apps_ExitContacts_Delete.png")    
    wait(3)
    ClickVerify(vncregion,find( "NewContacts_DialogTitle_DiscardChanges.png").below("App_DeleteContact_OK.png"),"Apps_PeopleTab.png")    

#ClickVerify(vncregion,"App_PeopleTab.png" , "Apps_PeopleTab.png" )

    ClickVerify(vncregion, "Apps_AppsTab.png" , "Apps_verifyAppsPeopleTabs.png" )

    Log("PASSED: TestAddContact ")    
##########################################
#<--Script Home People Add contact
#start from home
##########################################

##########################################
#Script Home  Apps
#start from home
##########################################

def SelectFavoriteApps(vncregion):
    Log("\n\r-------------------------------------")
    Log("START: SelectFavoriteApps")
    ClickScrollVerify(vncregion,"Apps_LiveNurse.png"  , "Apps_LiveNurse_headLiveNurse.png" ,WHEEL_DOWN,10,10)


    ClickVerify(vncregion,"Global_BackButton.png","Apps_verifyAppsPeopleTabs.png")



#ClickVerify(vncregion,"App_PeopleTab.png" , "Apps_PeopleTab.png" )

#ClickVerify(vncregion, "Apps_AppsTab.png" , "Apps_verifyAppsPeopleTabs.png" )

    ClickScrollVerify(vncregion, "Apps_MedCoach.png" , "Apps_MedCoach_headMedCoach.png" ,WHEEL_DOWN,10,10)

    ClickVerify(vncregion,"Global_BackButton.png","Apps_verifyAppsPeopleTabs.png")


    #ClickVerify(vncregion, "App_HomeGreatCall.png" , "Home_Head-GreatCall.png" )
    Log("PASSED: SelectFavoriteApps")

##########################################
#<--Script Home  Apps
#return to  home
##########################################

##########################################
#Script Home HELP
##########################################

def TestHelp(vncregion):
    Log("\n\r-------------------------------------")
    Log("START: TestHelp ")
    ClickVerify(vncregion, "App_HomeGreatCall.png" , "Home_Head-GreatCall.png" )
    vncregion.wait("Home_Head-GreatCall.png")

#srnshotfile = Screen.capture(vncregion)



    ClickVerify(vncregion,"Home_Help.png","Home_Help_headHelp.png")

    ClickVerify(vncregion,"Home_Help_gettingStarted.png","Home_help_headGettingStarted.png")

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")

    ClickVerify(vncregion,"Home_Help_UsingTouchScreen.png","Home_Help_head-Using-Touch-Screen.png")

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")

    ClickVerify(vncregion,"Home_Help_PhoneButtons.png" ,"Home_Help_head-PhoneButtons.png" )

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")

    ClickVerify(vncregion,"Home_Help_AppsTab.png" ,"Home_Help_head-AppsTab.png" )

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")

    ClickVerify(vncregion,"Home_Help_PeopleTab.png","Home_Help_head-PeopleTab.png")

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")

    ClickVerify(vncregion,"Home_Help_AddNewPeople.png" , "Home_Help_head-AddNewPeople.png")

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")

    ClickVerify(vncregion,"Home_Help_MakeCall.png" , "Home_Help_head-MakeACall.png")

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")

    ClickVerify(vncregion,"Home_Help_ReceivePhoneCalls.png" ,"Home_Help_head-ReceivePhoneCalls.png" )

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")
    
    #FindScroll(vncregion,"Home_Help_StatusBar.png",5,5,5)
    
    ClickScrollVerify(vncregion,"Home_Help_StatusBar.png","Home_Help_head-StatusBar.png",WHEEL_DOWN,10,10)

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")
    
    #FindScroll(vncregion,"Home_Help_Keyboard.png",5,5,5)
    
    ClickScrollVerify(vncregion,"Home_Help_Keyboard.png","Home_Help_head-Keyboard.png",WHEEL_DOWN,10,10)

    WaitHighlight(vncregion,"Home_Help_head-KeyboardDiagram.png",2)

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")

    #FindScroll(vncregion,"Home_Help_Voicemail.png",5,5,5)

    ClickScrollVerify(vncregion,"Home_Help_Voicemail.png","Home_Help_head-Voicemail.png",WHEEL_DOWN,10,10)

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")

    #FindScroll(vncregion,"Home_Help_Camera.png",5,5,5)
        

    ClickScrollVerify(vncregion,"Home_Help_Camera.png","Home_Help_head-Camera.png",WHEEL_DOWN,10,10)

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")

    #FindScroll(vncregion,"Home_Help_DownloadingApps.png",5,5,5)

    ClickScrollVerify(vncregion,"Home_Help_DownloadingApps.png","Home_Help_head-DownloadApps.png",WHEEL_DOWN,10,10)

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")

    ClickScrollVerify(vncregion,"Home_Help_FeaturedApps.png","Home_Help_head-FeaturedApps.png",WHEEL_DOWN,10,10)

    ClickVerify(vncregion,"Home_Help_button-Help-list.png","Home_Help_gettingStarted.png")

    ClickVerify(vncregion,"Home_Help_CloseHelp.png","Home_Head-GreatCall.png")

    ClickVerify(vncregion,"Global_BackButton.png","Home_Head-GreatCall.png")
    ClickVerify(vncregion,"Global_BackButton.png","Apps_verifyAppsPeopleTabs.png")
    
    Log("PASSED: TestHelp")
    
##########################################
#Script Start GoHome
##########################################
def GoHome():
    #enablelog="false"
    ClickVerify(vncregion,"Device_Btn_Home.png","App_HomeGreatCall.png")
    imgFound =  IsFindImage(vncregion,"Apps_verifyAppsPeopleTabs.png",2)
    if not imgFound:       
        ClickVerify(vncregion,"Home_Tab_Unselected.png","Apps_verifyAppsPeopleTabs.png")
    #enablelog="true"
##########################################
#Script END GoHome
##########################################
def HomeScreen_NavToAllsApps():
    waitregion = WaitHighlight(vncregion,"Home_img_AppsAndGreatCall.png",10)
    ClickVerify(vncregion,"Home_btn_Apps.png" ,"Home_Apps_Title.png" )
    
def StartSettingsApp():
    ClickScrollVerify(vncregion,"Apps_btn_Settings.png" ,"Settings_img_Title.png" ,WHEEL_DOWN,10,10)
    
def SettingsClearHomeScreenCache():
    ClickVerify(vncregion,"Settings_Btn_Apps.png" ,"Settings_Apps_Title.png"  )
    ClickScrollVerify(vncregion,"Settings_Apps_Btn_HomeScreen.png" ,"Settings_Apps_HomeScreen_Title1.png" ,WHEEL_DOWN,10,10)   
    


        
##########################################
### define functions above main script ###
##########################################

##########################################
#Framework END
##########################################


####################################################################################
#START Framework Images
#THIS DOES NOT GET CALLED
#Used just to view the image content with file name
####################################################################################
def ImageLibrary():

	find ("adbAndroid_Samsung_Galaxy_S3_412.png")
	find ("Android_Menu_Back.png")
	find ("Android_Menu_BackSeeTest.png")
	find ("AppIcon_GoPro.png")
	find ("CamMain_Button_Logo.png")
	find ("CamMain_Button_Media.png")
	find ("CamMain_Button_Mode_Burst.png")
	find ("CamMain_Button_Mode_Photo.png")
	find ("CamMain_Button_Mode_TimeLapse.png")
	find ("CamMain_Button_Mode_Video.png")
	find ("CamMain_Button_Record_OFF.png")
	find ("CamMain_Button_Record_ON.png")
	find ("CamMain_Button_Settings-1.png")
	find ("CamMain_Label_FPS_12.png")
	find ("CamMain_Label_FPS_15.png")
	find ("CamMain_Label_FPS_24.png")
	find ("CamMain_Label_FPS_30.png")
	find ("CamMain_Label_FPS_48.png")
	find ("CamMain_Label_FPS_60.png")
	find ("CamMain_Label_H3+Blk_Busy.png")
	find ("CamMain_Label_H3+Blk_Idle.png")
	find ("CamMain_Label_Protune.png")
	find ("CamMain_Label_Res_1080.png")
	find ("CamMain_Label_Res_1440.png")
	find ("CamMain_Label_Res_2-7K-17-9.png")
	find ("CamMain_Label_Res_2-7K.png")
	find ("CamMain_Label_Res_4K.png")
	find ("CamMain_Label_Res_4K17-9.png")
	find ("CamMain_Label_Wide.png")
	find ("CamSettings_Button_FrameRate.png")
	find ("CamSettings_Button_FrameRate_100FPS.png")
	find ("CamSettings_Button_FrameRate_120FPS.png")
	find ("CamSettings_Button_FrameRate_15FPS.png")
	find ("CamSettings_Button_FrameRate_240FPS.png")
	find ("CamSettings_Button_FrameRate_24FPS.png")
	find ("CamSettings_Button_FrameRate_30FPS.png")
	find ("CamSettings_Button_FrameRate_48FPS.png")
	find ("CamSettings_Button_FrameRate_60FPS.png")
	find ("CamSettings_Button_OFF.png")
	find ("CamSettings_Button_ON.png")
	find ("CamSettings_Button_VideoResolution.png")
	find ("CamSettings_Button_VideoResolution_1080.png")
	find ("CamSettings_Button_VideoResolution_1080SuperView.png")
	find ("CamSettings_Button_VideoResolution_1440.png")
	find ("CamSettings_Button_VideoResolution_27K.png")
	find ("CamSettings_Button_VideoResolution_27K179.png")
	find ("CamSettings_Button_VideoResolution_4K.png")
	find ("CamSettings_Button_VideoResolution_720.png")
	find ("CamSettings_Button_VideoResolution_720SuperView.png")
	find ("CamSettings_Button_VideoResolution_960.png")
	find ("CamSettings_Button_VideoResolution_WVGA.png")
	find ("CamSettings_DefaultDialog_Button_FrameRate_Cancel.png")
	find ("CamSettings_DefaultDialog_FrameRate_1080.png")
	find ("CamSettings_DefaultDialog_FrameRate_1080SuperView.png")
	find ("CamSettings_DefaultDialog_FrameRate_1080SuperView_ProTune.png")
	find ("CamSettings_DefaultDialog_FrameRate_1080_ProTune.png")
	find ("CamSettings_DefaultDialog_FrameRate_1440.png")
	find ("CamSettings_DefaultDialog_FrameRate_1440_ProTune.png")
	find ("CamSettings_DefaultDialog_FrameRate_27K-17-9.png")
	find ("CamSettings_DefaultDialog_FrameRate_27K-17-9_ProTune.png")
	find ("CamSettings_DefaultDialog_FrameRate_27K.png")
	find ("CamSettings_DefaultDialog_FrameRate_27K_ProTune.png")
	find ("CamSettings_DefaultDialog_FrameRate_4K-17-9.png")
	find ("CamSettings_DefaultDialog_FrameRate_4K-17-9_ProTune.png")
	find ("CamSettings_DefaultDialog_FrameRate_4K.png")
	find ("CamSettings_DefaultDialog_FrameRate_4K_ProTune.png")
	find ("CamSettings_DefaultDialog_FrameRate_720.png")
	find ("CamSettings_DefaultDialog_FrameRate_720SuperView.png")
	find ("CamSettings_DefaultDialog_FrameRate_720SuperView_ProTune.png")
	find ("CamSettings_DefaultDialog_FrameRate_720_ProTune.png")
	find ("CamSettings_DefaultDialog_FrameRate_960.png")
	find ("CamSettings_DefaultDialog_FrameRate_960_ProTune.png")
	find ("CamSettings_DefaultDialog_FrameRate_WVGA.png")
	find ("CamSettings_DefaultDialog_FrameRate_WVGA_ProTune.png")
	find ("CamSettings_Label_Adv_Color.png")
	find ("CamSettings_Label_Adv_ExposureComp.png")
	find ("CamSettings_Label_Adv_ISOLimit.png")
	find ("CamSettings_Label_Adv_ProTune.png")
	find ("CamSettings_Label_Adv_ResetDefault.png")
	find ("CamSettings_Label_Adv_Sharpness.png")
	find ("CamSettings_Label_Adv_WhiteBalance.png")
	find ("CamSettings_Label_Camera.png")
	find ("CamSettings_Label_CamInfo_Location.png")
	find ("CamSettings_Label_Capture_SpotMeter.png")
	find ("CamSettings_Label_Capture_UpsideDown.png")
	find ("CamSettings_Label_Setup_Preview.png")
	find ("CamSettings_PhotoRes_Set_12MP-Wide.png")
	find ("CamSettings_PhotoRes_Title.png")
	find ("CamSettings_Selected_FrameRate_100FPS.png")
	find ("CamSettings_Selected_FrameRate_120FPS.png")
	find ("CamSettings_Selected_FrameRate_12FPS.png")
	find ("CamSettings_Selected_FrameRate_15FPS.png")
	find ("CamSettings_Selected_FrameRate_240FPS.png")
	find ("CamSettings_Selected_FrameRate_24FPS.png")
	find ("CamSettings_Selected_FrameRate_30FPS.png")
	find ("CamSettings_Selected_FrameRate_48FPS.png")
	find ("CamSettings_Selected_FrameRate_60FPS.png")
	find ("CamSettings_Selected_VideoResolution_1080.png")
	find ("CamSettings_Selected_VideoResolution_1080SuperView.png")
	find ("CamSettings_Selected_VideoResolution_1440.png")
	find ("CamSettings_Selected_VideoResolution_27K-17-9.png")
	find ("CamSettings_Selected_VideoResolution_27K.png")
	find ("CamSettings_Selected_VideoResolution_4K-17-9.png")
	find ("CamSettings_Selected_VideoResolution_4K.png")
	find ("CamSettings_Selected_VideoResolution_720.png")
	find ("CamSettings_Selected_VideoResolution_720SuperView.png")
	find ("CamSettings_Selected_VideoResolution_960-1.png")
	find ("CamSettings_Selected_VideoResolution_960.png")
	find ("CamSettings_Selected_VideoResolution_WVGA.png")
	find ("CamSettings_SetFOV_CANCEL.png")
	find ("CamSettings_SetFOV_MEDIUM.png")
	find ("CamSettings_SetFOV_NARROW.png")
	find ("CamSettings_SetFOV_Title.png")
	find ("CamSettings_SetFOV_WIDE.png")
	find ("CamSettings_SetFPS_100.png")
	find ("CamSettings_SetFPS_12.png")
	find ("CamSettings_SetFPS_120.png")
	find ("CamSettings_SetFPS_15.png")
	find ("CamSettings_SetFPS_24.png")
	find ("CamSettings_SetFPS_240.png")
	find ("CamSettings_SetFPS_30.png")
	find ("CamSettings_SetFPS_48.png")
	find ("CamSettings_SetFPS_60.png")
	find ("CamSettings_SetFPS_Title.png")
	find ("CamSettings_SetVideoRes_1080.png")
	find ("CamSettings_SetVideoRes_1080SuperView.png")
	find ("CamSettings_SetVideoRes_1440.png")
	find ("CamSettings_SetVideoRes_27K-17-9.png")
	find ("CamSettings_SetVideoRes_27K.png")
	find ("CamSettings_SetVideoRes_4K-17-9.png")
	find ("CamSettings_SetVideoRes_4k.png")
	find ("CamSettings_SetVideoRes_720.png")
	find ("CamSettings_SetVideoRes_720SuperView.png")
	find ("CamSettings_SetVideoRes_960.png")
	find ("CamSettings_SetVideoRes_Cancel.png")
	find ("CamSettings_SetVideoRes_Title.png")
	find ("CamSettings_SetVideoRes_WVGA.png")
	find ("CamSettings__Button_VideoResolution.png")
	find ("global_vncregion_title.png")
	find ("HardwareButtons.png")
	find ("Main_IsConnected.png")
	find ("Main_MyGoProAlbum.png")
	find ("Main_PhotoOfTheDay.png")
	find ("Main_Setting.png")
	find ("Main_ShopCart.png")
	find ("Main_VideoOfTheDay.png")
	find ("Settings_Button_About.png")
	find ("Settings_Button_AutoDownload_ON-1.png")
	find ("Settings_Button_AutoDownload_ON.png")
	find ("Settings_Button_CameraLog.png")
	find ("Settings_Button_CameraModels.png")
	find ("Settings_Button_CameraStub_OFF.png")
	find ("Settings_Button_CameraStub_ON.png")
	find ("Settings_Button_CellularData_OFF.png")
	find ("Settings_Button_CellularData_ON.png")
	find ("Settings_Button_FirmwareDL.png")
	find ("Settings_Button_OtaLog.png")
	find ("Settings_Button_OtaSourceType.png")
	find ("Settings_Button_OtaStagingURL.png")
	find ("Settings_Button_PreviewPlayer.png")
	find ("Settings_Button_SendLTPKeepalive_OFF.png")
	find ("Settings_Button_SendLTPKeepalive_ON.png")
	find ("Settings_Label_TestAndDebug.png")
	find ("Settings_Label_Version.png")
	find ("Settings_Title.png")
	find ("Smarty_App_Logo.png")
	find ("SystemMenu.png")
	find ("SystemMenu_Search.png")
	find ("SystemSearch_Icon_GoPro.png")
	find ("TextBox_SystemSearch.png")

####################################################################################
#END Framework Images
####################################################################################

