#!/usr/bin/python3
"""Module creates an emptt class, Square"""


class Square:
    """Square is an empty class that does nothing"""
    def __init__(self, size=0):
        """init function initializes an instance of Square class"""
        try:
            if isinstance(size, int):
                try:
                    if size >= 0:
                        self.__size = size
                    else:
                        raise ValueError("size must be >= 0")
                except ValueError as err:
                    print(err)
            else:
                raise TypeError("size must be an integer")
        except TypeError as err:
            print(err)

    def area(self):
        "area is a method of Square class that returns the area of the square"
        x = self.__size
        return x**2
    def size(self):
        """getter method: returns value of size"""
        return self.__size
    def size(self, value):
        """setter method: sets value of size to passed parameter"""
        try:
            if isinstance(value ,int):
                try:
                    if value >= 0:
                        self.__size = value
                    else:
                        raise ValueError("size must be >= 0")
                except ValueError as err:
                    print(err)
            else:
                raise TypeError("size must be an integer")
        except TypeError as err:
            print(err)
