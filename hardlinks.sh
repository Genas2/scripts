#!/bin/bash

declare -A arr
files="$(find . -exec ls -di '{}' \; | sort -n)"

ifs="$IFS"
IFS="
"

for inode_file in $files
do
  inode=${inode_file%% *}
  file=${inode_file#* }

  [ -z "${arr[$inode]}" ] && arr[$inode]="0 "

  arr[$inode]="$(( ${arr[$inode]%% *} + 1 )) ${arr[$inode]#* } $file"
done

IFS="$ifs"

for key in ${!arr[@]}
do
  echo ${arr[$key]}
done
