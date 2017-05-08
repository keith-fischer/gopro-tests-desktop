#!/bin/sh

#jenkins shell step
#find most recent dmg
#delete older dmg files
#

#_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
#echo "script dir=${_DIR}"
#cd _DIR
#GoPro-MacInstaller-0.1.0.2146.dmg
_root=/Users/keithfisher/workspace/GDA-BAT-Mac/Automation
echo "_root=${_root}"
newf=$(ls -t $_root/temp/* | head -1)
#rm $_root/temp/GoPro-MacInstaller.dmg
echo "newf=${newf}"

for fname in $_root/temp/*.dmg; do
	echo "fname=${fname}"
	if [ "${fname}" = "${newf}" ]; then
		echo "Install file "
	else
		echo "delete file "
		rm $fname
	fi
done

cd /Users/keithfisher/workspace/GDA-BAT-Mac/Automation/gopro-tests-desktop/GDA/
./slave_mount_install_dmg.sh "${newf}"

#read -rsp $'Press enter to exit...\n'

