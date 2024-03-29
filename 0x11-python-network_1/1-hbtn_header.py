#!/usr/bin/python3
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    req_id = response.getheader('X-Request-Id')
    print(req_id)
