#!/usr/bin/python3
"""shebang"""


def read_file(filename=""):
    """ readfile """
    with open(filename, 'r') as fin:
        print(fin.read(), end="")
