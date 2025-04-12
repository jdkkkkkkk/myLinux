#!/bin/bash


#declare tbs="╚═╝║╬║╔═╗ ═══║║║" now it is in TABLE_SYSTEM_INFO.py
cpu_info=$(echo `cat /proc/cpuinfo | grep name | cut -f2 -d: | uniq -c`)
cpu_num=${cpu_info:0:2}
cpu_type=${cpu_info#* }
cpu_core=$(cat /proc/cpuinfo | grep "cpu cores" | uniq)
core_num=${cpu_core##* }
sys_info=$(cat /etc/fedora-release)
architecture=$(uname -m)
memtotal=$(echo `cat /proc/meminfo | grep MemTotal`)
mem_size=${memtotal#* }


cat /dev/null > ./.sys_info 
echo -e "sys_info:$sys_info\ncpu_num:$cpu_num\ncpu_type:$cpu_type\ncore_num:$core_num\narchitecture:$architecture\nmem_size:$mem_size" >> ./.sys_info
#echo -e "$cpu_num\n$cpu_type\n$core_num\n$sys_info_a $sys_info_b\n$hw_name\n$mem_size" >> /MY_TEST/.sys_info

