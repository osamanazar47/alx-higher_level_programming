0x11-python-network_1

General
    - How to fetch internet resources with the Python package urllib
    - How to decode urllib body response
    - How to use the Python package requests #requestsiswaysimplerthanurllib
    - How to make HTTP GET request
    - How to make HTTP POST/PUT/etc. request
    - How to fetch JSON resources
    - How to manipulate data from an external service

Tasks:
  0. What's my status? #0:-
    a Python script that fetches https://alx-intranet.hbtn.io/status

  1. Response header value #0:-
    a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.

  2. POST an email #0:-
    a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)

  3. Error code #0:-
    a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).You have to manage urllib.error.HTTPError exceptions and print: Error code: followed by the HTTP status code