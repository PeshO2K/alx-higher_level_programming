#!/usr/bin/python3
"""Rectangle Module"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """Class representing square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Class ocnstructor"""
        self.size = size
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        """Get size"""
        return self.width
    
    @size.setter
    def size(self, value):
        """Set size"""
        self.width = self.height = value
        

    

    def __str__(self):
        """string representation of sqaure"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
    
    def update(self, *args, **kwargs):
        """Update attributes"""
        attr = ["id", "size", "x", "y"]
        if args and len(args) > 0:
            for i, value in enumerate(args):
                if i < len(args):
                    setattr(self, attr[i], value)
        else:
            for key, value in kwargs.items():
                if key in attr:
                    setattr(self, key, value)
    

    def to_dictionary(self):
        """Dictionary representation"""
        return {'id': self.id, 'size': self.width,
                'x': self.x, 'y': self.y}
