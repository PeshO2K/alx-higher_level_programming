#!/usr/bin/python3

"""
Module that adds integers
"""


def add_integer(a, b=98):

    """Adds two integers or floats.

    Args:
    a (number): Float / Integer
    b (number, optional): Float / Integer. Default is 98

    Raises:
    TypeError: if not float / int

    Returns:
    int: sum of a and b

    >>> add_integer("a", 23)
    Traceback (most recent call last):
    TypeError: a must an integer


    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
