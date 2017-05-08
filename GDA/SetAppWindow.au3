; *** Start added by AutoIt3Wrapper ***
#include <StringConstants.au3>
; *** End added by AutoIt3Wrapper ***
#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Outfile=GDASetAppWindow.exe
#AutoIt3Wrapper_Outfile_x64=GDASetAppWindow64.exe
#AutoIt3Wrapper_Compile_Both=y
#AutoIt3Wrapper_UseX64=y
#AutoIt3Wrapper_Change2CUI=y
#AutoIt3Wrapper_Add_Constants=n
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
; *** Start added by AutoIt3Wrapper ***
#include <AutoItConstants.au3>
; *** End added by AutoIt3Wrapper ***
#include <Constants.au3>
#include <WinAPIEx.au3>

Func getProcessNamePID($procname, $dokill=False)
	; Display a list of  processes returned by ProcessList.
    Local $aProcessList = ProcessList($procname)
    For $i = 0 To $aProcessList[0][0]
        ;MsgBox($MB_SYSTEMMODAL, "", $aProcessList[$i][0] & @CRLF & "PID: " & $aProcessList[$i][1])
		if $aProcessList[$i][0]=$procname Then
			;ConsoleWrite(@CRLF & $aProcessList[$i][0] &  " PID:" & $aProcessList[$i][1])
			if $dokill=True Then ; kills all Quik processes
				ProcessClose($aProcessList[$i][1]) ;gracefull close
			Else
				Return $aProcessList[$i][1] ; first found
			EndIf
		EndIf
    Next
	Return Null
EndFunc

Func getProcessList($procname)
	; Display a list of Notepad processes returned by ProcessList.
    Local $aProcessList = ProcessList()
	Local $pid[0]
    For $i = 0 To $aProcessList[0][0]
        ;MsgBox($MB_SYSTEMMODAL, "", $aProcessList[$i][0] & @CRLF & "PID: " & $aProcessList[$i][1])
		if StringInStr($aProcessList[$i][0],$procname,$STR_NOCASESENSE )>0 Then
			ReDim $pid[UBound($pid) + 1]
			$pid[UBound($pid)-1]= $aProcessList[$i][1]
			ConsoleWrite(@CRLF & $aProcessList[$i][0] &  " PID:" & $aProcessList[$i][1])
		EndIf
    Next
	Return $pid
EndFunc

Func FindKillAll($procname)
	Local $proclist = Null
	$proclist = getProcessList($procname)
	If $proclist == Null Then
		ConsoleWrite(@CRLF & "Process not found nothing to kill")
	EndIf

	KillAll($proclist)

EndFunc

; array of pid
Func KillAll($gopro_pid)
	ConsoleWrite(@CRLF & "KillAll:"& String(UBound($gopro_pid)) & " Quik*.exe processes")
	Local $k = Null
	For $i = 0 To UBound($gopro_pid)-1
		$k = ProcessClose($gopro_pid[$i])
		;RunWait("taskkill /F /pid " & String($gopro_pid[$i]), "", @SW_HIDE)
		if $k=0 And @error>0 Then
			ConsoleWrite(@CRLF & "Kill:"& $gopro_pid[$i]& " = "& String(@error) & " Quik*.exe processes")
		Else
			ConsoleWrite(@CRLF & "Kill:"& $gopro_pid[$i]& " = "& String($k) & " Quik*.exe processes")
		EndIf
    Next
EndFunc

Func ProcessGetName($PId)
    If IsNumber($PId) = 0 Then
        SetError(2)
;~     ElseIf $PId > 999999 Then
;~         SetError(1)
    Else
        Local $PList = ProcessList("Quik.exe")
        Local $i = 1
        Local $ProcessName = ""
		;ConsoleWrite(@CRLF & String($PId))
		For $i = 1 To $PList[0][0]
			;ConsoleWrite(@CRLF & $PList[$i][1] & "-" &$PId)
			if $Pid = Number($PList[$i][1],$NUMBER_32BIT) Then
				;ConsoleWrite(@CRLF & $PList[$i][1] & "-" &$PId)
				Return $PList[$i][0]
			EndIf
		Next
		Return "!"
;~         While $i <= $PList[0][0] And $ProcessName = ""
;~             If $PList[$i][1] = $PId Then
;~                 $ProcessName = $PList[$i][0]
;~ 				Return $ProcessName
;~             Else
;~                 $i = $i + 1
;~             EndIf
;~         WEnd
;~         Return $ProcessName
    EndIf
