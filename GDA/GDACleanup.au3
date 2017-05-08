#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Outfile=GDACleanup.exe
#AutoIt3Wrapper_Outfile_x64=GDACleanup64.exe
#AutoIt3Wrapper_Compile_Both=y
#AutoIt3Wrapper_UseX64=y
#AutoIt3Wrapper_Change2CUI=y
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****
; *** Start added by AutoIt3Wrapper ***
#include <AutoItConstants.au3>
#include <Process.au3>
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
			ConsoleWrite(@CRLF & "Kill:"& $gopro_pid[$i]& " = "& String(@error)); & " GoPro*.exe processes")
			ConsoleWrite(@CRLF & "trying: Taskkill /PID " & String($k))
			_RunDos("start taskkill /PID " & String($k))
		Else
			ConsoleWrite(@CRLF & "Kill:"& $gopro_pid[$i]& " = "& String($k)) ; & " GoPro*.exe processes")
			$killcount += 1
		EndIf
    Next
	ConsoleWrite(@CRLF & "Killed:" & String($killcount) & "-" & String(UBound($gopro_pid)))
	if $killcount = UBound($gopro_pid) Then
		Return True
	Else
		Return False
	EndIf

EndFunc
Func FindKillAll($procname)
	Local $proclist = Null
	$proclist = getProcessList("GoPro")
	If $proclist == Null Then
		Return False
	EndIf

	If KillAll($proclist) Then
		ConsoleWrite(@CRLF & "FindKillAll OK")
		Return True
	Else
		ConsoleWrite(@CRLF & "FindKillAll Failed")
		Return False
	EndIf
