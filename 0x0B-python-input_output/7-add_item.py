#!/usr/bin/python3
"""Program that adds all arguments to a list and save to file"""



save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file
import sys


try:
    lst = load("add_item.json")
except:
    lst = []

length = len(sys.argv)
if length > 1:
    for i in range(1, length):
        lst.append(sys.argv[i])
save(lst, "add_item.json")
