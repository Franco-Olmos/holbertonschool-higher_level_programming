#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """class square"""

    def __init__(self, size=0):
        """init class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            self.__size = size
