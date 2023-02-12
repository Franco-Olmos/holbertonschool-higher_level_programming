#!/usr/bin/python3
""" shebang """


def write_file(filename="", text=""):
    """ writefile """
    with open(filename, "w+") as fin:
        fin.write(text)
        fin.close()
    return len(text)
