#!/usr/bin/python3
"""
a Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
if __name__ == '__main__':
    import sys
    import requests

    username = sys.argv[1]
    password = sys.argv[2]
    res = requests.get('https://api.github.com/user', auth=(username, password))
    json_data = res.json()
    print(json_data['id'])
