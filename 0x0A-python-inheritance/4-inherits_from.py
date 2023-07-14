#!/usr/bin/python3

"""
Module checks if object is instance of soecified class
"""


def inherits_from(obj, a_class):
    """
    function checks if objects is exactly an instance of specified class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
