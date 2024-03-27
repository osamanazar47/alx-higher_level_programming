#!usr/bin/env bash
#a Bash script that takes in a URL, and gives the size of the response
curl -w "%content-lenght:" "$1"
