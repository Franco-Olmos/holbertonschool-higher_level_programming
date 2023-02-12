#!/usr/bin/python3
""" shebang """


class MyList(list):
    """ class """
    def print_sorted(self):
        aux = list.copy(self)
        sorted_aux = aux.sort()
        print(aux)
