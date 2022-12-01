#!/usr/bin/python3
for i in range(100):
    if i < 10:
        print("{}".format(0), end="")
    if i < 99:
        print("{}".format(i), end=", ")
    if i == 99:
        print(i)
