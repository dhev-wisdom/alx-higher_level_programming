#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    l = list(a_dictionary)
    l.sort()
    for item in l:
        print("{:s}: {}".format(item, a_dictionary[item]))
