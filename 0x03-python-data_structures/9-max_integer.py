#!/usr/bin/python3
def max_integer(my_list=[]):
    largest = 0
    for num in my_list:
        if largest <= num:
            largest = num
    return largest
