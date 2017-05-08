import sys, os, re, time, traceback
import datetime as dt
import msaa
import comtypes.client
import win32api, win32con
import win32gui
import win32ui
import xmltodict, json
#import cPickle
import sys
import xmltodict

reload(sys)
#sys.setdefaultencoding('utf8')


gattribute = None
gvalue = None
gnode = None
def setTargetNode(attrib,value):
    global gattribute
    global gvalue
    global gnode
    gnode = None
    gattribute = attrib
    gvalue = value

def evalNodeAction(atrib, avalue, nnode):
    global gattribute
    global gvalue
    global gnode
    rc = False
    if not gattribute or not gvalue:
        return rc
    # if atrib=="AXTitle":
    #     print "%s|%s" % (gattribute,atrib)
    #     print "%s|%s" % (gvalue, avalue)
    if (str(gattribute) == str(atrib)) and (str(gvalue) in str(avalue)):
        gnode = nnode
        print "Action Node Found: %s=%s - %s" % (atrib, avalue, nnode)
        rc = True
    return rc

def evalNode(node, ui,parentattribute,z):
    print "%d=====================" % z
    act = node.accDefaultAction()
    if act:
        ui["action"] = act
    attlist = node.findall("window")
    if attlist:
        for i in range(len(attlist)):
            att = attlist[i]

            try:#nodes with lists
                if (parentattribute=="AXChildren" or parentattribute=="AXVisibleChildren") and (att == "AXChildren" or att == "AXVisibleChildren"):
                    ui[str(att)] = []
                    nlist=getattr(node, att)
                    print type(nlist)
                    for ii in range(len(nlist)):
                        try:
                            print type(nlist[ii])
                            attinfo = evalNode(nlist[ii], {},att,z+1)
                            if attinfo:
                                ui[str(att)].append(attinfo)
                        except Exception as err:
                            print "ERROR: %s" % err
                else:
                    try:
                        attinfo = getattr(node, att)
                        if attinfo:
                            if (type(attinfo) == atomac.NativeUIElement) and ("AXParent" not in att) and ("AXWindow" not in att) and ("AXTopLevelUIElement" not in att) and ("AXParent" not in str(type(attinfo))):
                                print "%s:type=%s" % (att,type(attinfo))
                                ui[str(att)]=evalNode(attinfo, {},att,z+1)
                            else:
                                ui[str(att)] = str(attinfo)
                                if evalNodeAction(str(att),str(attinfo),node):
                                    ui["Invoke"]=str(att)+"|"+str(attinfo)
                                    print "Set action node"
                            print "%s:%s=%s" % (type(attinfo),str(att), str(attinfo))
                    except Exception as err:
                        print "ERROR: %s" % err
                        ui[str(att)]="ERROR: %s" % err

            except:
                pass


    return ui

def pressbutton(press_button):
    if press_button:
        print "PRESS BUTTON==================="
        button_pos = press_button.AXPosition
        button_sz = press_button.AXSize
        x = button_pos[0]+(button_sz[0]/2)
        y = button_pos[1]+(button_sz[1]/2)

        print button_pos
        center=()
        center=center+(x,)
        center = center + (y,)
        print  center
        press_button.clickMouseButtonLeft(center)
        print "=============================="
        return True
    else:
        return False

def findwins(titlelist):
    rc = []  # or array
    for i in range(len(titlelist)):
        if msaa.window(titlelist[i]):
            rc.append(msaa.window(titlelist[i]))
    if len(rc) > 0:
        return rc
    return None

def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def do_click(ct):
    l, t, w, h = ct.accLocation()
    print str(l) + "-" + str(t) + "-" + str(w) + "-" + str(h)
    x = l + int(w / 2)
    y = t + int(h / 2)
    print str(x) + "-" + str(y)
    click(x, y)

def evalresult(_ap,selectbtn):
    if not windowView(_ap, selectbtn):
        print "######################"
        print "FAILED: %s" % selectbtn
        print "######################"
        exit(-1)

def evalselect(selectattr,selectval):
    rc=None
    if selectattr:
        rc={}
        rc[selectattr]=selectval
    return rc


