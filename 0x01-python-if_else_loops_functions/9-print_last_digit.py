#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print("{}".format(number % 10))
    else:
        number = number * -1
        mod = number % 10
        mod = mod * -1
        print("{}".format(mod))
