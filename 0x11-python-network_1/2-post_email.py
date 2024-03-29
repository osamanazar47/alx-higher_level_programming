#!/usr/bin/python3
"""a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email
as a parameter, and displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    email = {'email': sys.argv[2]}
    encode_email = urllib.parse.urlencode(email).encode('utf-8')
    url = sys.argv[1]
    req = urllib.request.Request(url, encode_email, method='POST')
    with urllib.request.urlopen(req) as res:
        content = res.read().decode('utf-8')
        print(content)
