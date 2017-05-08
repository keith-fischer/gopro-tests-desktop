#include <AutoItConstants.au3>
#include <Array.au3> ; Required for _ArrayDisplay only.
#include <WinAPIShPath.au3>
;=================================================
; JENKIN SLAVE MONITOR CONTROLLER
; check if slave process is running
; start slave process
; monitor slave process stdout for errors
; kill, restart slave process uppon errors found in stdout
; continue monitoring stdout errors forever
; this exe can be used in service to be invoked upon host restart

Func KillSlave($pid)
	Local $rc=False
	Return $rc
EndFunc

;java -jar slave.jar -jnlpUrl https://jenkinssd.gopro-platform.com/computer/WinGDA-02/slave-agent.jnlp -secret 41665ec47c535a726e18ee08ea840f5df47e5e46b3b301b3a21018c96fb18ce3

Func StartSlave($slavename, $secret)
	Local $pid = Null
	Local $javaslave = "java -jar C:\Automation\slave.jar -jnlpUrl https://jenkinssd.gopro-platform.com/computer/[[SLAVE]]/slave-agent.jnlp -secret [[SECRET]]"
	Local $comslave = StringReplace($javaslave,"[[SLAVE]]",$slavename)
	$comslave = StringReplace($comslave,"[[SECRET]]",$secret)
	$pid = Run(@ComSpec & $comslave, @SystemDir, @SW_HIDE, $STDERR_CHILD + $STDOUT_CHILD)
	Return $pid
EndFunc

Func CheckForErrors($pid)
	Local $rc=False

	Return $rc
EndFunc



Func MonitorSlave($slavename, $secret)
	Local $pid = StartSlave($slavename, $secret)

EndFunc


Func Example()
    Local $iPID = Run(@ComSpec & " /c DIR Example.au3", @SystemDir, @SW_HIDE, $STDERR_CHILD + $STDOUT_CHILD)
    Local $sOutput = ""
    While 1
        $sOutput = StdoutRead($iPID)
        If @error Then ; Exit the loop if the process closes or StdoutRead returns an error.
            ExitLoop
        EndIf
        MsgBox($MB_SYSTEMMODAL, "Stdout Read:", $sOutput)
    WEnd

    While 1
        $sOutput = StderrRead($iPID)
        If @error Then ; Exit the loop if the process closes or StderrRead returns an error.
            ExitLoop
        EndIf
        MsgBox($MB_SYSTEMMODAL, "Stderr Read:", $sOutput)
    WEnd
EndFunc   ;==>Example


Local $debug=True

if Not (UBound($CmdLine)=2) Then
	ConsoleWrite(@CRLF & "Need slave host name and the secret GUID generated from Jenkins")
	if $debug
		Local $slave = "WinGDA-02"
		Local $secret = "41665ec47c535a726e18ee08ea840f5df47e5e46b3b301b3a21018c96fb18ce3"
		MonitorSlave($slave, $secret)
	EndIf
Else
	Local $slave = $CmdLine[0]
	Local $secret = $CmdLine[1]
	MonitorSlave($slave, $secret)
EndIf
