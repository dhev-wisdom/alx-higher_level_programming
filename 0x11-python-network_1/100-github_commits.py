#!/usr/bin/python3
"""
Coding Interview Challenge
"""

import requests
import sys


def _interview():
    """ Holbertin Backend Interview """
    repo = sys.argv[1]
    user = sys.argv[2]
    url = "https://api.github.com/repos/" + user + "/" + repo + "/commits?sha=master&per_page=10"
    req = requests.get(url)
    data = req.json()
    print(data)
    for commit in data:
        print("{}: {}".format(commit['sha'], commit['commit']['author']['name']))


if __name__ == "__main__":
    _interview()
