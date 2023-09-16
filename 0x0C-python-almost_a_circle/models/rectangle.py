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

