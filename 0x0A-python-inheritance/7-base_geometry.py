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
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
