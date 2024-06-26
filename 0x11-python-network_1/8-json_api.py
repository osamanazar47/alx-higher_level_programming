#!/usr/bin/python3
"""
a Python script that takes in a letter and sends
a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
if __name__ == '__main__':
    import requests
    import sys

    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    q = {"q": letter}
    url = "http://0.0.0.0:5000/search_user"
    res = requests.post(url, data=q)
    try:
        json_data = res.json()  # Parse JSON response
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
