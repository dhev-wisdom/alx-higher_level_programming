#!/usr/bin/python3

"""
Module has function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, attr, val):
    """
    Function adds new attr to obj if possible
    Function takes three parameters
    1. object
    2. attribute
    3. value
    """

    if hasattr(obj, "__dict__"):
        setattr(obj, attr, val)

    else:
        raise TypeError("can't add new attribute")