EndFunc   ;==>ProcessGetName

Func ProcessGetWindow($PId)
    If IsNumber($PId) = 0 Or ProcessExists(ProcessGetName($PId)) = 0 Then
        SetError(1)
    Else
        Local $WinList = WinList()
        Local $i = 1
        Local $WindowTitle = ""
        While $i <= $WinList[0][0] And $WindowTitle = ""
            If WinGetProcess($WinList[$i][0], "") = $PId Then
                $WindowTitle = $WinList[$i][0]
            Else
                $i += 1
            EndIf
        WEnd
        Return $WindowTitle
    EndIf
EndFunc   ;==>ProcessGetWindow

Func EvalwinsizeSpec($hwnd,$w,$h)
	Local $aClientSize=WinGetClientSize($hWnd)
	ConsoleWrite(@CRLF & "Width: " & $aClientSize[0] & @CRLF & "Height: " & $aClientSize[1])
	if $aClientSize[0]>$w Or $aClientSize[1] >$h Then
		Return True
	EndIf
	Return False
EndFunc

Func getProcWinList($Pid)
	Local $syswinlist=WinList()
	local $thispid = 0
	Local $procname=""
	Local $hmainwin=0
	Local $thiswin=0
	For $i = 1 To $syswinlist[0][0]
        If $syswinlist[$i][0] = "GoPro" Then ; And BitAND(WinGetState($syswinlist[$i][1]), $WIN_STATE_VISIBLE) Then
			$thispid=WinGetProcess($syswinlist[$i][1])
			$procname=ProcessGetName($thispid)
			;ConsoleWrite(@CRLF & $procname &" - Title: " & $syswinlist[$i][0] & @CRLF & "Handle: " & $syswinlist[$i][1])

			if $Pid=$thispid Then
				$thiswin=$syswinlist[$i][1]
				ConsoleWrite(@CRLF & $procname& "  Title: " & $syswinlist[$i][0] & " Handle: " & $syswinlist[$i][1])

				if EvalwinsizeSpec($thiswin,200,200)= True Then
					$hmainwin=$thiswin
					ConsoleWrite(@CRLF & $procname& " MainWin  Title: " & $syswinlist[$i][0] & " Handle: " & $syswinlist[$i][1])
					Return $hmainwin
				EndIf
			EndIf
        EndIf
    Next
	Return $hmainwin

EndFunc


; Window to Process
; Now making Window name and executables/PIDs interchangable!
; Credit to Cynagen
func _Win2Process($wintitle)
    if isstring($wintitle) = 0 then return -1
    $wproc = WinGetProcess($wintitle)
    return _ProcessName($wproc)
endfunc
func _Process2Win($pid)
    if isstring($pid) then $pid = processexists($pid)
    if $pid = 0 then return -1
    $list = WinList()
    for $i = 1 to $list[0][0]
        if $list[$i][0] <> "" AND BitAnd(WinGetState($list[$i][1]),2) then
            $wpid = WinGetProcess($list[$i][0])
            if $wpid = $pid then return $list[$i][0]
        EndIf
    next
    return -1
endfunc
func _ProcessName($pid)
    if isstring($pid) then $pid = processexists($pid)
    if not isnumber($pid) then return -1
    $proc = ProcessList()
    for $p = 1 to $proc[0][0]
        if $proc[$p][1] = $pid then return $proc[$p][0]
    Next
    return -1
EndFunc

Func getWindowListHandle($wintitle)
    ; Retrieve a list of window handles.
    Local $aList = WinList()

    ; Loop through the array displaying only visable windows with a title.
    For $i = 1 To $aList[0][0]
		;ConsoleWrite(@CRLF & "Window: " & $aList[$i][0])
		If $aList[$i][0]==$wintitle Then
			;return $aList[$i][1]
			ConsoleWrite(@CRLF & "FOUND Window: " & $aList[$i][1])
			Local $aPos = WinGetPos($aList[$i][1])
			ConsoleWrite(@CRLF & "W=" & String($aPos[2]))
			ConsoleWrite(@CRLF & "H=" & String($aPos[3]))
			If $aPos[2]>1000 Then
				return $aList[$i][1]
			EndIf

		EndIf
        ;If $aList[$i][0] <> "" And BitAND(WinGetState($aList[$i][1]), 2) Then
        ;    MsgBox($MB_SYSTEMMODAL, "", "Title: " & $aList[$i][0] & @CRLF & "Handle: " & $aList[$i][1])
        ;EndIf
    Next
