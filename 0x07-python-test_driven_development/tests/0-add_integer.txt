#!/usr/bin/python3

"""
Test module
"""


def add_integer(a, b=98):
    """
    Adds two integers

    :param a: the first integer
    :param b: the second integer
    :return: the addition of a and b

    Examples

    >>> add_integer(5, 3)
    8

    >>> add_integer(2, 120)
    122

    >>> add_integer('a', 2)  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer

    >>> add_integer(120, 'gree')  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer

    >>> add_integer(120.4, 20.9)
    140

    >>> add_integer(-10, 20)
    10

    >>> add_integer(20)
    118

    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return int(a + b)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
