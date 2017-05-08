#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Outfile=GDACleanup.exe
#AutoIt3Wrapper_Outfile_x64=GDACleanup64.exe
#AutoIt3Wrapper_Compile_Both=y
#AutoIt3Wrapper_UseX64=y
#AutoIt3Wrapper_Change2CUI=y
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
; *** Start added by AutoIt3Wrapper ***
#include <AutoItConstants.au3>
; *** End added by AutoIt3Wrapper ***
#include <Constants.au3>
;~ #include "CUIAutomation2.au3"
;~ #include "MSAccessibility.au3"

Opt( "MustDeclareVars", 1 )

Func getProcessNamePID($procname)
	; Display a list of Notepad processes returned by ProcessList.
    Local $aProcessList = ProcessList($procname)
    For $i = 0 To $aProcessList[0][0]
        ;MsgBox($MB_SYSTEMMODAL, "", $aProcessList[$i][0] & @CRLF & "PID: " & $aProcessList[$i][1])
		if $aProcessList[$i][0]=$procname Then
			Return $aProcessList[$i][1]
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

Func KillAll($gopro_pid)
	ConsoleWrite(@CRLF & "KillAll:"& String(UBound($gopro_pid)) & " GoPro*.exe processes")
	Local $k = Null
	Local $killcount = 0
	For $i = 0 To UBound($gopro_pid)-1
		$k = ProcessClose($gopro_pid[$i])
		;RunWait("taskkill /F /pid " & String($gopro_pid[$i]), "", @SW_HIDE)
		if $k=0 And @error>0 Then
			ConsoleWrite(@CRLF & "Kill:"& $gopro_pid[$i]& " = "& String(@error) & " GoPro*.exe processes")
		Else
			ConsoleWrite(@CRLF & "Kill:"& $gopro_pid[$i]& " = "& String($k) & " GoPro*.exe processes")
			$killcount += 1
		EndIf
    Next
	if $killcount = UBound($gopro_pid) Then
		Return True
	EndIf
	Return False
EndFunc
Func FindKillAll($procname)
	Local $proclist = Null
	$proclist = getProcessList($procname)
	If $proclist == Null Then
		Return False
	EndIf

	KillAll($proclist)

EndFunc
Func TestUninstaller()
	Local $gopro_pid=getProcessList("quik")
	if UBound($gopro_pid)>0 Then
		ConsoleWrite(@CRLF & "FAILED: Unistall Quik*.exe processes still running")
		KillAll($gopro_pid)
		Return False
	Else
		ConsoleWrite(@CRLF & "PASSED: Unistall:No Quik*.exe processes running")
		Return True
	EndIf
EndFunc
Func DeleteFolder($path)
	ConsoleWrite(@CRLF & "Remove files:" & $path)
	if not FileExists($path) Then
		ConsoleWrite(@CRLF & "Folder Does Not Exist")
		Return
	EndIf
	FileSetAttrib($path &"\*.*","+N-RASHOT",$FT_RECURSIVE )
	Local $rc=DirRemove($path,$DIR_REMOVE )
	if $rc==1 Then
		ConsoleWrite(@CRLF & "PASSED:Remove files:" )
		DirRemove($path,$DIR_DEFAULT  )
	Else
		ConsoleWrite(@CRLF & "FAILED:Remove files:" )
	EndIf
EndFunc
Func Cleanup_GDA_App()

	ConsoleWrite(@CRLF & "START Cleanup Quik==================================")
	;Cleanup
	;::  Latest .exe of GoPro for desktop
	;::  Purge all files from C:\Users(username)\AppData\Local\GoPro
	;::  Task Manager open - End Task for GoPro Detection and GoPro System Tray
	;::  This PC\system\program files\GoPro\GoPro Desktop App
	;::  Make sure to click under view - Show Hidden Files

	;GoPro.exe
	;GoProAnalyticsService.exe
	;GoProAlertService.exe
	;GoProDesktopSystemTray.exe
	;GoProDeviceDetection.exe
	;GoProDeviceDetection.exe
	;GoProDeviceService.exe
	;GoProIDService.exe
	;GoProMediaFolderService.exe
	;GoProMediaService.exe
	;GoProMsgBus.exe
	;GoProShareService.exe
	;GoProUpdateService.exe
	;check processes and cleanup
