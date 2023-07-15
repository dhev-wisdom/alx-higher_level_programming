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
    def size(self):
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

    def update(self, *args, **kwargs):
        """
        Update attributes of Square
        """
        attrs = ['id', 'size', 'x', 'y']

        if args:
            for i, arg in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], arg)

        elif kwargs:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns dictionary representation od=f class Square
        """
        dict_ = {"id": self.id, "size": self.size, "y": self.y, "x": self.x}
        return dict_

    def __str__(self):
        """
        String representation of Square object
        """
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)
