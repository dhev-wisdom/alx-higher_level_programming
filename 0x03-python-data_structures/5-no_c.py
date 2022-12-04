#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    str_copy = list(my_string)
    for letter in range(len(str_copy)):
        if str_copy[letter] == "C" or str_copy[letter] == "c":
            str_copy[letter] = ""
    new_string = "".join(str_copy)
    return new_string
