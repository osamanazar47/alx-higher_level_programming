#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""
if __name__ == '__main__':
    import urllib.request
    import urllib.error
    import sys

    try:
        with urllib.request.urlopen(sys.argv[1]) as res:
            content = res.read()
            print(content)
    except urllib.error.HTTPError as err:
        print("Error code: {}".format(err.code))
