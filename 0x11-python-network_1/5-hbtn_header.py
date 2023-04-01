#!/usr/bin/python3
"""
Script sends a request to the URL and displays the value of
the variable X-Request-Id in the response header
"""

import requests
import sys


def _requests():
    """ print value of X-Request-Id from header """
    url = sys.argv[1]
    req = requests.get(url)
    print(req.headers['X-Request-Id'])


if __name__ == "__main__":
    _requests()
