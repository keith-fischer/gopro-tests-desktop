#!/bin/sh

# 
# _cd="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
# echo ${_cd}
# _detach="${_cd}/dmgdetach.sh"
# echo ${_detach}
# sh ${_detach} GoPro-MacInstaller
# _attach="${_cd}/dmgattach.sh"
# echo ${_attach}
# _mount="${_attach} /Users/keithfisher/Downloads/GoPro-MacInstaller-0.1.0.1902.dmg"
# echo ${_mount}
# sh ${_mount}
sudo installer -store -pkg "/GoPro-MacInstaller/GoPro.pkg" -target /


read -rsp $'Press enter to continue...\n'


#_mount=/Volumes/GoPro-MacInstaller
#_mount=/dev/disk2
#echo ${_mount}
#hdiutil detach ${_mount}
#_dmg=/Users/keithfisher/Downloads/GoPro-MacInstaller-0.1.0.1902.dmg
#hdiutil attach ${_dmg}

#read -rsp $'Press enter to continue...\n'


#this works too for sdcard
#diskutil unmountDisk /dev/disk3
#diskutil mountDisk /dev/disk3
