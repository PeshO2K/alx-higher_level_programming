#!/usr/bin/python3
"""Module that creates class Square"""


class Square:
    """A class that defines a square.

    Attributes:
        __size (int): The size of the square's side.

    Methods:
        __init__(self, size=0): Initializes the square with the given size.
    """

    def __init__(self, size=0):
        """Initializes the square with the given size.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
