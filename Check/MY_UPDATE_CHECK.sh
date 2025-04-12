#!/bin/bash


source ../.global
declare wait_list=$my_update_check_wait_list
declare -i no_update_pkg_num=0
declare -i updated_pkg_num=0

exe_upgrade(){
	local input=$1
	if [ "$1" == "python3-pip" ];then
		input="pip"
	fi

        local before_ver=$($input --version | sed -n 1p)
        yes y|apt-get install --only-upgrade $1 > /dev/null
        local after_ver=$($input --version | sed -n 1p)
        if [ "$before_ver" == "$after_ver" ];then
		((no_update_pkg_num++))
                echo "$before_ver is already the newest version."
        else
		((updated_pkg_num++))
                echo "upgrade $before_ver to $after_ver successfully."
        fi
}

echo '----------This is still a test----------'
echo -e "Do you want to upgrade the pkgs? ($wait_list)"
read -p 'Please enter [Y/n] ' choice
if [[ "$choice" == Y* ]] || [[ "$choice" == y* ]];then
        for val in ${wait_list[@]};do 
		exe_upgrade $val;
	done
	declare -i total=$(expr $no_update_pkg_num + $updated_pkg_num)
	echo "$updated_pkg_num upgraded, $no_update_pkg_num not upgraded, $total total"

elif [[ $choice == N* ]] || [[ "$choice" == n* ]];then
        echo 'Abort.'
else
        echo $'Actually that\'s an illegal input... whatever'
fi

echo 'Thanks for using this file.'
echo -e "\033[1;3;32;40m----------Welcome to my Fedora40----------\033[0m"
