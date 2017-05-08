#!/usr/bin/env bash

##########################################
# BAT Mac Installer Test
# pass dmg argument to override the debug test default
##########################################
args=("$@")
_dmg="/Users/keithfisher/Downloads/GoPro_Quik-MacInstaller-2.3.0.6081.dmg"
_nargs=${#args[*]}
if [ $_nargs -eq 1 ]; then
	_dmg="${args[0]}"
fi

_installer="/System/Library/CoreServices/Installer.app/Contents/MacOS/Installer"
_pkg="/Volumes/GoPro Quik-MacInstaller/GoPro Quik.pkg"
_pw="Qwerty1!"
_pyaccess="/Automation/gopro-tests-desktop/GDA/python/MacInstaller/installer_accessibility.py"
_py=/usr/bin/python
_diskmount=/dev/disk2s1
echo "DEPLOY QUIK INSTALLER ${_dmg}"
echo "INSTALL PKG: ${_pkg}"

#echo -e ${_pw} | sudo -S "${_installer}" "${_pkg}"
#exit $?

hdiutil info
echo "DETACH DMG"
hdiutil detach "${_diskmount}"
sleep 10s
hdiutil info
echo "ATTACH DMG"
hdiutil attach "${_dmg}"

echo "WAIT FOR DMG MOUNT"
sleep 20s
hdiutil info
sleep 1s
echo -e ${_pw} | sudo -S "${_installer}" "${_pkg}" &

echo "WAIT FOR INSTALLER STARTUP"
sleep 20s

${_py} ${_pyaccess}
ret_acc=$? #check for non zero exit id

echo "DETACH DMG"
hdiutil detach "${_diskmount}"
hdiutil info
# TODO
#Eval UI properties report with baseline report
#/usr/bin/python /Automation/gopro-tests-desktop/GDA/python/MacInstaller/eval_gui_report.py
#ret_eval=$?
# report GUI report tests
#if [ $ret_eval -ne 0 ]; then

# Dont run Quik BAT if installer tests failed
if [ $ret_acc -ne 0 ]
then
     #Handle failure
     echo "QUIK INSTALLER FAILED<<<<<<<<<<<<<<"
     echo "killing Installer"
     _ps_name="Installer"
	 _pid=$(pidof ${_ps_name})
     echo "pid=${_ps_name}"
     echo -e ${_pw} | sudo -S kill -9 ${_pid}
     #read -rsp $'Press enter to continue...\n'
else
	echo "START QUIK >>>>>>>>>>>>>>>>>>>>"
	"/Applications/GoPro Quik.app/Contents/MacOS/GoPro Quik"
fi
exit $?

# chain Quik GUI automation here
# Quik process & main window should be available
#read -rsp $'Press enter to continue...\n'
