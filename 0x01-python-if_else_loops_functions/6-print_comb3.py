#!/usr/bin/python3
num_list = []
for i in range(10):
    for j in range(1, 10):
        first = str(i) + str(j)
        rev = str(j) + str(i)
        if (num_list.count(first) != 1) and (num_list.count(rev) != 1):
            num_list.append(first)
for a in num_list:
    if a != num_list[-1]:
        print("{}".format(a), end=", ")
    if a == num_list[-1]:
        print(a)
