#!/usr/bin/python3
"""
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""

import sys
import requests


def _req():
    """ Fetch user_id with username and password """
    url = "https://api.github.com/user"
    username = sys.argv[1]
    pw = sys.argv[2]
    auth = requests.auth.HTTPBasicAuth(username, pw)
    req = requests.get(url, auth=auth)
    print(req.json()["id"])


if __name__ == "__main__":
    _req()
