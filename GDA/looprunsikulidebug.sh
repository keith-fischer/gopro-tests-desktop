#!/bin/sh


_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"


cd _DIR

for i in `seq 1 999`;
	do
		echo "*********************************************"
		echo "*********************************************"
		echo ">>> ${i} <<<"
		sh runsikulidebug.sh 
done    
 
read -rsp $'Press enter to continue...\n'
