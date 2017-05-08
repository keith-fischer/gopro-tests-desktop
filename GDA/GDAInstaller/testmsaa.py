#import ctypes
import sys, os, re, time
import msaa
import comtypes.client
import win32api, win32con
import win32gui
import win32ui


def screenshot(imgpath,windtitle):
    hwnd = win32gui.FindWindow(None, windtitle)
    rect = win32gui.GetWindowRect(hwnd)
    x = rect[0]
    y = rect[1]
    w = rect[2] - x
    h = rect[3] - y
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj=win32ui.CreateDCFromHandle(wDC)
    cDC=dcObj.CreateCompatibleDC()
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, w, h)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0,0),(w, h) , dcObj, (0,0), win32con.SRCCOPY)
    dataBitMap.SaveBitmapFile(cDC, imgpath)
    # Free Resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())


def click(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

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
        rc = False
        time.sleep(2)
        win = None
        try:
            win = msaa.window('GoPro')
        except:
            #AutoItX.WinClose('GoPro')
            return rc
        if not win:
            return rc
        print "Found Installer window"
        screenshot("C:\\Win_GDA-Studio_3a_BAT\\temp\\img1.png", "GoPro")
        print win.toxml()
        ct = win.find('PushButton', Name='Next')

        ct.accDoDefaultAction()
        time.sleep(1)

        win = msaa.window('GoPro')
        screenshot("C:\\Win_GDA-Studio_3a_BAT\\temp\\img2.png", "GoPro")
        print win.toxml()
        ct = win.find('CheckBox', Name='I accept the terms of the License Agreement')
        if ct:
            time.sleep(1)
            do_click(ct)
            ct = win.find('PushButton', Name='Next')
            ct.accDoDefaultAction()

        time.sleep(1)
        win = msaa.window('GoPro')

        print win.toxml()
        screenshot("C:\\Win_GDA-Studio_3a_BAT\\temp\\img2.png", "GoPro")
        ct = win.find('PushButton', Name='Install')
        ct.accDoDefaultAction()
        time.sleep(2)
        win = msaa.window('GoPro')
        screenshot("C:\\Win_GDA-Studio_3a_BAT\\temp\\img3.png", "GoPro")
        print win.toxml()
        ctfound = False
        for i in range(1, 60):
            win = msaa.window('GoPro')
            ct = win.find('PushButton', Name='Finish')
            if ct:
                ctfound = True
                screenshot("C:\\Win_GDA-Studio_3a_BAT\\temp\\img4.png", "GoPro")
                print win.toxml()
                ct.accDoDefaultAction()
                rc = True
                return rc
            else:
                print "waiting"
                time.sleep(1)
        if not ctfound:
            print "FAILED Install: Timeout"
            AutoItX.WinClose('GoPro')
            return rc

class TestGoProUnInstaller():
    def setUp(self, installerpath):
        os.startfile(installerpath)

    def uninstall(self):
        rc = False
        time.sleep(3)
        win = None
        try:
            win = msaa.window('GoPro Uninstaller')
        except:
            print "Error Uninstaller"
            #AutoItX.WinClose('GoPro')
            return rc
        if not win:
            print "Uninstaller not found"
            #AutoItX.WinClose('GoPro')
            return rc
        print "Found uninstaller"
        screenshot("C:\\Win_GDA-Studio_3a_BAT\\temp\\img5.png", "GoPro")
        print win.toxml()
        ct = win.find('PushButton', Name='Yes')
        if not ct:
            print "Uninstall button Yes not found"
            return rc
        ct.accDoDefaultAction()

        time.sleep(3)
        win = msaa.window('GoPro')
        screenshot("C:\\Win_GDA-Studio_3a_BAT\\temp\\img6.png", "GoPro")
        print win.toxml()
        ct = win.find('PushButton', Name='Yes')
        ct.accDoDefaultAction()

        time.sleep(3)
        win = msaa.window('GoPro Uninstaller')
        screenshot("C:\\Win_GDA-Studio_3a_BAT\\temp\\img7.png", "GoPro")
        print win.toxml()
        ct = win.find('PushButton', Name='OK')
        ct.accDoDefaultAction()
        rc = True
        return rc

    def tearDown(self):
        AutoItX.WinClose('GoPro')

class TestGoProApp():
    def testgopro(self):
        rc = False
        time.sleep(10)
        win = None
        try:
            win = msaa.window('GoPro Uninstaller')
        except:
            AutoItX.WinClose('GoPro')
            return rc
        if not win:
            return rc
        screenshot("C:\\Win_GDA-Studio_3a_BAT\\temp\\img5.png", "GoPro")
        print win.toxml()
        return True
        #ct = win.find('PushButton', Name='Next')




installerpath = 'C:\\Win_GDA-Studio_3a_BAT\\temp\\GoPro-WinInstaller-2.0.0.2099.exe'
# tc = TestGoProUnInstaller()
# tc.setUp(installerpath)
# if not tc.uninstall():
#     print "Failed Uninstall"
#     tc.tearDown()
# else:
#     print "Unistalled GDA"
tc = TestGoProInstaller()
tc.setUp(installerpath)
if not tc.testinstall(): #return false if installer stuck
    tc.tearDown() #kill the installer app prccess
else:
    tc=TestGoProApp()
    tc.testgopro()
