#!/usr/bin/python3
"""Rectangle Module"""
from models.base import Base

class Rectangle(Base):
    """Rectangle class"""
    def __init__(self,  width, height, x=0, y=0, id=None):
        """Initialize class"""        
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width"""
        self.__validate(value, "width") 
        self.__width = value

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self,value):
        """Set height
        Args:
            value (int): height of Rectangle. Must be int
        """
        self.__validate(value, "height")            
        self.__height = value

    @property
    def x(self):
        """Get x"""
        return self.__x

    @x.setter
    def x(self,value):
        """Set x"""
        self.__validate(value, "x")            
        self.__x = value

    @property
    def y(self):
        """Get y"""
        return self.__y

    @y.setter
    def y(self,value):
        """Set y"""
        self.__validate(value, "y")             
        self.__y = value
    

    def __validate(self, attr_value, attr_name):
        if not isinstance(attr_value, int):
            raise TypeError(f"{attr_name} must be an integer")
        elif attr_name in ["x", "y"] and attr_value < 0:
            raise ValueError(f"{attr_name} must be >= 0")
        elif attr_name in ["width", "height"] and attr_value <= 0:
            raise ValueError(f"{attr_name} must be > 0")
    
    def area(self):
        """Area of Rectangle"""
        return self.__width * self.__height 
    
    def display(self):
        """Displays rectangle"""
        rec = "\n" * self.__y
        rec += "\n".join([" " * self.__x + "#" * self.__width
                          for i in range(self.__height)])
        print(rec)

    def __str__(self):
        """String represntation"""
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"
    
    def update(self, *args, **kwargs):
        """Update attributes"""
        attr = ["id", "width", "height", "x", "y"]
        if args and len(args) > 0:
            for i, value in enumerate(args):
                if i < len(args):
                    setattr(self, attr[i], value)
        else:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)
    
    def to_dictionary(self):
        """Dictionary representation of Rectangle"""
        return {"id" : self.id, "width" : self.width,
                "height" : self.height, "x" : self.x,
                "y" : self.y}
        


        

       