EndFunc   ;==>Example
; #################################################
; Start

$dokill=False
$apptitle = "GoPro Quik" ;$CmdLine[0]
$hWnd = getWindowListHandle($apptitle)
$gppid=0
$appname = $apptitle & ".exe"
_Win2Process($appname)
$apppath = "C:\Program Files\GoPro\GoPro Desktop App\"
;ConsoleWrite(@CRLF & "START QUIK====================")
;$gppid = Run("C:\Program Files\GoPro\GoPro Desktop App\Quik.exe","C:\Program Files\GoPro\GoPro Desktop App")
;Sleep(15000)
;ConsoleWrite(@CRLF & "RUN QUIK====================")
;Exit(0)
if $CmdLine[0]=1 Then
	if $CmdLine[1]="kill" Then
		$dokill=False
		ConsoleWrite(@CRLF & "Kill Quik Process")
	Else
		$apptitle=$CmdLine[1]
		ConsoleWrite(@CRLF & "Start Process " & $apptitle)
	EndIf
ElseIf $CmdLine[0]=2 Then
	$apptitle=$CmdLine[1]
	$dokill=False
	ConsoleWrite(@CRLF & "Kill Process " & $apptitle)
EndIf
;getProcessList($appname)


;getProcessList($appname)
$gppid=getProcessNamePID($appname)
If $dokill=True Then
	ConsoleWrite(@CRLF & "KILL Quik Process ")
	$gppid=getProcessNamePID($appname,True)
	_Process2Win($gppid)
	Sleep(5000)
	FindKillAll($appname)

	ConsoleWrite(@CRLF & "KILL GoPro services Process ")
	FindKillAll("GoPro*.exe")
	;KillAll($gppid)
	;$gppid2=getProcessNamePID("GoPro*.exe",$dokill)
	;KillAll($gppid2)
	Sleep(1000)
EndIf



if $gppid=Null Or $gppid=0 Then
	ConsoleWrite(@CRLF & "Startup Quik, waiting Process")
	$gppid = Run($apppath & $appname,$apppath)

	Sleep(5000)
	$gppid=getProcessNamePID($appname)

	if $gppid=Null Or $gppid=0 Then
		ConsoleWrite(@CRLF & "Failed to find Quik Process")
		Exit(0)
	EndIf
EndIf
;gda inner container = 1903, 852
;gda main window = 1907, 856
;screen 1920, 1200
Sleep(1000)
$hWnd = getWindowListHandle($apptitle)
ConsoleWrite(@CRLF & "Found Quik Process " & String($gppid))
$hWnd = WinWait($apptitle,"",10)

if $hwnd=0 Then
	ConsoleWrite(@CRLF & "WINDOW NOT FOUND " )
	Exit(0)
EndIf
;$hWnd2=getProcWinList($gppid)
;if $hwnd2>0 Then
;	$hWnd=$hWnd2
;EndIf
ConsoleWrite(@CRLF & "Found Window " & String($hWnd))
;WinSetState($hWnd, "", @SW_SHOW)
WinWaitActive($hWnd,"",5)
Local $aPos = WinGetPos("[ACTIVE]")
ConsoleWrite(@CRLF & "BEFORE")
ConsoleWrite(@CRLF & "W=" & String($aPos[2]))
ConsoleWrite(@CRLF & "H=" & String($aPos[3]))
;1283x875
;1291,906
;mac=set size of window 1 to {1280, 836}
ConsoleWrite(@CRLF & "RESIZE Window " & String($hWnd))
$w=1280
$h=920
$x=@DesktopWidth-($w+10)
$y=10
; move top right corner
WinMove($hWnd,"",$x,$y,$w,$h)
EvalwinsizeSpec($hWnd,1000,800)
Local $aPos = WinGetPos("[ACTIVE]")
ConsoleWrite(@CRLF & "AFTER")
ConsoleWrite(@CRLF & "W=" & String($aPos[2]))
ConsoleWrite(@CRLF & "H=" & String($aPos[3]))
WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
WinFlash($hWnd, "", 4, 500)
WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
WinActivate($hWnd)
ConsoleWrite(@CRLF & "Done")



