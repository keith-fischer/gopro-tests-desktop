#import ctypes
import sys, os, re, time, traceback
import datetime as dt
import msaa
import comtypes.client
import win32api, win32con
import win32gui
import win32ui


def pkill(process_name):
    try:
        killed = os.system('tskill ' + process_name)
    except Exception, e:
        killed = 0
    return killed

def screenshot(imgpath,windtitle):
    rc = False
    try:
        hwnd = win32gui.FindWindow(None, windtitle)
        if not hwnd:
            return False

        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        wDC = win32gui.GetWindowDC(hwnd)
        dcObj = win32ui.CreateDCFromHandle(wDC)
        cDC = dcObj.CreateCompatibleDC()
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (w, h), dcObj, (0, 0), win32con.SRCCOPY)
        dataBitMap.SaveBitmapFile(cDC, imgpath)
        # Free Resources
        dcObj.DeleteDC()
        cDC.DeleteDC()
        win32gui.ReleaseDC(hwnd, wDC)
        win32gui.DeleteObject(dataBitMap.GetHandle())
        rc = True

    except:
        print "FAILED: Screenshot"
    return rc

def click(x, y):
    try:
        win32api.SetCursorPos((x, y))
    except:
        print "Failed: win32api.SetCursorPos:" + str(x)+"-"+str(y)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def msaawin(title):
    win = None
    try:
        win = msaa.window(title)
        if win:
            print "Found Window:" + title
    except:
        print "Window Not found:"+title
    return win


def winfind(win, cttype, ctname):
    ct = None
    try:
        ct = win.find(cttype, Name=ctname)
        if ct:
            print "Found Control:" + cttype + "-" + ctname
    except:
        print "Not Found Control:" + cttype + "-" + ctname
    return ct
# LONG = ctypes.c_long
# DWORD = ctypes.c_ulong
# ULONG_PTR = ctypes.POINTER(DWORD)
# WORD = ctypes.c_ushort
#
# class MOUSEINPUT(ctypes.Structure):
#     _fields_ = (('dx', LONG),
#                 ('dy', LONG),
#                 ('mouseData', DWORD),
#                 ('dwFlags', DWORD),
#                 ('time', DWORD),
#                 ('dwExtraInfo', ULONG_PTR))
# class KEYBDINPUT(ctypes.Structure):
#     _fields_ = (('wVk', WORD),
#                 ('wScan', WORD),
#                 ('dwFlags', DWORD),
#                 ('time', DWORD),
#                 ('dwExtraInfo', ULONG_PTR))
#
# class HARDWAREINPUT(ctypes.Structure):
#     _fields_ = (('uMsg', DWORD),
#                 ('wParamL', WORD),
#                 ('wParamH', WORD))
#
# class _INPUTunion(ctypes.Union):
#     _fields_ = (('mi', MOUSEINPUT),
#                 ('ki', KEYBDINPUT),
#                 ('hi', HARDWAREINPUT))
# class INPUT(ctypes.Structure):
#     _fields_ = (('type', DWORD),
#                 ('union', _INPUTunion))
#
# def SendInput(*inputs):
#     nInputs = len(inputs)
#     LPINPUT = INPUT * nInputs
#     pInputs = LPINPUT(*inputs)
#     cbSize = ctypes.c_int(ctypes.sizeof(INPUT))
#     return ctypes.windll.user32.SendInput(nInputs, pInputs, cbSize)
#
# INPUT_MOUSE = 0
# INPUT_KEYBOARD = 1
# INPUT_HARDWARE = 2
#
# def Input(structure):
#     if isinstance(structure, MOUSEINPUT):
#         return INPUT(INPUT_MOUSE, _INPUTunion(mi=structure))
#     if isinstance(structure, KEYBDINPUT):
#         return INPUT(INPUT_KEYBOARD, _INPUTunion(ki=structure))
#     if isinstance(structure, HARDWAREINPUT):
#         return INPUT(INPUT_HARDWARE, _INPUTunion(hi=structure))
#     raise TypeError('Cannot create INPUT structure!')
#
# WHEEL_DELTA = 120
# XBUTTON1 = 0x0001
# XBUTTON2 = 0x0002
# MOUSEEVENTF_ABSOLUTE = 0x8000
# MOUSEEVENTF_HWHEEL = 0x01000
# MOUSEEVENTF_MOVE = 0x0001
# MOUSEEVENTF_MOVE_NOCOALESCE = 0x2000
# MOUSEEVENTF_LEFTDOWN = 0x0002
# MOUSEEVENTF_LEFTUP = 0x0004
# MOUSEEVENTF_RIGHTDOWN = 0x0008
# MOUSEEVENTF_RIGHTUP = 0x0010
# MOUSEEVENTF_MIDDLEDOWN = 0x0020
# MOUSEEVENTF_MIDDLEUP = 0x0040
# MOUSEEVENTF_VIRTUALDESK = 0x4000
# MOUSEEVENTF_WHEEL = 0x0800
# MOUSEEVENTF_XDOWN = 0x0080
# MOUSEEVENTF_XUP = 0x0100
# def MouseInput(flags, x, y, data):
#     return MOUSEINPUT(x, y, data, flags, 0, None)
#
# def Mouse(flags, x=0, y=0, data=0):
#     return Input(MouseInput(flags, x, y, data))

