#!/bin/sh

# Prerequisites


# Mac
# 
# Delete GoPro and GoPro Studio from your Applications Folder.
# Delete the "GoPro" folder from macHD/Users/[your user]/Pictures/
# Delete all "com.gopro.xxx" files from macHD/Users/[your user]/library/preferences
# Delete all "com.gopro.xxx" folders from macHD/Users/[your user]/library/Application Support
# Open Terminal and type the following command: killall cfprefsd 
# Press enter. 
# Empty Trash.

killall GoPro
killall "GoPro Studio"
cd $home

cd ./Library/Preferences
echo ./Library/Preferences
_temp="./com.gopro.desktop-suite.plist"
echo $_temp
rm $_temp
[ -f "${_temp}" ] && echo "*** Error: The File Exists" || echo "The File Does Not Exist"

_temp="./com.gopro.GoPro-Studio.plist"
echo $_temp
rm $_temp
[ -f "${_temp}" ] && echo "*** Error: The File Exists" || echo "The File Does Not Exist"

_temp="./com.gopro.GoPro.plist"
echo $_temp
rm $_temp
[ -f "${_temp}" ] && echo "*** Error: The File Exists" || echo "The File Does Not Exist"

_temp="./com.GoPro.goproapp.GoProIDService.plist"
echo $_temp
rm $_temp
[ -f "${_temp}" ] && echo "*** Error: The File Exists" || echo "The File Does Not Exist"

_temp="./com.GoPro.goproapp.plist"
echo $_temp
rm $_temp
[ -f "${_temp}" ] && echo "*** Error: The File Exists" || echo "The File Does Not Exist"


#ls
cd $home

cd "./Library/Application Support"
echo "./Library/Application Support"

_temp="./com.GoPro.goproapp.GoProAlertService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.GoPro.goproapp.GoProAnalyticsService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.GoPro.goproapp.GoProDeviceService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.GoPro.goproapp.GoProExporterService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.GoPro.goproapp.GoProIDService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.GoPro.goproapp.GoProMediaFolderService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.GoPro.goproapp.GoProMediaService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.GoPro.goproapp.GoProMsgBus"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.GoPro.goproapp.GoProMusicService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.GoPro.goproapp.GoProPushNotificationService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.GoPro.goproapp.GoProShareService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.GoPro.goproapp.GoProUpdateService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.gopro.GoPro-Studio"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.GoPro.goproapp"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"

_temp="./com.GoPro.goproapp.GoProExporterService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"


_temp="./com.GoPro.goproapp.GoProIDService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"


_temp="./com.GoPro.goproapp.GoProMsgBus"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"


_temp="./com.GoPro.goproapp.GoProMusicService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"


_temp="./com.GoPro.goproapp.GoProUpdateService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error: The Directory Exists" || echo "The Directory Does Not Exist"



killall cfprefsd 

_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd _DIR
args=("$@")
_nargs=${#args[*]}
if [ $_nargs -eq 1 ]; then
	echo "args[0] with path to dmg file"
	echo "installing...${args[0]}"
	cd /usr/local/bin/
    sudo -S /usr/local/bin/installpkg -i "${args[0]}"
else
    echo "No arg, need 1 arg with path to dmg file"
    
fi

#read -rsp $'Press enter to continue...\n'
