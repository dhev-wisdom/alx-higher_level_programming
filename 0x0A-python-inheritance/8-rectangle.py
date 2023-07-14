#!/usr/bin/python3

"""
Module inherits from class BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        The constructor for Rectangle class
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
