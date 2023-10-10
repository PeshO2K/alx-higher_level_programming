#!/usr/bin/python3
"""  module rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class rectangle"""

    def __init__(self, size):
        """init rectangle"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """describe rectangle"""
        return "[Square] {}/{}".format(self.__size, self.__size)
