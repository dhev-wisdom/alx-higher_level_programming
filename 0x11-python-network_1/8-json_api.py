#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""

import sys
import requests


def _req():
    """ Handle url fetch with try catch and json """
    url = "http://0.0.0.0:5000/search_user"
    try:
        arg = sys.argv[1]
        q = arg
    except IndexError:
        q = ""
    # query_string = url + "?" + q
    req = requests.post(url, data=q)
    if req.json() and len(req.json()) > 0:
        req = req.json()
        print("[{}] {}".format(req.id, req.name))
    elif len(req.json()) < 1:
        print("No result")
    else:
        print("Not a valid JSON")


if __name__ == "__main__":
    _req()
