#!/bin/sh


_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


cd _DIR
args=("$@")
_nargs=${#args[*]}
if [ $_nargs -eq 2 ]; then
	sh runpkg.sh "${args[0]}"
	#sh runsikuli.sh "${args[1]}"
	sh sikuliBAT.sh
else
    echo "No arg, need 1 arg with path to dmg file"
	sh runpkg.sh "/Automation/temp/GoPro-MacInstaller.dmg"
	sh sikuliBAT.sh
fi

read -rsp $'Press enter to continue...\n'
