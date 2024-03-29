#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    body_content = response.read()
    print("Body response:")
    print("\t- type:", type(body_content))
    print("\t- content:", body_content)
    print("\t- utf8 content:", body_content.decode('utf-8'))
