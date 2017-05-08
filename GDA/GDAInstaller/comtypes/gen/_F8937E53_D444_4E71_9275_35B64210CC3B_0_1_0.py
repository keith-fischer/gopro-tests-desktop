# -*- coding: mbcs -*-
typelib_path = u'C:\\Program Files (x86)\\AutoIt3\\AutoItX\\AutoItX3.dll'
_lcid = 0 # change this if required
from ctypes import *
from comtypes import GUID
from comtypes import CoClass
import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0
from ctypes import HRESULT
from comtypes import BSTR
from comtypes.automation import VARIANT
from comtypes import helpstring
from comtypes import COMMETHOD
from comtypes import dispid
from comtypes.automation import VARIANT


class AutoItX3(CoClass):
    u'AutoItX3 Class'
    _reg_clsid_ = GUID('{1A671297-FA74-4422-80FA-6C5D8CE4DE04}')
    _idlflags_ = []
    _typelib_path_ = typelib_path
    _reg_typelib_ = ('{F8937E53-D444-4E71-9275-35B64210CC3B}', 1, 0)
class IAutoItX3(comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0.IDispatch):
    _case_insensitive_ = True
    u'IAutoItX3 Interface'
    _iid_ = GUID('{3D54C6B8-D283-40E0-8FAB-C97F05947EE8}')
    _idlflags_ = ['dual', 'nonextensible', 'oleautomation']
AutoItX3._com_interfaces_ = [IAutoItX3]

