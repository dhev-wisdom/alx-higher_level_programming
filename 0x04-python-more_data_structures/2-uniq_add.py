#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_l = set(my_list)
    add = 0
    for num in new_l:
        add += num
    return add
