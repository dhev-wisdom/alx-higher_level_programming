#!/usr/bin/python3
"""Module creates an emptt class, Square"""



class Square:
    """Square is an empty class that does nothing"""
    def __init__(self, size=0):
        try:
            if isinstance(size, int):
                try:
                    if size >= 0:
                        self.__size = size
                    else:
                        raise ValueError
                except ValueError:
                    self.__size = 0
                    print("size must be >= 0")
            else:
                raise TypeError:
        except TypeError:
            self.__size = 0
            print("size must be an integer")
