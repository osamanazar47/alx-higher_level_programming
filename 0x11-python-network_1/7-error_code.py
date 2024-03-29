#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8).
manage urllib.error.HTTPError exceptions and print:
Error code: followed by the HTTP status code
"""

if __name__ == '__main__':
    import sys
    import requests

    res = requests.get(sys.argv[1])
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
    else:
        print(res.text)
