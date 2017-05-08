#!/bin/sh

cd "/Automation/gopro-tests-desktop/GDA/Mac GDA-Studio 3a BAT/"
//node /Automation/gopro-tests-desktop/GDA/GDA_Test_Driver/bin/www 
/Applications/GoPro.app/Contents/MacOS/GoPro GoProPlayerPlugin -testscript "/Automation/gopro-tests-desktop/GDA/Mac GDA-Studio 3a BAT/servermsgloop.js" -testinterval 2000


read -rsp $'Press enter to continue...\n'
