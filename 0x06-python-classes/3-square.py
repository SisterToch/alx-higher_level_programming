#!/usr/bin/python3
"""this is a square class"""


class Square:
    """this is an empty square"""

    def __init__(self, size=0):
        """it however has the size instance"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise("size must be >=0")
        else:
            self.__size = size

    def area(self):
        """calculate the area using the size"""
        return (self.__size ** 2)
