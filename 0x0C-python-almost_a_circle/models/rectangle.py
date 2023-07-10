#!/usr/bin/python3
"""
Module ---
"""


from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        width property getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width property setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        heigth property getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height property setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x property getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x property setter
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y property getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y property  setter
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        method returns area of rectangle
        """
        area = self.__width * self.__height
        return area

    def display(self):
        """
        method displays rectangle represented with '#'
        """
        x, y = self.__width, self.__height
        for _ in range(y):
            for _ in range(x):
                print("#", end="")
            print("")
