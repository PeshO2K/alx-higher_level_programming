#!/usr/bin/python3
"""Sqaure Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor func"""
        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get size"""
        return self.width
    @size.setter
    def size(self, value):
        """Set szie"""
        self.width = self.height = value

    def __str__(self):
        """Print Square"""
        sqr = "[Square] ({}) {}/{} - {}"
        return sqr.format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Update attributes"""
        if args and len(args) > 0:
            args = list(args)
            if len(args) > 1:
                args.insert(2, args[1])
            super().update(*args)
        else:
            if 'size' in kwargs:
                kwargs['width'] = kwargs['height'] = kwargs['size']
            super().update(**kwargs)
