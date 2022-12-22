#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        j = 0
        while my_list[j]:
            if j <= x:
                print(my_list[j], end="")
            j+=1
        return (j)
    except:
        print("An error was encountered")
