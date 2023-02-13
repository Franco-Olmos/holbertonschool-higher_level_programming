#!/usr/bin/python3
""" shebang """

import json
""" import JSON """


def save_to_json_file(my_obj, filename):
    """ save JSON strucutre """

    with open(filename, "w+") as file:
        json.dump(my_obj, file)
        file.close()
