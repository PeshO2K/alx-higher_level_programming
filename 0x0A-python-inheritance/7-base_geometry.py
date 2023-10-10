#!/usr/bin/python3
"""
Empty Class
"""


class BaseGeometry():
    """
    Empty class
    """
    def area(self):
        """
        Function raise exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function validates value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
