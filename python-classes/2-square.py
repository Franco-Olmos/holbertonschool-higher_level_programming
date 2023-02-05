#!/usr/bin/python3
""" Class that defines a Square """


class Square:
    """ Class Square """

	def __init__(self, __size=0):
	    """ Init class"""
            if (type(__size) is not int):
                raise TypeError("size must be an integer")
	    if not (type(__size) is >= 0):
		raise ValueError("size must be >= 0")
            self.__size = __size
