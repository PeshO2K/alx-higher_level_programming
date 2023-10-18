#!/usr/bin/python3
"""Sqaure Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor func"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Print Square"""
        sqr = "[Square] ({}) {}/{} - {}"
        return sqr.format(self.id, self.x, self.y, self.width)
