#!/usr/bin/python3
def read_file(filename=""):
    """reads and prints text file to stdout"""

    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read())