;~ 	if Not TestUninstaller() Then
;~ 		Sleep(2000)
;~ 		TestUninstaller()
;~ 	EndIf
	Local $goprodata=@LocalAppDataDir&"\GoPro\Databases"
	DeleteFolder($goprodata)
	$goprodata=@LocalAppDataDir&"\GoPro\exports"
	DeleteFolder($goprodata)
	$goprodata=@LocalAppDataDir&"\GoPro\uploadtemp"
	DeleteFolder($goprodata)
	$goprodata=@LocalAppDataDir&"\GoPro"
	DeleteFolder($goprodata)
	;delete image repo
	$goprodata=@UserProfileDir&"\Pictures\GoPro"
	DeleteFolder($goprodata)
	$goprodata=@ProgramFilesDir&"\GoPro"
	DeleteFolder($goprodata)
	$goprodata=@ProgramsDir&"\GoPro"
	DeleteFolder($goprodata)
	$goprodata=@ProgramsCommonDir&"\GoPro"
	DeleteFolder($goprodata)
	$goprodata="C:\Program Files\GoPro"
	DeleteFolder($goprodata)

	;delete stored credentials for first time GDA use
	ConsoleWrite(@CRLF & "Delete Credentials for first time Quik use")
	Local $cmd = "cmdkey /delete:GoPro_Desktop_App"
	;Local $rc = RunWait(@ComSpec & " /c " & $cmd)
	Local $rc = RunWait($cmd)
	ConsoleWrite(@CRLF & "Delete Credentials:" & $rc)

	;delete user files
	;ConsoleWrite(@CRLF & @AppDataCommonDir)
	;ConsoleWrite(@CRLF & @AppDataDir)
;~ 	ConsoleWrite(@CRLF & @LocalAppDataDir)
;~ 	ConsoleWrite(@CRLF & @HomeDrive&@HomePath)
;~ 	ConsoleWrite(@CRLF & @UserProfileDir)
;~ 	ConsoleWrite(@CRLF & @TempDir)
;~ 	ConsoleWrite(@CRLF & @ComSpec)
EndFunc

Func Uninstall_GDA($gdapath)
	Local $hWnd = WinWait("Quik Uninstaller","",10)
	If $hWnd <> 0 Then
		ConsoleWrite(@CRLF & "Uninstall Quik==================================")
		WinActivate($hWnd)
		WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
		WinFlash($hWnd, "", 4, 500)
		;start uninstall process
		Send("{ENTER}")
		;wait for popup dialog
		$hWnd = WinWait("Quik Uninstall","",120)
		If $hWnd <> 0 Then
			WinActivate($hWnd)

			ConsoleWrite(@CRLF & "Uninstall Quik Done")
			WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
			Send("{ENTER}")
			ConsoleWrite(@CRLF & "Uninstall Quik Close")
			;WinWaitClose($hWnd,120)

			;ConsoleWrite(@CRLF & "Uninstall GDA wait for closed")
			Cleanup_GDA_App()
			Sleep(1000)
			Run($gdapath)
			Sleep(1000)
		EndIf

	EndIf
EndFunc

; Run the gopro

Local $jenkins = "C:\Win_GDA-Studio_3a_BAT\"
Local $gdapath = $jenkins & "temp\GoPro Quik-WinInstaller-2.3.0.5166.exe" ;debug
if $CmdLine[0] > 0 Then
	$gdapath = $CmdLine[1] ; full path to installer
EndIf

;~ if Not FileExists($gdapath) Then
;~ 	;$gdapath="C:\Users\" & EnvGet("USERNAME") & "\workspace\Win_GDA-Studio_3a_BAT\Automation\temp\"
;~ 	$gdapath = $jenkins & "temp\"
;~ 	FileChangeDir($gdapath)
;~ 	Local $hSearch = FileFindFirstFile("GoPro-WinInstaller-*.exe")
;~ 	Local $f
;~ 	If $hSearch <> -1 Then
;~ 		$f=FileFindNextFile($hSearch)
;~ 		$gdapath = $gdapath & $f ;full path to installer
;~ 	EndIf
;~ 	FileClose($hSearch)
;~ EndIf

