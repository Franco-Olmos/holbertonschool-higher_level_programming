#!/usr/bin/python3
""" shebang """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ square class """
    def __init__(self, size):
        """ init class """
        self.__size = size
        self.integer_validator("size", self.__size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        """ return """
        return ("[Rectangle] {}/{}".format(self.__size, self.__size))