EndFunc
Func TestUninstaller()
	Local $gopro_pid=getProcessList("gopro")
	if UBound($gopro_pid)>0 Then
		ConsoleWrite(@CRLF & "FAILED: Unistall GoPro*.exe processes still running")
		KillAll($gopro_pid)
		Return False
	Else
		ConsoleWrite(@CRLF & "PASSED: Unistall:No GoPro*.exe processes running")
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

	ConsoleWrite(@CRLF & "START Cleanup GDA==================================")
	;Cleanup
	;::  Latest .exe of GoPro for desktop
	;::  Purge all files from C:\Users(username)\AppData\Local\GoPro
	;::  Task Manager open - End Task for GoPro Detection and GoPro System Tray
	;::  This PC\system\program files\GoPro\GoPro Desktop App
	;::  Make sure to click under view - Show Hidden Files
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\CineFormStudio", "PremCS5FLFocused")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro\mainwindow", "geometry")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro\mainwindow", "maximized")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro\mainwindow", "pos")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro\mainwindow", "savestate")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro\mainwindow", "size")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Desktop App\mainwindow", "geometry")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Desktop App\mainwindow", "maximized")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Desktop App\mainwindow", "pos")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Desktop App\mainwindow", "savestate")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Desktop App\mainwindow", "size")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Desktop App", "installed")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Desktop App", "Reinstall")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Desktop App", "TotalReinstall")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Studio", "KeyPath")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Studio", "NewInstall")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Studio", "Reinstall")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Studio", "TotalNewInstall")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Studio", "TotalReinstall")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro", "")

	RegDelete("HKEY_LOCAL_MACHINE\SOFTWARE\GoPro\InstallSpots", "GoProDesktopApp")
	RegDelete("HKEY_LOCAL_MACHINE\SOFTWARE\GoPro\InstallSpots", "GoProTools")
	RegDelete("HKEY_LOCAL_MACHINE\SOFTWARE\GoPro\InstallSpots", "ParentDir")
	RegDelete("HKEY_LOCAL_MACHINE\SOFTWARE\GoPro\InstallSpots", "ProductDir")
	RegDelete("HKEY_LOCAL_MACHINE\SOFTWARE\GoPro", "")

	RegDelete("HKEY_CLASS_ROOT\GoPro Studio Project File","")
	RegDelete("HKEY_CLASS_ROOT\GoPro Studio Template File","")
	RegDelete("HKEY_CLASS_ROOT\GoPro Studio Template Package File","")

	RegDelete("HKEY_CLASSES_ROOT\.gcs", "Default")
	RegDelete("HKEY_CLASSES_ROOT\.gcs", "Default")

	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Project File", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Project File\DefaultIcon", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Project File\shell", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Project File\shell\edit", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Project File\shell\edit\command", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Project File\shell\open", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Project File\shell\open\command", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Template File\DefaultIcon", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Template File\shell\edit\command", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Template File\shell\edit", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Template File\shell\open\command", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Template File\shell\open", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Template File\shell", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Template Package File\shell\edit\command", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Template Package File\shell\edit", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Template Package File\shell\open\command", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Template Package File\shell\open", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Template Package File\shell", "Default")
	RegDelete("HKEY_CLASSES_ROOT\GoPro Studio Template Package File\DefaultIcon", "Default")
	RegDelete("HKEY_CLASSES_ROOT\Installer\Dependencies\{452405D2-38CA-470A-8BF1-820B63EDA7C2}", "Default")
	RegDelete("HKEY_CLASSES_ROOT\Installer\Dependencies\{452405D2-38CA-470A-8BF1-820B63EDA7C2}", "DisplayName")
	RegDelete("HKEY_CLASSES_ROOT\Installer\Dependencies\{452405D2-38CA-470A-8BF1-820B63EDA7C2}", "Version")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\CineFormStudio")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro\mainwindow")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Desktop App")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro\GoPro Studio")
	RegDelete("HKEY_CURRENT_USER\Software\GoPro")


	Local $goprodata=@LocalAppDataDir&"\GoPro\cache"
	DeleteFolder($goprodata)

	$goprodata=@LocalAppDataDir&"\GoPro\Certificates"
	DeleteFolder($goprodata)

	$goprodata=@LocalAppDataDir&"\GoPro\Databases"
	DeleteFolder($goprodata)

	$goprodata=@LocalAppDataDir&"\GoPro\Dumps"
	DeleteFolder($goprodata)

	$goprodata=@LocalAppDataDir&"\GoPro\exports"
	DeleteFolder($goprodata)

	$goprodata=@LocalAppDataDir&"\GoPro\GoPro"
	DeleteFolder($goprodata)

	$goprodata=@LocalAppDataDir&"\GoPro\Music"
	DeleteFolder($goprodata)

	$goprodata=@LocalAppDataDir&"\GoPro\uploadtemp"
	DeleteFolder($goprodata)

	$goprodata=@LocalAppDataDir&"\GoPro"
	DeleteFolder($goprodata)

	$goprodata=@AppDataDir&"\GoPro\Templates"
	ConsoleWrite(@CRLF & "Delete folder:" & $goprodata)
	DeleteFolder($goprodata)

	$goprodata=@AppDataDir&"\GoPro"
	ConsoleWrite(@CRLF & "Delete folder:" & $goprodata)
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
    $goprodata="C:\Users\autogda\AppData\Local\Temp\GoPro"
	DeleteFolder($goprodata)

	;delete stored credentials for first time GDA use
	ConsoleWrite(@CRLF & "Delete Credentials for first time GDA use")
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
	Local $hWnd = WinWait("GoPro Uninstaller","",10)
	If $hWnd <> 0 Then
		ConsoleWrite(@CRLF & "Uninstall GDA==================================")
		WinActivate($hWnd)
		WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
		WinFlash($hWnd, "", 4, 500)
		;start uninstall process
		Send("{ENTER}")
		;wait for popup dialog
		$hWnd = WinWait("GoPro Uninstall","",120)
		If $hWnd <> 0 Then
			WinActivate($hWnd)

			ConsoleWrite(@CRLF & "Uninstall GDA Done")
			WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
			Send("{ENTER}")
			ConsoleWrite(@CRLF & "Uninstall GDA Close")
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
Local $gdapath = $jenkins & "temp\GoPro-WinInstaller-2.0.0.2083.exe" ;debug
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

FindKillAll("GoPro*")
Sleep(5000)
FindKillAll("GoPro*")
;KillAll("GoPro*")
Cleanup_GDA_App()
exit(0)

;###############################################
; END HERE JUST DO CLEANUP
;###############################################
;~ $hWnd = WinWait("GoPro","",10)
;~ If $hWnd <> 0 Then
;~ 	WinClose($hWnd)
;~ 	Sleep(1000)
;~ 	Send("{TAB}{ENTER}")
;~ EndIf
Sleep(2000)



;Sleep(2000)
ConsoleWrite(@CRLF & "Run Install GDA")
Run($gdapath)
;Uninstall_GDA($gdapath)
Sleep(3000)

