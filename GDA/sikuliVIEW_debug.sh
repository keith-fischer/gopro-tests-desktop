#!/bin/sh


#killall SikuliX
echo "HOME=${HOME}" # All jenkin slaves use autogda user name


_job=Mac_GDA-Studio_3a_BAT #under the workspace the job name
_repo=gopro-tests-desktop
_root="${HOME}/workspace/${_job}"
_gda="/Automation/gopro-tests-desktop/GDA"
#java -Djava.awt.headless=false -jar /Applications/sikuli/SikuliX.app/Contents/Java/sikulix.jar -r "/Users/autogda/workspace/Mac GDA-Studio 3a BAT/gopro-tests-desktop/GDA/sikuli/gda.sikuli"
java -Djava.awt.headless=false -jar /Applications/sikuli/SikuliX.app/Contents/Java/sikulix.jar -r "${_gda}/sikuli/gda.sikuli" --args gda_view_tests-record

#"/Applications/sikuli/runsikulix" -c -d 3 -l "${_root}/Automation/results/gda" -r "${_gda}/sikuli/gda.sikuli"
read -rsp $'Press enter to continue...\n'
