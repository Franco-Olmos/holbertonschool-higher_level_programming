#!/usr/bin/python3
""" shebang """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ rectangle class """
    def __init__(self, width, height):
        """ init class """
        self.__width = width
        self.__height = height
        self.integer_validator("height", self.__height)
        self.integer_validator("width", self.__width)

    def area(self, size=0):
            return self.__width * self.__height

    def __str__(self):
        """ print str """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
