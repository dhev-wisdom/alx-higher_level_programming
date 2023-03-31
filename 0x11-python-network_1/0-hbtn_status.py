#!/usr/bin/python3
""" Python script fetches `https://alx-intranet.hbtn.io/status` """

import urllib.request


with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    body = response.read()
    print("Body response:$")
    print("    - type:", type(body))
    print("    - content:", body)
    print("    - utf8 content:", body.decode('utf-8'))
