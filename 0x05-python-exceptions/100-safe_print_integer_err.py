#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    try:
        if value > 0 or value <= 0:
            print("{:d}".format(value))
        else:
            raise ValueError
        return True
    except (ValueError, TypeError) as err:
        print("Exception: ", err, file=sys.stderr)
        return False
