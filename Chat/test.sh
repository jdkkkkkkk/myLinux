#!/bin/bash



line=`grep -n "is_offline" globl.py | cut -d: -f1`
echo $line
