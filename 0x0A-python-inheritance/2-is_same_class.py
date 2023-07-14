#!/usr/bin/python3

"""
Module checks if object is instance of soecified class
"""


def is_same_class(obj, a_class):
    """
    function checks if objects is exactly an instance of specified class
    """
    if type(obj) is a_class:
        return True
    else:
        return False
