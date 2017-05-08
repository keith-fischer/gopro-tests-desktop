import time
import atomac #works for accessability only on Mac
import json
#import cPickle
import sys
reload(sys)
sys.setdefaultencoding('utf8')


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
    act = node.getActions()
    if act:
        ui["action"] = act
    attlist = node.getAttributes()
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

def evalresult(_ap,selectbtn):
    if not windowView(_ap, selectbtn):
        print "######################"
        print "FAILED: %s" % selectbtn
        print "######################"
        exit(-1)


def teststep(_ap,screen,selecttype=None,selectval=None,chkselect=True):
    global gnode,test
    testid = len(test)
    print "%d. TEST: %s ---------------------" % (testid,screen)
    print "Button Press: %s - %s" % (selecttype,selectval)
    time.sleep(2)
    setTargetNode(selecttype, selectval)
    ui = evalNode(_ap, {}, "AXChildren", 1)
    if ui and len(ui):
        ui["TestResult"] = "Failed"
        ui["screen_name"] = screen
        ui["testid"] = testid
        if not selecttype or not selectval:
            ui["button_node"] = "N/A"
        else:
            if pressbutton(gnode):
                ui["TestResult"] = "Passed"
        test.append(ui)
        fname = "/Automation/pymacinstaller/test%d_%s.json" % (testid, screen)
        with open(fname, 'w') as fp:
            json.dump(ui, fp)

        if gnode:
            return True
        else:
            if not chkselect:
                return False
            else:
                print "Failed to select Button: %s %s=%s" % (screen, selecttype,selectval)
                exit(-3)

    else:
        print "FAILED: to get screen gui. No target window found"
        exit(-2)

time.sleep(2) # builtin wait for previous bash script to mount and start Installer
app = None
for i in range(10): #to support the slow macs
    app = atomac.getAppRefByBundleId('com.apple.installer')  #Installer
    if app:
        break
    time.sleep(2)

if not app:
    print "Installer not found"
    exit(-1)

# BEGIN TEST RUN

ap=app.AXChildren[0]
test=[]
#infinate recursion with menus
#teststep(app.AXChildren[1],"Menus",None,None, False)
teststep(ap,"Welcome","AXTitle","Continue")
teststep(ap,"Important_info","AXTitle","Go Back")
teststep(ap,"Welcome","AXTitle","Continue")
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
    testpath="/Automation/pymacinstaller/MacInstallerTestRun.json"
    with open(testpath, 'w') as fp:
        json.dump(test, fp)
if not isdone:
    print "FAILED Installer copy/configure processs"
    print "Final Installer window is not found"
    exit(-2) # set non zero exit code
