#!/bin/sh

#_mount=/Volumes/GoPro-MacInstaller
#_mount=/dev/disk2
#echo ${_mount}
#hdiutil detach ${_mount}
#_dmg=/Users/keithfisher/Downloads/GoPro-MacInstaller-0.1.0.1902.dmg
#hdiutil attach ${_dmg}
args=("$@")
_nargs=${#args[*]}
if [ $_nargs -eq 1 ]; then
	_dmg=${args[0]}
	#_mount = "/Volumes/${args[1]}"
	#hdiutil info
	#hdiutil detach /dev/disk2
	
	#hdiutil detach ${_mount}
	
	hdiutil attach ${_dmg}
	
fi
hdiutil info
#read -rsp $'Press enter to continue...\n'


#this works too for sdcard
#diskutil unmountDisk /dev/disk3
#diskutil mountDisk /dev/disk3
