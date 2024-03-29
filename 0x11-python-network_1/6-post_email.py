#!/usr/bin/python3
"""
a Python script that takes in a URL and an email address
, sends a POST request to the passed URL with the email
as a parameter, and finally displays the body of the response.
"""

if __name__ == '__main__':
    import sys
    import requests
    email = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data=email)
    print("Your email is", res.content)