########################################

AutoItX = comtypes.client.CreateObject('AutoItX3.Control')
if not AutoItX:
    print "AutoItX"
    exit(1)


def do_click(ct):
    l, t, w, h = ct.accLocation()
    print str(l) + "-" + str(t) + "-" + str(w) + "-" + str(h)
    x = l + int(w / 2)
    y = t + int(h / 2)
    print str(x) + "-" + str(y)
    click(x, y)

class TestGoProInstaller():
    def setUp(self,installerpath):
        os.startfile(installerpath)
        time.sleep(3)

    def tearDown(self):
        AutoItX.WinClose('GoPro')

    # def do_click(self,ct):
    #     l, t, w, h = ct.accLocation()
    #     print str(l) + "-" + str(t) + "-" + str(w) + "-" + str(h)
    #     x = l + int(w/ 2)
    #     y = t + int(h / 2)
    #     print str(x) + "-" + str(y)
    #     click(x, y)

    def testinstall(self):
        sys.stdout.flush()
        imgpath="C:\\Win_GDA-Studio_3a_BAT\\temp\\"
        rc = False
        time.sleep(2)
        win = msaawin('GoPro')
        if not win:
            return rc
        print "Found Installer window"
        screenshot(imgpath+"installerwelcome.png", "GoPro")
        #print win.toxml()
        ct = win.find('PushButton', Name='Next')

        ct.accDoDefaultAction()
        time.sleep(2)

        win = msaawin('GoPro')
        if not win:
            return rc
        screenshot(imgpath+"installeragreement.png", "GoPro")
        #print win.toxml()
        ct = win.find('CheckBox', Name='I accept the terms of the License Agreement')
        if ct:
            time.sleep(1)
            do_click(ct)
            time.sleep(1)
            ct = win.find('PushButton', Name='Next')
            ct.accDoDefaultAction()
        else:
            print "Failed:win.find('CheckBox', Name='I accept the terms of the License Agreement')"
            return rc
        time.sleep(3)
        win = msaawin('GoPro')
        if not win:
            return rc

        #print win.toxml()
        screenshot(imgpath+"installerlocation.png", "GoPro")
        ct = win.find('PushButton', Name='Install')
        if not ct:
            print "Failed: pushbutton Install not found"
            return rc
        ct.accDoDefaultAction()
        time.sleep(2)
        win = msaawin('GoPro')
        if not win:
            return rc
        screenshot(imgpath+"installerprogress.png", "GoPro")
        #print win.toxml()
        for i in range(1, 99):
            sys.stdout.flush()
            win = msaawin('GoPro')
            if win:
                time.sleep(5)
                ct = winfind(win, 'PushButton', 'Finish')
                #ct = win.find('PushButton', Name='Finish')
                if ct:
                    screenshot(imgpath+"InstallerFinished.png", "GoPro")
                    #print win.toxml()
                    #do_click(ct)
                    ct.accDoDefaultAction()
                    rc = True
                    break
                else:
                    print str(i) + ". Pushbutton waiting"
                    time.sleep(5)
            else:
                print str(i) + ". waiting"
                time.sleep(1)
        if not rc:
            print "FAILED Install: Timeout"
            AutoItX.WinClose('GoPro')

        return rc

class TestGoProUnInstaller():
    def setUp(self, installerpath):
        os.startfile(installerpath)

    def uninstall(self):
        sys.stdout.flush()
        rc = False
        time.sleep(3)
        win = msaawin('GoPro Uninstaller')
        if not win:
            print "Uninstaller not found"
            #AutoItX.WinClose('GoPro')
            return rc
        print "Found uninstaller"
        screenshot("C:\\Win_GDA-Studio_3a_BAT\\temp\\uninstall1.png", "GoPro Uninstaller")
        #print win.toxml()
        ct = win.find('PushButton', Name='Yes')
        if not ct:
            print "Uninstall button Yes not found"
            return rc
        ct.accDoDefaultAction()
        #progress window -------------------------
        time.sleep(5)
        try:
            win = msaa.window('GoPro')
        except:
            print "Error Uninstaller progress not found"
            AutoItX.WinClose('GoPro')
            return rc
        if not win:
            print "Uninstall GoPro progress window not found"
            AutoItX.WinClose('GoPro')
            return rc

        screenshot("C:\\Win_GDA-Studio_3a_BAT\\temp\\uninstall2.png", "GoPro")
        #print win.toxml()
        time.sleep(3)
        # wait for uninstaller finished window -------------------------
        win = None
        for i in range(1, 99):
            sys.stdout.flush()
            try:
                win = msaa.window('GoPro Uninstall')
            except:
                win = None

            if win:
                print "found uninstall window"
                ct = win.find('PushButton', Name='OK')
                if ct:
                    screenshot("C:\\Win_GDA-Studio_3a_BAT\\temp\\uninstall3.png", "GoPro Uninstaller")
                    #print win.toxml()
                    ct.accDoDefaultAction()
                    rc = True
                    break
                else:
                    print str(i) + ". PushButton waiting"
                    time.sleep(1)
            else:
                print str(i) + ". waiting"
                time.sleep(1)
        if not rc:
            print "FAILED Uninstaller: Timeout"
            if AutoItX:
                AutoItX.WinClose('GoPro')
        return rc

    def tearDown(self):
        if AutoItX:
            AutoItX.WinClose('GoPro')

