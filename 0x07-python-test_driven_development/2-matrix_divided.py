#!/usr/bin/python3
"""
Module contains function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    Function divides all elements of a matrix
    """

    if not isinstance(matrix, list) or \
            not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element/div, 2) for element in row] for row in matrix]
