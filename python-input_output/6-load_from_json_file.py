#!/usr/bin/python3
""" shebang """


import json
""" import JSON """


def load_from_json_file(filename):
    """ turn object from JSON """
    with open(filename, "r") as file:
        return json.load(file)
