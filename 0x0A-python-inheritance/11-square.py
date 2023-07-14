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
        """
        public method handles the area of a square object
        """
        return self.__size ** 2

    def __str__(self):
        """
        The official string representaion of the class Square
        The return when you run print(<Square object>)
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
