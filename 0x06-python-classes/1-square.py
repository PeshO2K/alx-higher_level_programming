#!/usr/bin/python3
class Square:
    """A class that defines a square.

    Attributes:
        __size (int): The size of the square's side.

    Methods:
        __init__(self, size): Initializes the square with the given size.
    """

    def __init__(self, size):
        """Initializes the square with the given size.

        Args:
            size (int): The size of the square's side.
        """
        self.__size = size
