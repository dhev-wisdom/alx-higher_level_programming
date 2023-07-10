#!/usr/bin/python3
"""
A module that creates a base class
"""


from base import Base


class Rectangle(Base):
    """
    A base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instance method thar initializes Base class
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """ getter method to return the value of width """
        return self.__width

    @width.setter
    def width(self, val):
        """ public setter method to set the value of width """
        if (type(val) != int):
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    @property
    def height(self):
        """ public getter method to return the value of height """
        return self.__height

    @height.setter
    def height(self, val):
        """ public setter method for height """
        if (type(val) != int):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    @property
    def id(self):
        """ public getter method for id """
        return self.id

    @id.setter
    def id(self, val):
        """ public setter method for id """
        self.id = val

    @property
    def x(self):
        """ Getter method for x """
        return self.__x

    @x.setter
    def x(self, val):
        """ public setter method for x """
        if (type(val) != int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    @property
    def y(self):
        """ public getter method that returns tge value of y """
        return self.__y

    @y.setter
    def y(self, val):
        """ public setter method for y """
        if (type(val) != int):
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val
