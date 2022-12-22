#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(int(value)))
        return True
    except TypeError as e:
        print("Encountered a type error: ", e)
        return False
