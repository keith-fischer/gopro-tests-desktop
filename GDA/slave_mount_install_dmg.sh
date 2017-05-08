#!/bin/sh
_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd _DIR

args=("$@")
_nargs=${#args[*]}
if [ $_nargs -eq 1 ]; then
	if [ -f "${args[0]}" ]; then
		echo "starting...${args[0]}"
    	./runpkg.sh "${args[0]}"
    else
    	echo "Invalid Path:${args[0]}"
    fi
else
    echo "debug:Need 1 arg with path to dmg file"
    _arg1="/Users/keithfisher/Downloads/GoPro-MacInstaller-0.1.0.2076.dmg"
    if [ -f "${_arg1}" ]; then
		echo "starting...${_arg1}"
    	./runpkg.sh "${_arg1}"
    else
    	echo "Invalid Path:${_arg1}"
    fi
fi

#read -rsp $'Press enter to exit...\n'