;KillAll("GoPro.exe")

; Wait for the calculator to become active. The classname "CalcFrame" is monitored instead of the window title
;WinWaitActive("[CLASS:CalcFrame]")
Local $hWnd = 0
$hWnd=WinWait("GoPro","",10)
If $hWnd = 0 Then
	ConsoleWrite(@CRLF & "Not Found: GoPro GDA Install Window==================================")
	Exit(1)
EndIf
if $hWnd=$hWnd1 Then

	ConsoleWrite(@CRLF & "1Window Stuck: GoPro GDA Install Window==================================")
	ConsoleWrite(@CRLF & String($hWnd) & "=" & String($hWnd1))
	Exit(1)
EndIf
$hWnd1=$hWnd
ConsoleWrite(@CRLF & "START Install GDA==================================")
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
$hWnd = WinWait("GoPro","",30)
If $hWnd=0 Then
	ConsoleWrite(@CRLF & "Not Found: GoPro GDA Install Window==================================")
	Exit(1)
EndIf
if $hWnd=$hWnd1 Then
	ConsoleWrite(@CRLF & "2Window Stuck: GoPro GDA Install Window==================================")

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
$hWnd = WinWait("GoPro","",30)
If $hWnd=0 Then
	ConsoleWrite(@CRLF & "Not Found: GoPro GDA Install Window==================================")
	Exit(1)
EndIf
if $hWnd=$hWnd1 Then
	ConsoleWrite(@CRLF & "3Window Stuck: GoPro GDA Install Window==================================")

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

$hWnd = WinWait("GoPro","",30)
If $hWnd=0 Then
	ConsoleWrite(@CRLF & "Not Found: GoPro GDA Install Window==================================")
	Exit(1)
EndIf
if $hWnd=$hWnd1 Then
	ConsoleWrite(@CRLF & "4Window Stuck: GoPro GDA Install Window==================================")

	ConsoleWrite(@CRLF & String($hWnd) & "=" & String($hWnd1))
	Exit(1)
EndIf
$hWnd1=$hWnd
Sleep(1000)
ConsoleWrite(@CRLF & "Installing GDA.....")

Sleep(120000) ;30sec
$hWnd = WinWait("GoPro","",30)
If $hWnd=0 Then
	ConsoleWrite(@CRLF & "Not Found: GoPro GDA Install Window==================================")
	Exit(1)
EndIf
if $hWnd=$hWnd1 Then
	ConsoleWrite(@CRLF & "5Window Stuck: GoPro GDA Install Window==================================")

	ConsoleWrite(@CRLF & String($hWnd) & "=" & String($hWnd1))
	Exit(1)
EndIf
$hWnd1=$hWnd
ConsoleWrite(@CRLF & "Installing GDA.....")
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
$hWnd = WinWait("GoPro","",30)
If $hWnd=0 Then
	ConsoleWrite(@CRLF & "Not Found: GoPro GDA Install Window==================================")
	Exit(1)
EndIf
if $hWnd=$hWnd1 Then
	ConsoleWrite(@CRLF & "6Window Stuck: GoPro GDA Install Window==================================")
	ConsoleWrite(@CRLF & String($hWnd) & "=" & String($hWnd1))
	Exit(1)
EndIf
$hWnd1=$hWnd
ConsoleWrite(@CRLF & "Start GDA App.....")
;WinWaitClose($hWnd,10)
Sleep(2000)
$hWnd = WinWait("GoPro","",30)
if $hWnd=$hWnd1 Then
	ConsoleWrite(@CRLF & "Window Stuck: GoPro GDA Install Window==================================")
	ConsoleWrite(@CRLF & String($hWnd) & "=" & String($hWnd1))
	Exit(1)
EndIf
$hWnd1=$hWnd
If $hWnd<>0 Then
	ConsoleWrite(@CRLF & "GDA App Running==================================")
	WinActivate($hWnd)
	WinSetOnTop($hWnd, "",$WINDOWS_ONTOP)
	;WinFlash($hWnd, "", 4, 500)
	WinActivate($hWnd)
	;Send("{TAB}{ENTER}")
	ConsoleWrite(@CRLF & "Completed GoPro GDA Installer==================================")
	;WinClose("[CLASS:Qt5QWindowIcon]")
Else
	ConsoleWrite(@CRLF & "FAILED GDA App Startup *******************")
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
