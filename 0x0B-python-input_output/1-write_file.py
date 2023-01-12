#!/usr/bin/python3
"""Program that opens a text file and writes into it"""


def write_file(filename="", text=""):
    """Function that opens file (UTF8) and writes `text` into it"""

    with open(filename, "w", encoding="utf-8") as f:
        writ = f.write(text)
        return writ
