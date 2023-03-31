#!/usr/bin/python3
""" 
    cript that takes in a URL, sends a request to the URL and displays the value of
    the X-Request-Id variable found in the header of the response
"""

from urllib.request import  urlopen, Request
from urllib.parse import urlencode
import sys



url = sys.argv[1]
req = Request(url)
with urlopen(req) as response:
    print(response.getheader('X-Request-Id'))
