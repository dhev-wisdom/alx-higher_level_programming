#!/usr/bin/python3
"""Program that reads and prints a text file"""


def read_file(filename=""):
    """reads and prints text file(UTF8) to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read())
