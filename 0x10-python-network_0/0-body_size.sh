#!/bin/bash
#a Bash script that takes in a URL, and gives the size of the response
curl -s -w "%{size_download}" -o /dev/null "$1"
