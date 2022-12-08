#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for ky in a_dictionary.keys():
        if key == ky:
            del a_dictionary[ky]
    return a_dictionary
