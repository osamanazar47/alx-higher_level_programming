#!/usr/bin/python3
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
    body_content = response.read()
    print("Body response:")
    print("    - type:", type(body_content))
    print("    - content:", body_content)
    print("    - utf-8 content:", body_content.decode('utf-8'))
