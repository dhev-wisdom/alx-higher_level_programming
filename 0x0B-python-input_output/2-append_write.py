#!/usr/bin/python3
"""Program that opens a text file and appends text into it"""


def append_write(filename="", text=""):
    """Function that opens file (UTF8) and appends `text` at the end"""

    with open(filename, "a+", encoding="utf-8") as f:
        writ = f.write(text)
        return writ
