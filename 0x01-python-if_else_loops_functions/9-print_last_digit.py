#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        print("{}".format(number % 10), end="")
    elif int(number) != number:
        print("{}".format((ord(number)) % 10), end="")
    else:
        number = number * -1
        mod = number % 10
        mod = mod * -1
        print("{}".format(mod), end="")
