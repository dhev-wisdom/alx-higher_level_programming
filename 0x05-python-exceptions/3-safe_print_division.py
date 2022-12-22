#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        return result
    except Exception as err:
        print(err)
        return None
    finally:
        print("Inside result: {:d}".format(result)
