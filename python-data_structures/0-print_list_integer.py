#!/usr/bin/python3

def print_list_integer(my_list=[]):
    n = 0
    for n in range(0, len(my_list)):
        print("{:d}".format(my_list[n]))
