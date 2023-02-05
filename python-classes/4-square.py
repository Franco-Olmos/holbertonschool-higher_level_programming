#!/usr/bin/python3
"""define a square class"""


class Square:
    """class square"""

    def __init__(self, size=0):
        """init class"""
        self.__size = size

    @property
    def size(self):
        """return"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return"""
        return self.__size ** 2