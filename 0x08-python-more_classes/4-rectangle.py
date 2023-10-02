#!/usr/bin/python3
"""Module to define rectangle"""


class Rectangle():
    """
    Class defining Rectangle
    
    """
    def __init__(self, width=0, height=0):
        """set width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve width"""
        return self.__width
    
    @width.setter
    def width (self, value):
        """Update value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve height"""
        return self.__height
        
    @height.setter
    def height (self, value):
        """Retrieve value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
        
    def area(self):
        """Area of rectangle"""
        return self.__width * self.__height
    
    def perimeter(self):
        """perimeter of rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
    
    def __str__(self):
        """Prints rectangle  #"""
        rec = ""
        if self.__height > 0 and self.__width > 0:
            rec = "\n".join(["#" * self.__width for i in range(self.__height)])
        return rec

    def __repr__(self):
        """
        String repr for Rectangle
        """
        return f"Rectangle({self.__width}, {self.__height})"
        
