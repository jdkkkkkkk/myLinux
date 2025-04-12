#!/bin/bash


source ../.global

set_offline_flag(){
	local line=`grep -n "is_offline" globl.py | head -n1 | cut -d: -f1`
	if [ -n "$line" ];then
		sed -i "${line}s/.*/is_offline = $1/" globl.py
	else
		err "Chat" "can't find \"is_offline\" in globl.py"
	fi
}



echo -e "\033[1;32mWelcome to CHAT, please choose a pattern:\033[0m"
offline_info
flag=0
exit_flag=0
while true
do
	read -r -s -n 1 choice
	case "$choice" in
		"a")
			flag=$(((flag-1)%2))
			;;
		"d")
			flag=$(((flag+1)%2))
			;;
		`echo -e "\n"`)
			exit_flag=1
			;;
		*)
			;;
	esac
	
	if [ "$exit_flag" == 1 ];then
		break
	fi

	echo -e "\033[4F\033[?25l"
	#echo -e "\033[?25l"
	if [ "$flag" == 0 ];then
		offline_info
	else
		online_info
	fi
done

if [ "$flag" == 0 ];then
	set_offline_flag True
else
	set_offline_flag False
fi

python3 "./pycmd.py"
