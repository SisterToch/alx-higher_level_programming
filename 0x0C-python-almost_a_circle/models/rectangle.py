#!/usr/bin/python3
"""This module is for rectangle"""

from models.base import Base


class Rectangle(Base):
    """we are inheriting base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    """the getter functions"""
    @width property
    def width(self):
        return self.__width

    @height property
    def height(self):
        return self.__height

    @x property
    def x(self):
        return self.__x

    @y property
    def y(self):
        return self.__y

    """the setter functions"""
 @width.setter
    def width(self, value):
        """Sets the value for width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")

        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Sets the value for height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")

        if value <= 0:
            raise ValueError("height must be > 0")

        self.__height = value

    @x.setter
    def x(self, value):
        """Sets the value for x"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")

        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @y.setter
    def y(self, value):
        """Sets the value for y"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")

        if value < 0:
            raise ValueError("y must be >= 0")

        self.__y = value
