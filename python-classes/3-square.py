#!/usr/bin/python3
""" Class square """


class Square:
    """ Class Square """
    def __init__(self, __size=0):
	""" Init """
        self.__size = __size

    def area(self):
        area_ = int(self.__size) ** 2
     	return area_
