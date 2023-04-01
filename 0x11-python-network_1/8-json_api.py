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
    if len(sys.argv) > 0:
        q = sys.argv[1]
    else:
        q = ""

    payload = {"q": q}

    req = requests.post(url, data=payload)

    try:
        if req.json():
            print("[{}] {}".format(req.json()['id'], req.json()['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    _req()
