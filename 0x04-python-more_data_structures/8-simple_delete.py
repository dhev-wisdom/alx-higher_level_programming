#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for ky in a_dictionary.keys():
        if key == ky:
            a_dictionary.pop(key)
    return a_dictionary
