#!/usr/bin/python3
"""
script that takes in a URL
sends a request to the URL
and displays the body of the response
"""

import requests
import sys


def _req():
    """ Send request to url and print response """
    url = sys.argv[1]
    req = requests.get(url)
    status_code = req.status_code
    if status_code >= 400:
        print("Error code:", status_code)
    else:
        print(req.text)


if __name__ == "__main__":
    _req()
