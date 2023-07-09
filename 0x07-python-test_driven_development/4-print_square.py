#!/usr/bin/python3
"""
Module prints square(s) with '#'
"""


def print_square(size):
    """
    Function prints square with the character #
    """
    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")
    if size <= 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
