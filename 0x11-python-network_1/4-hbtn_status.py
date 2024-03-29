#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
"""
import requests
req = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t- type: {}".format(type(req.content.decode('utf-8'))))
print("\t- content: {}".format(req.content.decode('utf-8')))