class TestGoProApp():
    def testgopro(self):
        sys.stdout.flush()
        rc = False
        time.sleep(10)
        win = None
        try:
            win = msaa.window('GoPro')
        except:
            if AutoItX:
                AutoItX.WinClose('GoPro')
            return rc
        if not win:
            return rc
        rc = True
        screenshot("C:\\Win_GDA-Studio_3a_BAT\\temp\\GDA1.png", "GoPro")
        #print win.toxml()
        return rc
        #ct = win.find('PushButton', Name='Next')

def eval_GDAversion(gdapath): #GoPro-WinInstaller-2.0.0.2099.exe
    installername = "Gopro-Wininstaller-"
    gda = os.path.basename(gdapath)
    print gda
    gda = gda.replace(installername, "")
    gda = gda.replace(".exe", "")
    glist = gda.split(".")
    print str(glist)
    gdanum = glist[0]+glist[1]+glist[2]+"."+glist[3]
    if not "GoPro".lower() in gdanum.lower():
        print "Found Installer version"
        return gda, float(gdanum)
    else:
        print "GDA installer file name has changed"
        return gda, float(0)

def dt_now():
    datet = dt.datetime.now()
    print str(datet)
    return datet

def datediff_secs(dt1,dt2):
    nn = (dt2 - dt1).total_seconds()
    print nn
    return nn


def findLatestInstallerFromJenkinsAndCleanup(jenkinspath, _now):
    print"findLatestInstallerFromJenkinsAndCleanup>>>"
    #GoPro-WinInstaller-2.0.0.2099.exe
    installername = "Gopro-Wininstaller"
    if not os.path.isdir(jenkinspath):
        print "Error: invalid jenkins directory for build installers"
        return ""
    fullpath = selectpath = None
    secmin = 999999999
    for root, dirs, filenames in os.walk(jenkinspath):
        sys.stdout.flush()
        for f in filenames:
            print str(f.title().find(installername))+f.title()
            if f.title().find(installername) < 0:
                print "not installer"
                continue

            fullpath = os.path.join(jenkinspath, f.title())
            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(fullpath)
            dt1 = os.path.getmtime(fullpath)
            dt1 = dt.datetime.fromtimestamp(dt1)
            sectotal = datediff_secs(dt1, _now)
            print str(sectotal) + "  " + f.title()
            if sectotal < secmin:
                secmin = sectotal
                selectpath = fullpath

    #delete all but the target file
    if selectpath:
        for root, dirs, filenames in os.walk(jenkinspath):
            sys.stdout.flush()
            for f in filenames:
                if f.title().find(installername) < 0:
                    continue
                fullpath = os.path.join(jenkinspath, f.title())
                if fullpath != selectpath:
                    try:
                        os.remove(fullpath)
                    except:
                        print "Failed to delete old installer"
                        try:
                            pkill(f.title()) #try to kill stuck installer process
                        except:
                            print "Failed to kill installer process:"+f.title()
                        return None
                    print "Cleanup:" + fullpath
                else:
                    print "Target File:"+fullpath
    print"findLatestInstallerFromJenkinsAndCleanup<<<<<<"
    return selectpath

# script start ================================

_now = dt_now()

installerpath = 'C:\\Win_GDA-Studio_3a_BAT\\temp'
installerpath = findLatestInstallerFromJenkinsAndCleanup(installerpath, _now)
if not installerpath or not os.path.exists(installerpath):
    print "Using debug default installer path"
    #installerpath = 'C:\\Win_GDA-Studio_3a_BAT\\temp\\GoPro-WinInstaller-2.0.0.2099.exe'
if not os.path.exists(installerpath):
    print "Error: Windows GDA installer not found"
    exit(1)
version, vernum = eval_GDAversion(installerpath)
print version
print str(vernum)
if vernum < 1:
    print "Failed: Invalid version number"
    exit(1)

#try unistaller
tc = TestGoProUnInstaller()
tc.setUp(installerpath)
uninstall = tc.uninstall()
if not uninstall:
     print "Uninstall not found"
     #tc.tearDown()
else:
     print "Unistalled GDA Completed"
tc = TestGoProInstaller()
if uninstall:
    tc.setUp(installerpath)
#installer app should be running now
if not tc.testinstall(): #return false if installer stuck
    print "Failed GDA Installer"
    tc.tearDown() #kill the installer app prccess
    exit(1)
else: #installer will auto exit
    tc = TestGoProApp()
    if tc.testgopro():
        exit(0)
    exit(1)
