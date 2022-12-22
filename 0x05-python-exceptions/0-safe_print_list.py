#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for element in my_list:
            print("{}".format(element), end="")
            i += 1
        return (i)
    except:
        print("An error was encountered")
