#!/usr/bin/python3
"""
    cript that takes in a URL, sends a request to the URL and displays the
    values of the X-Request-Id variable found in the header of the response
"""

import urllib.request
import sys


def _import():
    url = sys.argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))

if __name__ == "__main__":
    _import()
