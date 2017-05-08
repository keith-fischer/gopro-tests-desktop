#!/bin/sh

# Prerequisites


# Mac
# 
# Delete GoPro and GoPro Studio from your Applications Folder.
# Delete the "GoPro" folder from macHD/Users/[your user]/Pictures/
# Delete all "com.gopro.xxx" files from macHD/Users/[your user]/library/preferences
# Delete all "com.gopro.xxx" folders from macHD/Users/[your user]/library/Application Support
# Open Keychain Access and delete all com.gopro.desktop entries
# Open Terminal and type the following command: killall cfprefsd 
# Press enter. 
# Empty Trash. 
# Open Activity monitor and make sure that no gopro processes are currently running. If they are 
# manually force quit them, and re-run the killall cfprefsd command.


killall GoPro
killall "GoPro Studio"


cd /

cd ./Applications
echo ./Applications
_temp="./GoPro" # This is the GoPro Folder
echo $_temp
rm -rf $_temp
[ -f "${_temp}" ] && echo "*** Error not Cleaned: The File Exists ${_temp}" || echo "Cleaned:  ${_temp}"

#_temp="./GoPro.app"
#echo $_temp
#rm -rf $_temp
#[ -f "${_temp}" ] && echo "*** Error not Cleaned: The File Exists ${_temp}" || echo "Cleaned:  ${_temp}"

#_temp="./GoPro Studio.app"
#echo $_temp
#rm -rf $_temp
#[ -f "${_temp}" ] && echo "*** Error not Cleaned: The File Exists ${_temp}" || echo "Cleaned:  ${_temp}"

cd $home

cd ./Pictures
echo ./Pictures
_temp="./GoPro" # This removes the GoPro Folder and all files in the folder.
echo $_temp
rm -rf $_temp
[ -f "${_temp}" ] && echo "*** Error not Cleaned: The File Exists ${_temp}" || echo "Cleaned:  ${_temp}"


cd $home

cd ./Library/Preferences
echo ./Library/Preferences
_temp="./com.gopro.desktop-suite.plist"
echo $_temp
rm $_temp
[ -f "${_temp}" ] && echo "*** Error not Cleaned: The File Exists ${_temp}" || echo "Cleaned:  ${_temp}"

_temp="./com.gopro.GoPro-Studio.plist"
echo $_temp
rm $_temp
[ -f "${_temp}" ] && echo "*** Error not Cleaned: The File Exists ${_temp}" || echo "Cleaned:  ${_temp}"

_temp="./com.gopro.GoPro.plist"
echo $_temp
rm $_temp
[ -f "${_temp}" ] && echo "*** Error not Cleaned: The File Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.GoProIDService.plist"
echo $_temp
rm $_temp
[ -f "${_temp}" ] && echo "*** Error not Cleaned: The File Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.plist"
echo $_temp
rm $_temp
[ -f "${_temp}" ] && echo "*** Error not Cleaned: The File Exists ${_temp}" || echo "Cleaned: ${_temp}"


#ls
cd $home

cd "./Library/Application Support"
echo "./Library/Application Support"

_temp="./com.GoPro.goproapp"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.GoProAlertService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.GoProAnalyticsService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.GoProDeviceService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.GoProExporterService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.GoProIDService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.GoProMediaFolderService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.GoProMediaService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.GoProMsgBus"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.GoProMusicService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.GoProPushNotificationService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.GoProShareService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.GoPro.goproapp.GoProUpdateService"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

_temp="./com.gopro.GoPro-Studio"
echo $_temp
rm -rf -- $_temp
[ -d "${_temp}" ] && echo "*** Error not Cleaned: The Directory Exists ${_temp}" || echo "Cleaned: ${_temp}"

#ls

# Need to delete GoPro related keychains.

killall cfprefsd 


#read -rsp $'Press enter to continue...\n'
