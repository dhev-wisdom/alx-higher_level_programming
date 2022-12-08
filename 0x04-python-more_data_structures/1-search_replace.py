#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_l = []
    for item in my_list:
        if item == search:
            new_l.append(replace)
        else:
            new_l.append(item)
    return new_l
