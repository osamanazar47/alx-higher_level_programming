#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to
the URL and displays the body of the response (decoded in utf-8).
manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code
"""

if __name__ == '__main__':
    import sys
    import requests
    import requests.exceptions

    try:
        res = requests.get(sys.argv[1])
        res.raise_for_status()
        print(res.content)
    except requests.exceptions.HTTPError as err:
        print("Error code:", err)