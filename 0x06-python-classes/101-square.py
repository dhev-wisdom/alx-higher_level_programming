#!/usr/bin/python3
"""Module creates an empty class, Square"""


class Square:
    """Square is an empty class that does nothing"""
    def __init__(self, size=0, position=(0, 0)):
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

        try:
            (pos1, pos2) = position
            if isinstance(pos1, int) & isinstance(pos2, int):
                self.__position = (pos1, pos2)
            else:
                raise TypeError
        except TypeError:
            print("position must be a tuple of 2 positive integers")

    def area(self):
        "area is a method of Square class that returns the area of the square"
        x = self.__size
        return x**2

    @property
    def size(self):
        """getter method: returns value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method: sets value of size to passed parameter"""
        try:
            if isinstance(value, int):
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

    @property
    def position(self):
        """a getter method to get the position of the square"""
        return self.__position

    @position.setter
    def position(self, position):
        """a setter method to set the position of the square"""
        (pos1, pos2) = position
        self.__position = (pos1, pos2)

    def my_print(self):
        """Public instance method to print the square with '#'"""
        x = self.__size
        y = self.__position
        if x > 0:
            for i in range(x):
                print("_" * y[0], end="")
                for j in range(x):
                    print("#", end="")
                print()
        else:
            print()

    def __str__(self):
        """Prints an instance of Square"""
        _print = ""
        x = self.__size
        y = self.__position
        if x > 0:
            if y[1] > 0:
                for i in range(y[1]):
                    _print += '\n'
            for i in range(x):
                for a in range(y[0]):
                    _print += "_"
                for j in range(x):
                    _print += "#"
                _print += '\n'
        else:
            _print += '\n'

        return _print
