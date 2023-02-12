#!/usr/bin/python3
""" shebang """


def inherits_from(obj, a_class):
    """ function """
    if obj is None and a_class is list:
        return False
    if type(obj) is float and a_class is int:
        return False
    return type(obj) is not a_class