;~ if Not FileExists($gdapath) Then
;~ 	ConsoleWrite(@CRLF & "Error: Can't resolve or find the GoPro-WinInstaller.exe")
;~ 	exit(1)
;~ EndIf
;~ $hWnd1=0
;ConsoleWrite(@CRLF & "START GoPro-WinInstaller.exe")
;ConsoleWrite(@CRLF & $gdapath)
;Run($gdapath)
;Uninstall_GDA($gdapath)

If FindKillAll("Quik") Then
	ConsoleWrite(@CRLF & "FindKillAll Quik OK")
Else
	ConsoleWrite(@CRLF & "FindKillAll Quik Failed")
EndIf

If FindKillAll("GoPro") Then
	ConsoleWrite(@CRLF & "FindKillAll GoPro OK")
Else
	ConsoleWrite(@CRLF & "FindKillAll GoPro Failed")
EndIf
;KillAll("GoPro*")
Cleanup_GDA_App()
exit(0)
;~ $hWnd = WinWait("GoPro","",10)
;~ If $hWnd <> 0 Then
;~ 	WinClose($hWnd)
;~ 	Sleep(1000)
;~ 	Send("{TAB}{ENTER}")
;~ EndIf
Sleep(2000)



;Sleep(2000)
ConsoleWrite(@CRLF & "Run Install Quik")
Run($gdapath)
;Uninstall_GDA($gdapath)
Sleep(3000)

;KillAll("GoPro.exe")

; Wait for the calculator to become active. The classname "CalcFrame" is monitored instead of the window title
;WinWaitActive("[CLASS:CalcFrame]")
$hWnd = WinWait("GoPro","",10)
If $hWnd = 0 Then
	ConsoleWrite(@CRLF & "Not Found: GoPro Quik Install Window==================================")
	Exit(1)
EndIf
if $hWnd=$hWnd1 Then

	ConsoleWrite(@CRLF & "1Window Stuck: GoPro Quik Install Window==================================")
	ConsoleWrite(@CRLF & String($hWnd) & "=" & String($hWnd1))
	Exit(1)
EndIf
$hWnd1=$hWnd
ConsoleWrite(@CRLF & "START Install Quik==================================")
WinActivate($hWnd)
WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
;WinFlash($hWnd, "", 4, 500)

WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
;Local $hControl = ControlGetHandle($hWnd,"","[CLASS:MBA;UIThread;a8516069-e736-43b9-90a9-3e0df8aad689]")

;ControlClick($hWnd, "","[TEXT:Next]")
;ControlClick($hWnd, "","[CLASS:MBA;UIThread;a8516069-e736-43b9-90a9-3e0df8aad689]")

;Local $sText = ControlGetText($hWnd, "", "Edit1")

;AutoItSetOption("SendKeyDelay", 400)
;next
ConsoleWrite(@CRLF & "Welcome To...")
WinActivate($hWnd)
WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
WinActivate($hWnd)
Send("{TAB}{ENTER}")

Sleep(2000)
$hWnd = WinWait("Quik","",30)
If $hWnd=0 Then
	ConsoleWrite(@CRLF & "Not Found: GoPro Quik Install Window==================================")
	Exit(1)
EndIf
if $hWnd=$hWnd1 Then
	ConsoleWrite(@CRLF & "2Window Stuck: GoPro Quik Install Window==================================")

	ConsoleWrite(@CRLF & String($hWnd) & "=" & String($hWnd1))
	Exit(1)
EndIf
$hWnd1=$hWnd
WinActivate($hWnd)
WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
;WinFlash($hWnd, "", 4, 500)

;accept license
ConsoleWrite(@CRLF & "License Agreement...")
WinActivate($hWnd)
WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
WinActivate($hWnd)

Send("{TAB}")
Sleep(1000)
Send("{TAB}")
Sleep(1000)
Send("{TAB}")
Sleep(1000)
Send("{TAB}")
Sleep(1000)
Send("{TAB}")
Sleep(1000)
Send("{SPACE}")
ConsoleWrite(@CRLF & "License Accept...")
Sleep(1000)
Send("{TAB}")
Sleep(1000)
Send("{ENTER}")
Sleep(2000)
$hWnd = WinWait("Quik","",30)
If $hWnd=0 Then
	ConsoleWrite(@CRLF & "Not Found: GoPro Quik Install Window==================================")
	Exit(1)
