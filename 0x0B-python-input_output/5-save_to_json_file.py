#!/usr/bin/python3
"""Progrqm that writes an Object to a text file, using a JSON representation"""


import json as js


def save_to_json_file(my_obj, filename):
    """Function to write object to text file using JSON"""

    with open(filename, "w", encoding="utf-8" as f:
            js.dump(my_obj, f)
