#!bin/bash

reserved_path=$(pwd)
cd /home/brian/MY_TEST/Sys
source ../.global


declare exe_file="./TABLE_SYSTEM_INFO.py"
if [ -z "$1" ];then
	python3 $exe_file "SYS" "./MY_SYSTEM_INFO.sh" "./.sys_info"
	exit 0
fi

case "$1" in
	'-h' | '--help')
		echo -e "\n(self-defined) SYSTEM, version $SYS_version\n"
		echo -e "Usage: show system information [arguments]\nOptions:"
		echo -e "  -h, --help\t\tdisplay this message"
		echo -e "  -v, --version\t\tdisplay version"
		echo -e "  -r, --realtime\tdisplay real-time system-info"
		;;


	'-v' | '--version')
		echo -e "SYSTEM script v$SYS_version"
		;;


	'-r' | '--realtime')
		python3 $exe_file "REALTIME" "./REAL_TIME_SYSINFO.sh" "./.realtime_sysinfo"
		;;


	*)
		unrecognized_option "system" $1
		;;
esac

cd $reserved_path
