#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
if __name__ == '__main__':
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    res = requests.get('https://api.github.com/user', auth=auth)
    json_data = res.json()
    print(json_data['id'])
