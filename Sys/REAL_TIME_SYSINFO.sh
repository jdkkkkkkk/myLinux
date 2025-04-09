#!/bin/bash


#----------mem_info----------
tmp_memfree=$(cat /proc/meminfo | grep MemFree)
tmp_memavlb=$(cat /proc/meminfo | grep MemAvailable)
tmp_memcached=$(cat /proc/meminfo | grep Cached | head -n 1)
tmp_memshared=$(cat /proc/meminfo | grep Shmem | head -n 1)
memfree=${tmp_memfree#* }
memavlb=${tmp_memavlb#* }
memcached=${tmp_memcached#* }
memshared=${tmp_memshared#* }


cat /dev/null > ./.realtime_sysinfo
echo -e "mem_free:$memfree\nmem_available:$memavlb\nmem_cached:$memcached\nmem_shared:$memshared" >> ./.realtime_sysinfo
