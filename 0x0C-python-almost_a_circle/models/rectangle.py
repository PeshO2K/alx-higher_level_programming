#!/usr/bin/python3
"""
Rectangle module
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Class Constructor
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        get width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """
        get height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """
        get x
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        set x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        get y
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        set y
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Return Area
        """
        return self.__height * self.__width

    def display(self):
        """Prints rectangle with #"""
        rec = "\n" * self.__y
        rec += "\n".join([" " * self.__x + "#" * self.__width
                          for i in range(self.__height)])
        print(rec)

    def __str__(self):
        """Return Object description"""
        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
                f" - {self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        """Update attributes"""
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        else:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary rep"""
        return {'id': self.id, 'width': self.width,
                'height': self.height,
                'x': self.x, 'y': self.y}
