#Region ;**** Directives created by AutoIt3Wrapper_GUI ****
#AutoIt3Wrapper_Outfile=installerversioncleanup.exe
#AutoIt3Wrapper_Outfile_x64=installerversioncleanup64.exe
#AutoIt3Wrapper_Compile_Both=y
#AutoIt3Wrapper_UseX64=y
#AutoIt3Wrapper_Change2CUI=y
#Tidy_Parameters=/gd /gds
#EndRegion ;**** Directives created by AutoIt3Wrapper_GUI ****

#include <Array.au3>
#include <AutoItConstants.au3>
#include <Constants.au3>
#include <Date.au3>
#include <FileConstants.au3>
#include <WinAPIFiles.au3>

;1. establish installer dir
;2. iterate files
;3. find newest file
;4. delete the old files


;-------------------------------------
;
; return Null no file found or an array list of file names
Func getFileList($dirpath,$filter)
	FileChangeDir($dirpath)
	ConsoleWrite(@CRLF & "Found Dir: " & $dirpath )
	Local $hSearch = FileFindFirstFile($filter)
	Local $flist[60]
	Local $idx=0
	If $hSearch = -1 Then
		FileClose($hSearch)
        Return Null
    EndIf


	While 1
		$idx = $idx+1
        $flist[$idx] = FileFindNextFile($hSearch)
        ; If there is no more file matching the search.
        If @error Then ExitLoop
		ConsoleWrite(@CRLF & "Found: " & $flist[$idx] )
    WEnd
	FileClose($hSearch)

	Return $flist
EndFunc

Func DoCleanup($installpath,$flist)
	FileChangeDir($installpath)
	$sz = UBound($flist,$UBOUND_ROWS)-1
	$f= Null
	Local $fdt[60]
	Local $dt[6]
	Local $sdt
	local $path
	local $diff
	Local $keepidx=99
	Local $Min=99999999
	Local $target
	ConsoleWrite(@CRLF & "Found Dir: " & $installpath )
	For $i = 1 To $sz
		$f=$flist[$i]
		ConsoleWrite(@CRLF & String($i))
		if $f=Null Or $f="" Then
			$sz=$i-1
			ExitLoop
		Else
			$path = $installpath & "\" & $f
			$dt = FileGetTime($path, $FT_MODIFIED, $FT_ARRAY ) ;$FT_STRING) ; ,$FT_ARRAY )
			$sdt = FileGetTime($path, $FT_MODIFIED, $FT_STRING ) ;$FT_STRING) ; ,$FT_ARRAY )
			ConsoleWrite(@CRLF & $sdt )
			if $sdt Then
			;"1970/01/01 00:00:00"
				$sdt = $dt[0] & "/" & $dt[1] & "/" & $dt[2] & " " & $dt[3] & ":" & $dt[4] & ":" & $dt[5]
				$diff = _DateDiff('s',$sdt,_NowCalc())
				ConsoleWrite(@CRLF & String($sdt ))
			;
			;$fdt[$i]=$sdt
			;ConsoleWrite(@CRLF & String($i) & "array: " & $path & "-" & String($diff))

				if $Min>$diff Then
					$Min=$diff
					$keepidx = $i
				EndIf
			EndIf
		EndIf
	Next
	Local $del=0
	if $keepidx=99 Then
		ConsoleWrite(@CRLF & String($i) & "Installer Cleanup FAILED: No Installer Target Found")
		Exit(1)
	EndIf
	For $i = 1 To $sz
		if Not($i = $keepidx) Then
			FileDelete($installpath & "\" & $flist[$i])
			Sleep(1)
			if FileExists($installpath & "\" & $flist[$i]) Then
				ConsoleWrite(@CRLF & String($i) & "Delete FAILED: " & $flist[$i])
				$del +=1
			Else
				ConsoleWrite(@CRLF & String($i) & "Delete: " & $flist[$i])
			EndIf
		Else
			ConsoleWrite(@CRLF & String($i) & "Found Target: " & $installpath & "\" & $flist[$i])
			$target =  $installpath & "\" & $flist[$i]
		EndIf
	Next
	if $del>0 Then
		ConsoleWrite(@CRLF & String($i) & "Installer Cleanup FAILED: Old installers are not deleted")
		Exit(1)
	Else
		If FileExists($installpath & "\" & $flist[$keepidx]) Then
			ConsoleWrite(@CRLF & "Target Install File: " & $flist[$keepidx] )
		Else
			ConsoleWrite(@CRLF & String($i) & "Installer Cleanup FAILED:No installer.exe found")
			Exit(1)
		EndIf
	EndIf
	Return $target
EndFunc

Local $jenkins="C:\Win_GDA-Studio_3a_BAT\"
Local $installpath = $jenkins & "temp"
;Local $installpath="C:\Users\" & EnvGet("USERNAME") & "\workspace\Win_GDA-Studio_3a_BAT\Automation\temp\"

if $CmdLine[0]>0 Then
	$installpath=$CmdLine[1] ;path to dir
	ConsoleWrite(@CRLF & "Found cmd path: " & $installpath )
EndIf

if Not FileExists($installpath) Then
	$installpath = $jenkins & "temp"
	;$installpath = "C:\Users\" & EnvGet("USERNAME") & "\workspace\Win_GDA-Studio_3a_BAT\Automation\temp\"
	ConsoleWrite(@CRLF & "Using default path: " & $installpath )
EndIf
if Not FileExists($installpath) Then
	ConsoleWrite(@CRLF & "Stopped: No path to the installer.exe dir, C:\my\path\to\installers" )
	Exit(1)
EndIf


;========================
$flist = getFileList($installpath, "GoPro-WinInstaller-*.exe")

if $flist = Null Then
	ConsoleWrite(@CRLF & "No files found" )
	Exit(1)
EndIf

Local $installer = DoCleanup($installpath,$flist)

