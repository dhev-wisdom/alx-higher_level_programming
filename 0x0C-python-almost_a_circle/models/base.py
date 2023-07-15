#!/usr/bin/python3
"""
A module that creates a base class
"""


class Base:
    """
    A base class
    """

    __nb_objects = 0  # A private class attribute

    def __init__(self, id=None):
        """
        Instance method thar initializes Base class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
