#!/bin/sh
_root=/Automation/Sikuli
_findA=img-verify-7.png
_findB=img-verify-3.png
_findC=img-verify-11.png
_findD=img-verify-15.png
_findE=img-verify-region.png
java -Djava.awt.headless=false -jar /Applications/sikuli/SikuliX.app/Contents/Java/sikulix.jar -r "${_root}/cmd.sikuli" --args "/Automation/Sikuli/img-region.png" "${_findA}"
java -Djava.awt.headless=false -jar /Applications/sikuli/SikuliX.app/Contents/Java/sikulix.jar -r "${_root}/cmd.sikuli" --args "/Automation/Sikuli/img-region.png" "${_findB}"
java -Djava.awt.headless=false -jar /Applications/sikuli/SikuliX.app/Contents/Java/sikulix.jar -r "${_root}/cmd.sikuli" --args "/Automation/Sikuli/img-region.png" "${_findC}"
java -Djava.awt.headless=false -jar /Applications/sikuli/SikuliX.app/Contents/Java/sikulix.jar -r "${_root}/cmd.sikuli" --args "/Automation/Sikuli/img-region.png" "${_findD}"
java -Djava.awt.headless=false -jar /Applications/sikuli/SikuliX.app/Contents/Java/sikulix.jar -r "${_root}/cmd.sikuli" --args "/Automation/Sikuli/img-region.png" "${_findE}"

read -rsp $'Press enter to continue...\n'
