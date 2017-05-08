#!/bin/sh

echo "HOME=${HOME}" # All jenkin slaves use autogda user name

_job=Mac_GDA-Studio_3a_BAT #under the workspace the job name
_repo=gopro-tests-desktop
_root="${HOME}/workspace/${_job}"
_gda="/Automation/gopro-tests-desktop/GDA"
_pw="Qwerty1!"
# Run in backgrouns: Localhost simple api Testrail service for brokering testing transactions to the corp testrail server
defaults write com.apple.CrashReporter DialogType none
python "/Automation/gopro-tests-desktop/GDA/python/testrail/restservertestrail.py" &

for i in {1..99}
do
   echo "==========================================="
   echo "$i Run Test ==============================="
   # Reset Quik desktop app: Graceful exit or kill if stuck. Restart resize and position of main Quik window for sikuli control
   #"${_gda}/GDASetWinSize.app/Contents/MacOS/applet"
   osascript /Automation/gopro-tests-desktop/GDA/GDASetWinSize.scpt
   echo "STARTING SIKULI ================================="
   java -Djava.awt.headless=false -jar /Applications/sikuli/SikuliX.app/Contents/Java/sikulix.jar -r "${_gda}/sikuli/gda.sikuli" --args "gda_create_tests-record" "Songs_Regression_MBP10.11-Mac230_6081"

done
# shutdown the testrail service
pkill -f restservertestrail.py

read -rsp $'Press enter to continue...\n'
