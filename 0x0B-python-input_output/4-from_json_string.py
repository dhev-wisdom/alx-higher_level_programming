#!/usr/bin/python3
"""JSON Module: Program to convert JSON representation to original object"""


import json as js


def from_json_string(my_str):
    """Function to convert from json to object"""

    return js.loads(my_str)
