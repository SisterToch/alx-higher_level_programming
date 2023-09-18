#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """this inherits from rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        self.id = None
        self.x = x
        self.y = y
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")
    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
