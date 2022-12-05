#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    l1, l2 = 0, 0
    for num in range(len(tuple_a)):
        l1 += 1
    for num2 in range(len(tuple_b)):
        l2 += 1
    a_is_longer = True
    if l1 > l2:
        a_is_longer = True
    else:
        a_is_longer = False
    if a_is_longer:
        for a,b in zip(tuple_a, tuple_b):
            

