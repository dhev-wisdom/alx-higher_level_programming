#!/usr/bin/python3
"""
Module defines an empty class 'BaseGeometry'
"""


class BaseGeometry():
    """
    an empty class
    """

    def area(self):
        """
        public method raises an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        public method validates value<s>
        """

        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        else:
            if value <= 0:
                raise ValueError(f"{name} must be greater than 0")
