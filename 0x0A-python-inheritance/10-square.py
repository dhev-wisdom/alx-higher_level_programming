#!/usr/bin/python3

"""
Module inherits from class Rectangle
"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Square class inherits from Rectangle
    """

    def __init__(self, size):
        """
        The constructor for Square class
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size ** 2
