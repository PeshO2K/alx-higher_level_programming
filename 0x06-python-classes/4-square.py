#!/usr/bin/python3
class Square:
    """A class that defines a square.

    Attributes:
        size (int): The size of the square's side.

    Methods:
        __init__(self, size=0): Initializes the square with the given size.
        area(self): Returns the area of the square.
    """

    def __init__(self, size=0):
        """Initializes the square with the given size.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Gets the size of the square's side.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square's side.

        Args:
            value (int): The size of the square's side.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
