#!/bin/bash

dev_base_dir=/Users/nolancotton/dev
counter=0

echo "-----------------------------------"
echo "Pushing all unstaged changes to git"
echo

while read LINE
do
    echo "Switching to $LINE"
    echo "$LINE is complete"
    break
done < "$(ls -ltr $dev_base_dir | grep dr)"

echo 
echo "-----------------------------------"
