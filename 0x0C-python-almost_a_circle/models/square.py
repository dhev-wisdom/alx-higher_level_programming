#!/usr/bin/python3

"""
Module contains class Square that inherites from the Rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(se;f):
        """
        public getter method for @size
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        public setter method for the size property
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        String representation of Square object
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)
