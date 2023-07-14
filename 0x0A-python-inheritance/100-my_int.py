#!/usr/bin/python3

"""
module contains class MyInt
MyInt is a rebel
It inverts == with !=
Making the True(th) a lie and the False a truth
"""


class MyInt(int):
    """
    class MyInt inherits from the int class
    """

    def __eq__(slef, other):
        """
        method overrides the default equality method
        It makes what should be equal unequal
        """
        return super().__ne__(other)

    def __ne__(slef, other):
        """
        method overrides the default equality method
        It makes what should be unequal equal
        """
        return super().__eq__(other)
