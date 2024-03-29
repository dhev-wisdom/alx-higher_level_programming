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
        m, n = self.__x, self.__y

        for _ in range(n):
            print("")
        for _ in range(y):
            for _ in range(m):
                print(" ", end="")
            for _ in range(x):
                print("#", end="")
            print("")

    def update(self, *args, **kwargs):
        """
        Method to update attributes
        """
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Return dictionary representation of Rectangle class
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        the standard str function that defines what a class prints
        """
        return (
                f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - "
                f"{self.__width}/{self.__height}"
        )
