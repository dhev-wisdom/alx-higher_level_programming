#!/usr/bin/python3
"""
Module has function tat prints two new lines after certain characters
"""


def text_indentation(text):
    """
    Function prints two new lines after these characters:
    '.', '?', ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punc = ['.', '?', ':']
    lines = []
    line = ""

    for char in text:
        line += char

        if char in punc:
            lines.append(line.strip())
            lines.append("")

            line = ""

    lines.append(line.strip())

    for line in lines:
        print(line)
