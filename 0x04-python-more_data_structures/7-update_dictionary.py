#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if key in a_dictionary.keys():
        pass
    else:
        a_dictionary[key] = value
    for item in a_dictionary:
        if key == item:
            a_dictionary[key] = value
        else:
            pass
    return a_dictionary
