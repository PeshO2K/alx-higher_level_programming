#!/usr/bin/python3
"""Module that creates class Square"""


class Square:
    """A class that defines a square.

    Attributes:
        size (int): The size of the square's side.
        position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initializes
        the square with the given size and position.

        area(self): Returns the area of the square.
        my_print(self): Prints the square at its position
        using the "#" character.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square with the given size and position.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.
            position (tuple, optional): The position of the square.
            Defaults to (0, 0).

        Raises:
            TypeError: If the size is not an integer or the position is not
            a tuple of 2 positive integers.
            ValueError: If the size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Gets the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The position of the square.

        Raises:
            TypeError: If the position is not a tuple of 2 positive integers.
        """
        if len(value) != 2 or \
           not isinstance(value, tuple) or \
           not all(isinstance(i, int) and i >= 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """Prints the square at its position using the "#" character.

        The square is printed as a grid of "#" characters, with the
        size of the grid equal to the size of the square's side.
        The position of the square is represented by the number of
        newlines before the grid and the number of spaces before
        each row of the grid.
        """
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