IAutoItX3._methods_ = [
    COMMETHOD([dispid(1), helpstring(u'property error'), 'propget'], HRESULT, 'error',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(2), helpstring(u'property SW_HIDE'), 'propget'], HRESULT, 'SW_HIDE',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(3), helpstring(u'property SW_MAXIMIZE'), 'propget'], HRESULT, 'SW_MAXIMIZE',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(4), helpstring(u'property SW_MINIMIZE'), 'propget'], HRESULT, 'SW_MINIMIZE',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(5), helpstring(u'property SW_RESTORE'), 'propget'], HRESULT, 'SW_RESTORE',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(6), helpstring(u'property SW_SHOW'), 'propget'], HRESULT, 'SW_SHOW',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(7), helpstring(u'property SW_SHOWDEFAULT'), 'propget'], HRESULT, 'SW_SHOWDEFAULT',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(8), helpstring(u'property SW_SHOWMAXIMIZED'), 'propget'], HRESULT, 'SW_SHOWMAXIMIZED',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(9), helpstring(u'property SW_SHOWMINIMIZED'), 'propget'], HRESULT, 'SW_SHOWMINIMIZED',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(10), helpstring(u'property SW_SHOWMINNOACTIVE'), 'propget'], HRESULT, 'SW_SHOWMINNOACTIVE',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(11), helpstring(u'property SW_SHOWNA'), 'propget'], HRESULT, 'SW_SHOWNA',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(12), helpstring(u'property SW_SHOWNOACTIVATE'), 'propget'], HRESULT, 'SW_SHOWNOACTIVATE',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(13), helpstring(u'property SW_SHOWNORMAL'), 'propget'], HRESULT, 'SW_SHOWNORMAL',
              ( ['retval', 'out'], POINTER(c_int), 'pVal' )),
    COMMETHOD([dispid(14), helpstring(u'method Init')], HRESULT, 'Init'),
    COMMETHOD([dispid(15), helpstring(u'method AutoItSetOption')], HRESULT, 'AutoItSetOption',
              ( ['in'], BSTR, 'strOption' ),
              ( ['in'], c_int, 'nValue' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(18), helpstring(u'method ClipGet')], HRESULT, 'ClipGet',
              ( ['retval', 'out'], POINTER(BSTR), 'strClip' )),
    COMMETHOD([dispid(19), helpstring(u'method ClipPut')], HRESULT, 'ClipPut',
              ( ['in'], BSTR, 'strClip' )),
    COMMETHOD([dispid(20), helpstring(u'method ControlClick')], HRESULT, 'ControlClick',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['in', 'optional'], BSTR, 'strButton', u'LEFT' ),
              ( ['in', 'optional'], c_int, 'nNumClicks', 1 ),
              ( ['in', 'optional'], c_int, 'nX', -2147483647 ),
              ( ['in', 'optional'], c_int, 'nY', -2147483647 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(21), helpstring(u'method ControlCommand')], HRESULT, 'ControlCommand',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['in'], BSTR, 'strCommand' ),
              ( ['in'], BSTR, 'strExtra' ),
              ( ['retval', 'out'], POINTER(BSTR), 'strResult' )),
    COMMETHOD([dispid(22), helpstring(u'method ControlDisable')], HRESULT, 'ControlDisable',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(23), helpstring(u'method ControlEnable')], HRESULT, 'ControlEnable',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(24), helpstring(u'method ControlFocus')], HRESULT, 'ControlFocus',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(25), helpstring(u'method ControlGetFocus')], HRESULT, 'ControlGetFocus',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(BSTR), 'strControlWithFocus' )),
    COMMETHOD([dispid(26), helpstring(u'method ControlGetHandle')], HRESULT, 'ControlGetHandle',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['retval', 'out'], POINTER(BSTR), 'strRetText' )),
    COMMETHOD([dispid(27), helpstring(u'method ControlGetPosX')], HRESULT, 'ControlGetPosX',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(28), helpstring(u'method ControlGetPosY')], HRESULT, 'ControlGetPosY',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(29), helpstring(u'method ControlGetPosHeight')], HRESULT, 'ControlGetPosHeight',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(30), helpstring(u'method ControlGetPosWidth')], HRESULT, 'ControlGetPosWidth',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(31), helpstring(u'method ControlGetText')], HRESULT, 'ControlGetText',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['retval', 'out'], POINTER(BSTR), 'strControlText' )),
    COMMETHOD([dispid(32), helpstring(u'method ControlHide')], HRESULT, 'ControlHide',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(33), helpstring(u'method ControlListView')], HRESULT, 'ControlListView',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['in'], BSTR, 'strCommand' ),
              ( ['in'], BSTR, 'strExtra1' ),
              ( ['in'], BSTR, 'strExtra2' ),
              ( ['retval', 'out'], POINTER(BSTR), 'strResult' )),
    COMMETHOD([dispid(34), helpstring(u'method ControlMove')], HRESULT, 'ControlMove',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['in'], c_int, 'nX' ),
              ( ['in'], c_int, 'nY' ),
              ( ['in', 'optional'], c_int, 'nWidth', -1 ),
              ( ['in', 'optional'], c_int, 'nHeight', -1 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(35), helpstring(u'method ControlSend')], HRESULT, 'ControlSend',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['in'], BSTR, 'strSendText' ),
              ( ['in', 'optional'], c_int, 'nMode', 0 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(36), helpstring(u'method ControlSetText')], HRESULT, 'ControlSetText',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['in'], BSTR, 'strControlText' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(37), helpstring(u'method ControlShow')], HRESULT, 'ControlShow',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(38), helpstring(u'method ControlTreeView')], HRESULT, 'ControlTreeView',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strControl' ),
              ( ['in'], BSTR, 'strCommand' ),
              ( ['in'], BSTR, 'strExtra1' ),
              ( ['in'], BSTR, 'strExtra2' ),
              ( ['retval', 'out'], POINTER(BSTR), 'strResult' )),
    COMMETHOD([dispid(39), helpstring(u'method DriveMapAdd')], HRESULT, 'DriveMapAdd',
              ( ['in'], BSTR, 'strDevice' ),
              ( ['in'], BSTR, 'strShare' ),
              ( ['in', 'optional'], c_int, 'nFlags', 0 ),
              ( ['in', 'optional'], BSTR, 'strUser', u'' ),
              ( ['in', 'optional'], BSTR, 'strPwd', u'' ),
              ( ['retval', 'out'], POINTER(BSTR), 'strResult' )),
    COMMETHOD([dispid(40), helpstring(u'method DriveMapDel')], HRESULT, 'DriveMapDel',
              ( ['in'], BSTR, 'strDevice' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(41), helpstring(u'method DriveMapGet')], HRESULT, 'DriveMapGet',
              ( ['in'], BSTR, 'strDevice' ),
              ( ['retval', 'out'], POINTER(BSTR), 'strMapping' )),
    COMMETHOD([dispid(45), helpstring(u'method IsAdmin')], HRESULT, 'IsAdmin',
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(46), helpstring(u'method MouseClick')], HRESULT, 'MouseClick',
              ( ['in', 'optional'], BSTR, 'strButton', u'LEFT' ),
              ( ['in', 'optional'], c_int, 'nX', -2147483647 ),
              ( ['in', 'optional'], c_int, 'nY', -2147483647 ),
              ( ['in', 'optional'], c_int, 'nClicks', 1 ),
              ( ['in', 'optional'], c_int, 'nSpeed', -1 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(47), helpstring(u'method MouseClickDrag')], HRESULT, 'MouseClickDrag',
              ( ['in'], BSTR, 'strButton' ),
              ( ['in'], c_int, 'nX1' ),
              ( ['in'], c_int, 'nY1' ),
              ( ['in'], c_int, 'nX2' ),
              ( ['in'], c_int, 'nY2' ),
              ( ['in', 'optional'], c_int, 'nSpeed', -1 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(48), helpstring(u'method MouseDown')], HRESULT, 'MouseDown',
              ( ['in', 'optional'], BSTR, 'strButton', u'LEFT' )),
    COMMETHOD([dispid(49), helpstring(u'method MouseGetCursor')], HRESULT, 'MouseGetCursor',
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(50), helpstring(u'method MouseGetPosX')], HRESULT, 'MouseGetPosX',
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(51), helpstring(u'method MouseGetPosY')], HRESULT, 'MouseGetPosY',
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(52), helpstring(u'method MouseMove')], HRESULT, 'MouseMove',
              ( ['in'], c_int, 'nX' ),
              ( ['in'], c_int, 'nY' ),
              ( ['in', 'optional'], c_int, 'nSpeed', -1 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(53), helpstring(u'method MouseUp')], HRESULT, 'MouseUp',
              ( ['in', 'optional'], BSTR, 'strButton', u'LEFT' )),
    COMMETHOD([dispid(54), helpstring(u'method MouseWheel')], HRESULT, 'MouseWheel',
              ( ['in'], BSTR, 'strDirection' ),
              ( ['in', 'optional'], c_int, 'nClicks', 1 )),
    COMMETHOD([dispid(55), helpstring(u'method Opt')], HRESULT, 'Opt',
              ( ['in'], BSTR, 'strOption' ),
              ( ['in'], c_int, 'nValue' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(56), helpstring(u'method PixelChecksum')], HRESULT, 'PixelChecksum',
              ( ['in'], c_int, 'nLeft' ),
              ( ['in'], c_int, 'nTop' ),
              ( ['in'], c_int, 'nRight' ),
              ( ['in'], c_int, 'nBottom' ),
              ( ['in', 'optional'], c_int, 'nStep', 1 ),
              ( ['retval', 'out'], POINTER(c_double), 'nRes' )),
    COMMETHOD([dispid(57), helpstring(u'method PixelGetColor')], HRESULT, 'PixelGetColor',
              ( ['in'], c_int, 'nX' ),
              ( ['in'], c_int, 'nY' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(58), helpstring(u'method PixelSearch')], HRESULT, 'PixelSearch',
              ( ['in'], c_int, 'nLeft' ),
              ( ['in'], c_int, 'nTop' ),
              ( ['in'], c_int, 'nRight' ),
              ( ['in'], c_int, 'nBottom' ),
              ( ['in'], c_int, 'nCol' ),
              ( ['in', 'optional'], c_int, 'nVar', 0 ),
              ( ['in', 'optional'], c_int, 'nStep', 1 ),
              ( ['retval', 'out'], POINTER(VARIANT), 'vOutResult' )),
    COMMETHOD([dispid(59), helpstring(u'method ProcessClose')], HRESULT, 'ProcessClose',
              ( ['in'], BSTR, 'strProcess' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(60), helpstring(u'method ProcessExists')], HRESULT, 'ProcessExists',
              ( ['in'], BSTR, 'strProcess' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(61), helpstring(u'method ProcessSetPriority')], HRESULT, 'ProcessSetPriority',
              ( ['in'], BSTR, 'strProcess' ),
              ( ['in'], c_int, 'nPriority' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(62), helpstring(u'method ProcessWait')], HRESULT, 'ProcessWait',
              ( ['in'], BSTR, 'strProcess' ),
              ( ['in', 'optional'], c_int, 'nTimeout', 0 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(63), helpstring(u'method ProcessWaitClose')], HRESULT, 'ProcessWaitClose',
              ( ['in'], BSTR, 'strProcess' ),
              ( ['in', 'optional'], c_int, 'nTimeout', 0 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(70), helpstring(u'method Run')], HRESULT, 'Run',
              ( ['in'], BSTR, 'strRun' ),
              ( ['in', 'optional'], BSTR, 'strDir', u'' ),
              ( ['in', 'optional'], c_int, 'nShowFlag', 13 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(71), helpstring(u'method RunAs')], HRESULT, 'RunAs',
              ( ['in'], BSTR, 'strUser' ),
              ( ['in'], BSTR, 'strDomain' ),
              ( ['in'], BSTR, 'strPassword' ),
              ( ['in'], c_int, 'nLogonFlag' ),
              ( ['in'], BSTR, 'strRun' ),
              ( ['in', 'optional'], BSTR, 'strDir', u'' ),
              ( ['in', 'optional'], c_int, 'nShowFlag', 13 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(64), helpstring(u'method RunAsWait')], HRESULT, 'RunAsWait',
              ( ['in'], BSTR, 'strUser' ),
              ( ['in'], BSTR, 'strDomain' ),
              ( ['in'], BSTR, 'strPassword' ),
              ( ['in'], c_int, 'nLogonFlag' ),
              ( ['in'], BSTR, 'strRun' ),
              ( ['in', 'optional'], BSTR, 'strDir', u'' ),
              ( ['in', 'optional'], c_int, 'nShowFlag', 13 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(72), helpstring(u'method RunWait')], HRESULT, 'RunWait',
              ( ['in'], BSTR, 'strRun' ),
              ( ['in', 'optional'], BSTR, 'strDir', u'' ),
              ( ['in', 'optional'], c_int, 'nShowFlag', 13 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(73), helpstring(u'method Send')], HRESULT, 'Send',
              ( ['in'], BSTR, 'strSendText' ),
              ( ['in', 'optional'], c_int, 'nMode', 0 )),
    COMMETHOD([dispid(74), helpstring(u'method Shutdown')], HRESULT, 'Shutdown',
              ( ['in'], c_int, 'nFlags' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(75), helpstring(u'method Sleep')], HRESULT, 'Sleep',
              ( ['in'], c_int, 'nMilliseconds' )),
    COMMETHOD([dispid(76), helpstring(u'method StatusbarGetText')], HRESULT, 'StatusbarGetText',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['in', 'optional'], c_int, 'nPart', 1 ),
              ( ['retval', 'out'], POINTER(BSTR), 'strStatusText' )),
    COMMETHOD([dispid(77), helpstring(u'method ToolTip')], HRESULT, 'ToolTip',
              ( ['in'], BSTR, 'strTip' ),
              ( ['in', 'optional'], c_int, 'nX', -2147483647 ),
              ( ['in', 'optional'], c_int, 'nY', -2147483647 )),
    COMMETHOD([dispid(78), helpstring(u'method WinActivate')], HRESULT, 'WinActivate',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' )),
    COMMETHOD([dispid(79), helpstring(u'method WinActive')], HRESULT, 'WinActive',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(80), helpstring(u'method WinClose')], HRESULT, 'WinClose',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(81), helpstring(u'method WinExists')], HRESULT, 'WinExists',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(82), helpstring(u'method WinGetCaretPosX')], HRESULT, 'WinGetCaretPosX',
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(83), helpstring(u'method WinGetCaretPosY')], HRESULT, 'WinGetCaretPosY',
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(84), helpstring(u'method WinGetClassList')], HRESULT, 'WinGetClassList',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(BSTR), 'strRetText' )),
    COMMETHOD([dispid(85), helpstring(u'method WinGetClientSizeHeight')], HRESULT, 'WinGetClientSizeHeight',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(86), helpstring(u'method WinGetClientSizeWidth')], HRESULT, 'WinGetClientSizeWidth',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(87), helpstring(u'method WinGetHandle')], HRESULT, 'WinGetHandle',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(BSTR), 'strRetText' )),
    COMMETHOD([dispid(88), helpstring(u'method WinGetPosX')], HRESULT, 'WinGetPosX',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(89), helpstring(u'method WinGetPosY')], HRESULT, 'WinGetPosY',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(90), helpstring(u'method WinGetPosHeight')], HRESULT, 'WinGetPosHeight',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(91), helpstring(u'method WinGetPosWidth')], HRESULT, 'WinGetPosWidth',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(92), helpstring(u'method WinGetProcess')], HRESULT, 'WinGetProcess',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(BSTR), 'strResult' )),
    COMMETHOD([dispid(93), helpstring(u'method WinGetState')], HRESULT, 'WinGetState',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(94), helpstring(u'method WinGetText')], HRESULT, 'WinGetText',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(BSTR), 'strRetText' )),
    COMMETHOD([dispid(95), helpstring(u'method WinGetTitle')], HRESULT, 'WinGetTitle',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(BSTR), 'strRetText' )),
    COMMETHOD([dispid(96), helpstring(u'method WinKill')], HRESULT, 'WinKill',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(97), helpstring(u'method WinList')], HRESULT, 'WinList',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['retval', 'out'], POINTER(VARIANT), 'vOutResult' )),
    COMMETHOD([dispid(98), helpstring(u'method WinMenuSelectItem')], HRESULT, 'WinMenuSelectItem',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strItem1' ),
              ( ['in', 'optional'], BSTR, 'strItem2', u'' ),
              ( ['in', 'optional'], BSTR, 'strItem3', u'' ),
              ( ['in', 'optional'], BSTR, 'strItem4', u'' ),
              ( ['in', 'optional'], BSTR, 'strItem5', u'' ),
              ( ['in', 'optional'], BSTR, 'strItem6', u'' ),
              ( ['in', 'optional'], BSTR, 'strItem7', u'' ),
              ( ['in', 'optional'], BSTR, 'strItem8', u'' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(99), helpstring(u'method WinMinimizeAll')], HRESULT, 'WinMinimizeAll'),
    COMMETHOD([dispid(100), helpstring(u'method WinMinimizeAllUndo')], HRESULT, 'WinMinimizeAllUndo'),
    COMMETHOD([dispid(101), helpstring(u'method WinMove')], HRESULT, 'WinMove',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], c_int, 'nX' ),
              ( ['in'], c_int, 'nY' ),
              ( ['in', 'optional'], c_int, 'nWidth', -1 ),
              ( ['in', 'optional'], c_int, 'nHeight', -1 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(102), helpstring(u'method WinSetOnTop')], HRESULT, 'WinSetOnTop',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], c_int, 'nFlag' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(103), helpstring(u'method WinSetState')], HRESULT, 'WinSetState',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], c_int, 'nFlags' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(104), helpstring(u'method WinSetTitle')], HRESULT, 'WinSetTitle',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], BSTR, 'strNewTitle' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(105), helpstring(u'method WinSetTrans')], HRESULT, 'WinSetTrans',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in'], BSTR, 'strText' ),
              ( ['in'], c_int, 'nTrans' ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(106), helpstring(u'method WinWait')], HRESULT, 'WinWait',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['in', 'optional'], c_int, 'nTimeout', 0 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(107), helpstring(u'method WinWaitActive')], HRESULT, 'WinWaitActive',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['in', 'optional'], c_int, 'nTimeout', 0 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(108), helpstring(u'method WinWaitClose')], HRESULT, 'WinWaitClose',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['in', 'optional'], c_int, 'nTimeout', 0 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(109), helpstring(u'method WinWaitNotActive')], HRESULT, 'WinWaitNotActive',
              ( ['in'], BSTR, 'strTitle' ),
              ( ['in', 'optional'], BSTR, 'strText', u'' ),
              ( ['in', 'optional'], c_int, 'nTimeout', 0 ),
              ( ['retval', 'out'], POINTER(c_int), 'nRes' )),
    COMMETHOD([dispid(110), helpstring(u'property version'), 'propget'], HRESULT, 'version',
              ( ['retval', 'out'], POINTER(BSTR), 'strRetVer' )),
]
################################################################
## code template for IAutoItX3 implementation
##class IAutoItX3_Impl(object):
##    def WinSetOnTop(self, strTitle, strText, nFlag):
##        u'method WinSetOnTop'
##        #return nRes
##
##    def WinGetPosHeight(self, strTitle, strText):
##        u'method WinGetPosHeight'
##        #return nRes
##
##    def RunAsWait(self, strUser, strDomain, strPassword, nLogonFlag, strRun, strDir, nShowFlag):
##        u'method RunAsWait'
##        #return nRes
##
##    def ControlListView(self, strTitle, strText, strControl, strCommand, strExtra1, strExtra2):
##        u'method ControlListView'
##        #return strResult
##
##    def Opt(self, strOption, nValue):
##        u'method Opt'
##        #return nRes
##
##    def WinGetClassList(self, strTitle, strText):
##        u'method WinGetClassList'
##        #return strRetText
##
##    def WinMinimizeAllUndo(self):
##        u'method WinMinimizeAllUndo'
##        #return 
##
##    def ControlGetPosY(self, strTitle, strText, strControl):
##        u'method ControlGetPosY'
##        #return nRes
##
##    def ControlGetPosX(self, strTitle, strText, strControl):
##        u'method ControlGetPosX'
##        #return nRes
##
##    @property
##    def SW_MAXIMIZE(self):
##        u'property SW_MAXIMIZE'
##        #return pVal
##
##    def MouseClick(self, strButton, nX, nY, nClicks, nSpeed):
##        u'method MouseClick'
##        #return nRes
##
##    def ControlCommand(self, strTitle, strText, strControl, strCommand, strExtra):
##        u'method ControlCommand'
##        #return strResult
##
##    def WinGetTitle(self, strTitle, strText):
##        u'method WinGetTitle'
##        #return strRetText
##
##    def WinGetText(self, strTitle, strText):
##        u'method WinGetText'
##        #return strRetText
##
##    def PixelChecksum(self, nLeft, nTop, nRight, nBottom, nStep):
##        u'method PixelChecksum'
##        #return nRes
##
##    def StatusbarGetText(self, strTitle, strText, nPart):
##        u'method StatusbarGetText'
##        #return strStatusText
##
##    def DriveMapGet(self, strDevice):
##        u'method DriveMapGet'
##        #return strMapping
##
##    @property
##    def SW_SHOWNORMAL(self):
##        u'property SW_SHOWNORMAL'
##        #return pVal
##
##    def MouseGetPosY(self):
##        u'method MouseGetPosY'
##        #return nRes
##
##    def MouseGetPosX(self):
##        u'method MouseGetPosX'
##        #return nRes
##
##    def WinGetHandle(self, strTitle, strText):
##        u'method WinGetHandle'
##        #return strRetText
##
##    def ProcessSetPriority(self, strProcess, nPriority):
##        u'method ProcessSetPriority'
##        #return nRes
##
##    @property
##    def SW_SHOWNOACTIVATE(self):
##        u'property SW_SHOWNOACTIVATE'
##        #return pVal
##
##    def MouseGetCursor(self):
##        u'method MouseGetCursor'
##        #return nRes
##
##    def ControlDisable(self, strTitle, strText, strControl):
##        u'method ControlDisable'
##        #return nRes
##
##    def ControlGetText(self, strTitle, strText, strControl):
##        u'method ControlGetText'
##        #return strControlText
##
##    def WinClose(self, strTitle, strText):
##        u'method WinClose'
##        #return nRes
##
##    def Send(self, strSendText, nMode):
##        u'method Send'
##        #return 
##
##    def ControlSend(self, strTitle, strText, strControl, strSendText, nMode):
##        u'method ControlSend'
##        #return nRes
##
##    def ControlClick(self, strTitle, strText, strControl, strButton, nNumClicks, nX, nY):
##        u'method ControlClick'
##        #return nRes
##
##    @property
##    def SW_RESTORE(self):
##        u'property SW_RESTORE'
##        #return pVal
##
##    def ControlGetPosHeight(self, strTitle, strText, strControl):
##        u'method ControlGetPosHeight'
##        #return nRes
##
##    def WinWaitNotActive(self, strTitle, strText, nTimeout):
##        u'method WinWaitNotActive'
##        #return nRes
##
##    def Run(self, strRun, strDir, nShowFlag):
##        u'method Run'
##        #return nRes
##
##    def ProcessClose(self, strProcess):
##        u'method ProcessClose'
##        #return nRes
##
##    def RunAs(self, strUser, strDomain, strPassword, nLogonFlag, strRun, strDir, nShowFlag):
##        u'method RunAs'
##        #return nRes
##
##    def WinExists(self, strTitle, strText):
##        u'method WinExists'
##        #return nRes
##
##    def WinActive(self, strTitle, strText):
##        u'method WinActive'
##        #return nRes
##
##    @property
##    def version(self):
##        u'property version'
##        #return strRetVer
##
##    def ControlGetFocus(self, strTitle, strText):
##        u'method ControlGetFocus'
##        #return strControlWithFocus
##
##    def WinGetState(self, strTitle, strText):
##        u'method WinGetState'
##        #return nRes
##
##    def PixelGetColor(self, nX, nY):
##        u'method PixelGetColor'
##        #return nRes
##
##    def WinWait(self, strTitle, strText, nTimeout):
##        u'method WinWait'
##        #return nRes
##
##    def ControlEnable(self, strTitle, strText, strControl):
##        u'method ControlEnable'
##        #return nRes
##
##    def WinGetProcess(self, strTitle, strText):
##        u'method WinGetProcess'
##        #return strResult
##
##    def IsAdmin(self):
##        u'method IsAdmin'
##        #return nRes
##
##    def ProcessWait(self, strProcess, nTimeout):
##        u'method ProcessWait'
##        #return nRes
##
##    @property
##    def SW_SHOWDEFAULT(self):
##        u'property SW_SHOWDEFAULT'
##        #return pVal
##
##    def WinMove(self, strTitle, strText, nX, nY, nWidth, nHeight):
##        u'method WinMove'
##        #return nRes
##
##    def WinWaitActive(self, strTitle, strText, nTimeout):
##        u'method WinWaitActive'
##        #return nRes
##
##    def ClipPut(self, strClip):
##        u'method ClipPut'
##        #return 
##
##    def ControlSetText(self, strTitle, strText, strControl, strControlText):
##        u'method ControlSetText'
##        #return nRes
##
##    @property
##    def SW_SHOWMINIMIZED(self):
##        u'property SW_SHOWMINIMIZED'
##        #return pVal
##
##    def ControlMove(self, strTitle, strText, strControl, nX, nY, nWidth, nHeight):
##        u'method ControlMove'
##        #return nRes
##
##    def MouseUp(self, strButton):
##        u'method MouseUp'
##        #return 
##
##    def WinSetTrans(self, strTitle, strText, nTrans):
##        u'method WinSetTrans'
##        #return nRes
##
##    def WinGetClientSizeWidth(self, strTitle, strText):
##        u'method WinGetClientSizeWidth'
##        #return nRes
##
##    def WinSetTitle(self, strTitle, strText, strNewTitle):
##        u'method WinSetTitle'
##        #return nRes
##
##    def ControlFocus(self, strTitle, strText, strControl):
##        u'method ControlFocus'
##        #return nRes
##
##    def WinGetClientSizeHeight(self, strTitle, strText):
##        u'method WinGetClientSizeHeight'
##        #return nRes
##
##    def WinGetCaretPosX(self):
##        u'method WinGetCaretPosX'
##        #return nRes
##
##    def WinGetCaretPosY(self):
##        u'method WinGetCaretPosY'
##        #return nRes
##
##    def MouseDown(self, strButton):
##        u'method MouseDown'
##        #return 
##
##    def ControlTreeView(self, strTitle, strText, strControl, strCommand, strExtra1, strExtra2):
##        u'method ControlTreeView'
##        #return strResult
##
##    def WinList(self, strTitle, strText):
##        u'method WinList'
##        #return vOutResult
##
##    def ControlShow(self, strTitle, strText, strControl):
##        u'method ControlShow'
##        #return nRes
##
##    def PixelSearch(self, nLeft, nTop, nRight, nBottom, nCol, nVar, nStep):
##        u'method PixelSearch'
##        #return vOutResult
##
##    @property
##    def SW_SHOWNA(self):
##        u'property SW_SHOWNA'
##        #return pVal
##
##    def ToolTip(self, strTip, nX, nY):
##        u'method ToolTip'
##        #return 
##
##    def WinGetPosX(self, strTitle, strText):
##        u'method WinGetPosX'
##        #return nRes
##
##    def WinGetPosY(self, strTitle, strText):
##        u'method WinGetPosY'
##        #return nRes
##
##    def Shutdown(self, nFlags):
##        u'method Shutdown'
##        #return nRes
##
##    @property
##    def error(self):
##        u'property error'
##        #return pVal
##
##    def WinWaitClose(self, strTitle, strText, nTimeout):
##        u'method WinWaitClose'
##        #return nRes
##
##    @property
##    def SW_HIDE(self):
##        u'property SW_HIDE'
##        #return pVal
##
##    def RunWait(self, strRun, strDir, nShowFlag):
##        u'method RunWait'
##        #return nRes
##
##    @property
##    def SW_SHOW(self):
##        u'property SW_SHOW'
##        #return pVal
##
##    def Init(self):
##        u'method Init'
##        #return 
##
##    def WinMenuSelectItem(self, strTitle, strText, strItem1, strItem2, strItem3, strItem4, strItem5, strItem6, strItem7, strItem8):
##        u'method WinMenuSelectItem'
##        #return nRes
##
##    def MouseWheel(self, strDirection, nClicks):
##        u'method MouseWheel'
##        #return 
##
##    def AutoItSetOption(self, strOption, nValue):
##        u'method AutoItSetOption'
##        #return nRes
##
##    @property
##    def SW_SHOWMAXIMIZED(self):
##        u'property SW_SHOWMAXIMIZED'
##        #return pVal
##
##    def WinActivate(self, strTitle, strText):
##        u'method WinActivate'
##        #return 
##
##    def ControlGetPosWidth(self, strTitle, strText, strControl):
##        u'method ControlGetPosWidth'
##        #return nRes
##
##    def ProcessWaitClose(self, strProcess, nTimeout):
##        u'method ProcessWaitClose'
##        #return nRes
##
##    def WinGetPosWidth(self, strTitle, strText):
##        u'method WinGetPosWidth'
##        #return nRes
##
##    def WinKill(self, strTitle, strText):
##        u'method WinKill'
##        #return nRes
##
##    def WinSetState(self, strTitle, strText, nFlags):
##        u'method WinSetState'
##        #return nRes
##
##    def DriveMapDel(self, strDevice):
##        u'method DriveMapDel'
##        #return nRes
##
##    @property
##    def SW_MINIMIZE(self):
##        u'property SW_MINIMIZE'
##        #return pVal
##
##    def MouseMove(self, nX, nY, nSpeed):
##        u'method MouseMove'
##        #return nRes
##
##    def ControlHide(self, strTitle, strText, strControl):
##        u'method ControlHide'
##        #return nRes
##
##    def MouseClickDrag(self, strButton, nX1, nY1, nX2, nY2, nSpeed):
##        u'method MouseClickDrag'
##        #return nRes
##
##    def ProcessExists(self, strProcess):
##        u'method ProcessExists'
##        #return nRes
##
##    def ClipGet(self):
##        u'method ClipGet'
##        #return strClip
##
##    def DriveMapAdd(self, strDevice, strShare, nFlags, strUser, strPwd):
##        u'method DriveMapAdd'
##        #return strResult
##
##    @property
##    def SW_SHOWMINNOACTIVE(self):
##        u'property SW_SHOWMINNOACTIVE'
##        #return pVal
##
##    def WinMinimizeAll(self):
##        u'method WinMinimizeAll'
##        #return 
##
##    def ControlGetHandle(self, strTitle, strText, strControl):
##        u'method ControlGetHandle'
##        #return strRetText
##
##    def Sleep(self, nMilliseconds):
##        u'method Sleep'
##        #return 
##

class Library(object):
    u'AutoItX3 1.0 Type Library'
    name = u'AutoItX3Lib'
    _reg_typelib_ = ('{F8937E53-D444-4E71-9275-35B64210CC3B}', 1, 0)

__all__ = ['AutoItX3', 'IAutoItX3']
from comtypes import _check_version; _check_version('501')
