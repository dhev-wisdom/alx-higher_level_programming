#!/usr/bin/python3
"""
File contains function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """
    Function returns a list of available fields in an instance of a class
    """
    return dir(obj)
