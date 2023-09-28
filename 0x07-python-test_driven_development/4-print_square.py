#!/usr/bin/python3
"""
Module that prints square
"""


def print_square(size):

    """
    function that prints a square with #.

    Args:
    size(int): the size of square. Positive number

    Returns: Nothing
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)
