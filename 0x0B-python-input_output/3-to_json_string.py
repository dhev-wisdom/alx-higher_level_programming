#!/usr/bin/python3
import json
"""Program to return JSON representation of an object string"""


def to_json_string(my_obj):
    """Function to convert string to JSON and return result"""

    js = json.dumps(my_obj)
    return js

if __name__ = "__main__":
    to_json_string(my_obj)
