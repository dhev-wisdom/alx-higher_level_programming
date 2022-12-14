#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for i in range(x):
            print(my_list[i], end="")
        print()
        return i + 1
    except IndexError as e:
        print("An error was encountered. ", e)
