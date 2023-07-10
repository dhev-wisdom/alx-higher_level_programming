#!/usr/bin/python3
"""
Multiplies two matrices using the NumPy module
"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Function multiplies two matrices using the NumPy

    :param m_a: The first matrix.
    :param m_b: The second matrix.
    :return: The resulting matrix after multiplication.

    Examples:
    :param m_a: The first matrix.
    :param m_b: The second matrix.
    :return: The resulting matrix after multiplication.

    Examples:
    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8]])
    array([[19, 22], [43, 50]])

    >>> lazy_matrix_mul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]])
    array([[ 58,  64], [139, 154]])

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]])
    Traceback (most recent call last):
    ...
    ValueError: m_a and m_b can't be multiplied

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 'eight']])
    Traceback (most recent call last):
    ...
    TypeError: m_b should contain only integers or floats

    >>> lazy_matrix_mul([[1, 2], [3, 4]], 'not a matrix')
    Traceback (most recent call last):
    ...
    TypeError: m_b must be a list of lists

    >>> lazy_matrix_mul([], [[1, 2], [3, 4]])
    Traceback (most recent call last):
    ...
    ValueError: m_a can't be empty

    >>> lazy_matrix_mul([[1, 2], [3, 4]], [[5, 6], [7, 8], [9, 10]])
    Traceback (most recent call last):
    ...
    TypeError: each row of m_a must be of the same size or each row of m_b must be of the same size

    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    if len(set(len(row) for row in m_a)) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) > 1:
        raise TypeError("each row of m_b must be of the same size")

    m_a = np.array(m_a)
    m_b = np.array(m_b)

    result = np.matmul(m_a, m_b)

    return result
