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
                        raise ValueError
                except ValueError:
                    print("size must be >= 0")
            else:
                raise TypeError
        except TypeError:
            print("size must be an integer")
