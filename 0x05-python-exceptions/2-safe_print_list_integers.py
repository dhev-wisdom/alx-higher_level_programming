#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            try:
                if i < 0 or i >= 0:
                    print("{:d}".format(my_list[i]), end="")
                    count = count + 1
            except (TypeError, ValueError):
                pass
        print()
        return count
    except Exception as err:
        print(err)
