#!/usr/bin/python3
"""
script that takes in a URL and an email address
sends a POST request to the passed URL with the email as a parameter
and finally displays the body of the response
"""

import requests
import sys


def _requests():
    """ POSTs email to fetched URL """
    url = sys.argv[1]
    email = sys.argv[2]
    params = {'email': email}
    req = requests.get(url, params=params)
    print(req.text)



if __name__ == "__main__":
    _requests()