EndIf
if $hWnd=$hWnd1 Then
	ConsoleWrite(@CRLF & "3Window Stuck: GoPro Quik Install Window==================================")

	ConsoleWrite(@CRLF & String($hWnd) & "=" & String($hWnd1))
	Exit(1)
EndIf
$hWnd1=$hWnd
WinActivate($hWnd)
WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
;WinFlash($hWnd, "", 4, 500)
WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
ConsoleWrite(@CRLF & "Install Location...")
WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
;next
WinActivate($hWnd)
Send("{TAB}{ENTER}")
Sleep(2000)

$hWnd = WinWait("Quik","",30)
If $hWnd=0 Then
	ConsoleWrite(@CRLF & "Not Found: GoPro Quik Install Window==================================")
	Exit(1)
EndIf
if $hWnd=$hWnd1 Then
	ConsoleWrite(@CRLF & "4Window Stuck: GoPro Quik Install Window==================================")

	ConsoleWrite(@CRLF & String($hWnd) & "=" & String($hWnd1))
	Exit(1)
EndIf
$hWnd1=$hWnd
Sleep(1000)
ConsoleWrite(@CRLF & "Installing Quik.....")

Sleep(120000) ;30sec
$hWnd = WinWait("GoPro","",30)
If $hWnd=0 Then
	ConsoleWrite(@CRLF & "Not Found: GoPro Quik Install Window==================================")
	Exit(1)
EndIf
if $hWnd=$hWnd1 Then
	ConsoleWrite(@CRLF & "5Window Stuck: GoPro Quik Install Window==================================")

	ConsoleWrite(@CRLF & String($hWnd) & "=" & String($hWnd1))
	Exit(1)
EndIf
$hWnd1=$hWnd
ConsoleWrite(@CRLF & "Installing Quik.....")
WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
WinActivate($hWnd)
;WinFlash($hWnd, "", 4, 500)
WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
ConsoleWrite(@CRLF & "Succesfuly Installed, Finish..")
WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
;install
WinActivate($hWnd)
Send("{TAB}{TAB}{ENTER}")
Sleep(2000)
$hWnd = WinWait("Quik","",30)
If $hWnd=0 Then
	ConsoleWrite(@CRLF & "Not Found: GoPro Quik Install Window==================================")
	Exit(1)
EndIf
if $hWnd=$hWnd1 Then
	ConsoleWrite(@CRLF & "6Window Stuck: GoPro Quik Install Window==================================")
	ConsoleWrite(@CRLF & String($hWnd) & "=" & String($hWnd1))
	Exit(1)
EndIf
$hWnd1=$hWnd
ConsoleWrite(@CRLF & "Start Quik App.....")
;WinWaitClose($hWnd,10)
Sleep(2000)
$hWnd = WinWait("Quik","",30)
if $hWnd=$hWnd1 Then
	ConsoleWrite(@CRLF & "Window Stuck: GoPro Quik Install Window==================================")
	ConsoleWrite(@CRLF & String($hWnd) & "=" & String($hWnd1))
	Exit(1)
EndIf
$hWnd1=$hWnd
If $hWnd<>0 Then
	ConsoleWrite(@CRLF & "Quik App Running==================================")
	WinActivate($hWnd)
	WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
	;WinFlash($hWnd, "", 4, 500)
	WinActivate($hWnd)
	;Send("{TAB}{ENTER}")
	ConsoleWrite(@CRLF & "Completed GoPro Quik Installer==================================")
	;WinClose("[CLASS:Qt5QWindowIcon]")
Else
	ConsoleWrite(@CRLF & "FAILED Quik App Startup *******************")
	Exit(1)
EndIf
; Now that the calculator window is active type the values 2 x 4 x 8 x 16
; Use AutoItSetOption to slow down the typing speed so we can see it
;~ AutoItSetOption("SendKeyDelay", 400)
;~ Send("2*4*8*16=")
;~ Sleep(2000)

;~ ; Now quit by sending a "close" request to the calculator window using the classname
;~ WinClose("[CLASS:CalcFrame]")

;~ ; Now wait for the calculator to close before continuing
;~ WinWaitClose("[CLASS:CalcFrame]")

; Finished!
