#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status with requests """

import requests


def _requests():
    """ fetch url with requests package """
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(req.text))
    print("\t- content:", req.text)


if __name__ == "__main__":
    _requests()
