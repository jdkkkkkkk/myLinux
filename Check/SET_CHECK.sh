#!/bin/bash
                              
reserved_path=$(pwd)
cd /home/brian/MY_TEST/Check
globl_path="../.global"
source $globl_path




find_substr(){
	for tmp in ${my_update_check_wait_list[@]}
	do
		[ "$tmp" == "$1" ] && echo "yes"
	done
}


if [ -z "$1" ];then
	ERR "check" "no input option."
fi

case "$1" in
	'-h' | '--help')
		echo -e "\n(self-defined) SET_CHECK, version $CHECK_version\n"
		echo -e "Usage: check options [arguments]...\nOptions:"
		echo -e "  -h, --help\t\tdisplay this message"
		echo -e "  -v, --version\t\tdisplay version of this script"
		echo -e "  -l, --list\t\tdisplay the list"
		echo -e "  -a, --add\t\tadd pkg-name to the list"
		echo -e "  -d, --del, --delete\tdelete pkg-name of the list (default is the last one)"
		echo -e "  -c, --change\t\tchange pkg-name already in the list"
		echo -e "  -f, --find\t\tfind the pkg-name in the list or not"
		;;


	'-l' | '--list')
		echo -e "$my_update_check_wait_list"
		;;


	'-v' | '--version')
		echo -e "SET_CHECK script v$CHECK_version"
		;;


	'-a' | '--add')
		if [ ! -n "$2" ];then
			err "check" "please input pkg-name."
		fi
	
		if [[ "$my_update_check_wait_list[@]" =~ "${2}" ]];then
			err "check" "\"$2\" already in the list."
		fi

		pkg_info=$(apt -qq list $2 2>/dev/null)
		if test -z "$pkg_info";then
			err "check" "\"$2\" not found, please check again."
		fi
	
		if [[ "$pkg_info" != *"installed"* ]];then
			err "check" "\"$2\" not installed, please try \"apt install $2\"."
		fi

		new_list="$my_update_check_wait_list $2"
		sed -i "s/$my_update_check_wait_list/$new_list/" $globl_path
		;;
	

	'-d' | '--del' | '--delete')		
		if [ ! -n "$2" ];then
			if [ -z "$my_update_check_wait_list" ];then
				err "check" "cannot delete from empty list."
			fi
			sed -i "s/$my_update_check_wait_list/${my_update_check_wait_list% *}/" $globl_path
		else
			flag_d=$(find_substr $2)
			if [[ "$flag_d" == 'yes' ]];then
				tmp_line=$(echo ${my_update_check_wait_list/$2/} | sed -e 's/^[ ]*//g' | sed -e 's/[ ]*$//g')	
				sed -i "s/$my_update_check_wait_list/$tmp_line/" $globl_path
			else
				err "check" "\"$2\" not in list."
			fi
		fi
		;;


	'-c' | '--change')
		if [ ! -n "$2" ] || [ ! -n "$3" ];then
			err "check" "please input pkg-name."
		else
			flag_c1=$(find_substr $2)
			if [[ "$flag_c1" != 'yes' ]];then
				err "check" "\"$2\" not in list."
			fi

			#confirm that $3 is valid or not then do the delete-and-add option
			flag_c2=$(find_substr $3)
			if [[ "$flag_c2" == 'yes' ]];then
				err "check" "\"$3\" already in the list."
			fi

			pkg_info=$(apt -qq list $3 2>/dev/null)
        		if test -z "$pkg_info";then
                		err "check" "\"$3\" not found, please check again."
			fi

			if ! [[ "$pkg_info" == *"installed"* ]];then 
				err "check" "\"$3\" not installed, please try \"apt install $3\""	
			fi
		
			new_list4change=${my_update_check_wait_list//$2/$3}
			sed -i "s/$my_update_check_wait_list/$new_list4change/" $globl_path
		fi
		;;


	'-f' | '-find')
		if [ ! -n "$2" ];then
			err "check" "please input pkg-name."
		else
			flag_f=$(find_substr $2)
			if [[ "$flag_f" == 'yes' ]];then
				echo -e "\"$2\" in the list."
				exit 0
			else
				echo -e "\"$2\" not in list."
				exit 0
			fi
		fi
		;;


	*)
	unrecognized_option "check" $1
esac

cd $reserved_path

