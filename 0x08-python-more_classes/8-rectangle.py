#!/usr/bin/python3
"""Module creates and empty clasd, Rectangle"""


class Rectangle:
    """Empty class Rectangle"""
    number_of_instances = 0  # Object count
    print_symbol = "#"  # symbol employed by "print()" and "str()" to print

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Getter method that returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter method to set the value of width"""
        try:
            if isinstance(value, int):
                try:
                    if value >= 0:
                        self.__width = value
                    else:
                        raise ValueError("width  must be >= 0")
                except ValueError as err:
                    print(err)
            else:
                raise TypeError("width must be an integer")
        except TypeError as er:
            print(er)

    @property
    def height(self):
        """Getter method to return the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter method to set the vakue of height"""
        try:
            if isinstance(value, int):
                try:
                    if value >= 0:
                        self.__height = value
                    else:
                        raise ValueError("height must be >= 0")
                except ValueError as err:
                    B
                    print(err)
            else:
                raise TypeError("height must be an integer")
        except TypeError as er:
            print(er)

    def area(self):
        """class method to return area of the rectangle"""
        x = self.__width
        y = self.__height
        return x * y

    def perimeter(self):
        """class method to return perimeter of the rectangle"""
        a = self.__width
        b = self.__height
        if a <= 0 or b <= 0:
            return 0
        else:
            x = 2 * a
            y = 2 * b
            return x + y

    def __str__(self):
        """Control the output of "print()" on your class"""
        x = self.__width
        y = self.__height
        __print = ""

        for a in range(y):
            for b in range(x):
                __print += str(self.print_symbol)
            __print += '\n'
        if __print[-1] == '\n':
            __print = __print[:-1]

        return __print

    def __repr__(self):
        """String representation of class that make class"""
        x = str(self.__width)
        y = str(self.__height)

        _print = "Rectangle(" + x + ", " + y + ")"
        return _print

    def __del__(self):
        """Class method to delete instance of class"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """evaluate and return the bigger of the two rectangles"""
        area_1, area_2 = 0, 0
        status = "proceed"
        try:
            if isinstance(rect_1, Rectangle):
                area_1 = rect_1.area()
            else:
                status = "stop"
                raise TypeError("rect_1 must be an instance of Rectangle")
        except TypeError as err:
            print(err)
        try:
            if isinstance(rect_2, Rectangle):
                area_2 = rect_2.area()
            else:
                status = "stop"
                raise TypeError("rect_2 must be an instance of Rectangle")
        except TypeError as err:
            print(err)
        if status == "proceed":
            if area_2 > area_1:
                return rect_2
            else:
                return rect_1
