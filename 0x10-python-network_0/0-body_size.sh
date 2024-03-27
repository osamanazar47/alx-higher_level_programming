#!usr/bin/env bash
#a Bash script that takes in a URL, and gives the size of the response
size=$(curl -s -w "%{size_download}" -o /dev/null "$1")
echo "$size"
