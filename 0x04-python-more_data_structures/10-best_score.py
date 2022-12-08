#!/usr/bin/python3
def best_score(a_dictionary):
    a = 0
    for y in a_dictionary.values():
        if a <= y:
            a = y
    for k, z in a_dictionary.items():
        if z == a:
            return k