def teststep(_ap,screen,selecttype=None,selectattr=None,selectval=None,chkselect=True):
    global gnode,test
    time.sleep(2)
    testid = len(test)
    print "%d. TEST: %s ---------------------" % (testid,screen)
    print "Button Press: %s - %s" % (selecttype,selectval)
    time.sleep(2)

    attr = evalselect(selectattr, selectval)
    if attr:
        acc = _ap.find(selecttype, **attr)
    else:
        acc = _ap.find(selecttype)
    if acc:
        print acc
        try:
            do_click(acc)
            acc.accDoDefaultAction()
            print "PASSED  %s: %s - %s" % (screen, selecttype, selectval)
        except:
            print "FAILED ACTION  %s: %s - %s" % (screen, selecttype, selectval)
    else:
        print "FAILED NOT FOUND %s: %s - %s" % (screen, selecttype, selectval)
        acc = _ap.findall(selecttype)
        print acc
# Installer start ===================================
installerdir="C:\Users\keith\Downloads\\"
installername="GoPro Quik-WinInstaller-2.3.0.5166.exe"
installerpath=installerdir+installername
wintitles=["Quik","Quik Installer"] #popups are detatched from Quik installler process
title_quickinstaller=0
title_popup=1
#win = msaa.window(wintitles[title_quickinstaller])
AutoItX = comtypes.client.CreateObject('AutoItX3.Control')
if not AutoItX:
    print "AutoItX"
    exit(1)
# kill all instances of the quik installer
proc=AutoItX.ProcessExists(installername)
while proc <> 0:
    AutoItX.ProcessClose(installername)
    proc=AutoItX.ProcessExists(installername)
    time.sleep(2)


app = None
os.startfile(installerpath)  #Installer
for i in range(10): #to support the slow macs
    time.sleep(2)
    app = msaa.window(wintitles[title_quickinstaller])
    if app:
        break


if not app:
    print "Installer not found"
    exit(-1)

# BEGIN TEST RUN
ap = app
if not ap:
    print "Installer Window not found:%s" % wintitles[title_quickinstaller]
    exit(-1)
if ap.accChildCount()<1:
    print "Installer Window has no child accessability objects:%d" % win.accChildCount()
    exit(-1)
test=[]
#infinate recursion with menus
#teststep(app.AXChildren[1],"Menus",None,None, False)
teststep(ap,"Welcome","PushButton","Name","Next")
#teststep(ap,"License","PushButton","Name","Back") # no accessable "Back button
#teststep(ap,"Welcome","PushButton","Name","Next")
teststep(ap,"License","CheckBox","State","focusable")
teststep(ap,"License","PushButton","Name","Next")

teststep(ap,"Important_info","AXTitle","Print")
teststep(ap,"Important_info-printer_info","AXTitle","Show Details")
teststep(ap,"Important_info-printer_info-details","AXTitle","Hide Details")
teststep(ap,"Important_info-printer_info","AXTitle","Cancel")
#teststep(ap,"Important_info","AXTitle","Save")
#teststep(ap,"Important_info-Save_popup_info","AXTitle","Cancel")
teststep(ap,"Important_info","AXTitle","Continue")
teststep(ap,"Software_Agreement","AXTitle","Print")
teststep(ap,"Software_Agreement-Printer_info","AXTitle","Show Details")
teststep(ap,"Software_Agreement-Printer_info-details","AXTitle","Hide Details")
teststep(ap,"Software_Agreement-Printer_info","AXTitle","Cancel")
#teststep(ap,"Software_Agreement","AXTitle","Save")
#teststep(ap,"Software_Agreement-Save_popup_info","AXTitle","Cancel")
teststep(ap,"Software_Agreement","AXTitle","Continue")
teststep(ap,"popup_continue_agree_disagree","AXTitle","Read License")
teststep(ap,"Software_Agreement","AXTitle","Continue")
teststep(ap,"popup_continue_agree_disagree","AXTitle","Agree")
teststep(ap,"Standard_Install","AXTitle","Change Install Location")
teststep(ap,"Select_Destination","AXTitle","Continue")
time.sleep(4)
teststep(ap,"Standard_Install","AXTitle","Install")
time.sleep(4)
isdone=False

for w in range(10):
    time.sleep(4)
    if not teststep(ap,"Wait_for_installer_finish","AXTitle","Close", False):
        print "%d. waiting for installer" % w

    else:
        isdone=True
        break
    testpath="/Automation/pywininstaller/WinInstallerTestRun.json"
    with open(testpath, 'w') as fp:
        json.dump(test, fp)
if not isdone:
    print "FAILED Installer copy/configure processs"
    print "Final Installer window is not found"
    exit(-2) # set non zero exit code
