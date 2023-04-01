#!/usr/bin/python3
"""
script that takes in a URL
sends a request to the URL
and displays the body of the response (decoded in utf-8)
"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
import sys


def error_handling():
    """ Account for possible errors while fetching url """
    url = sys.argv[1]
    req = Request(url)
    try:
        with urlopen(req) as response:
            body = response.read().decode('utf-8')
            print(body)
    except HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    error_handling()
