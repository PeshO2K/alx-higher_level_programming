#!/usr/bin/python3
"""
Module rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class rectangle
    """
    def __init__(self, size):
        """
        constructor rectangle
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        area
        """
        return super().area()
