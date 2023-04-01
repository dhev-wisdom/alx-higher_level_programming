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
    payload = {"q": q}

    req = requests.post(url, data=payload)

    try:
        req = req.json()
        if req:
            print("[{}] {}".format(req.id, req.name))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    _req()
