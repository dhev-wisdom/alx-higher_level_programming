#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


"""Add script argument to json"""


try:
    lst = load_from_json_file("add_item.json")
except FileNotFoundError:
    lst = []

length = len(sys.argv)
if length > 1:
    for i in range(1, length):
        lst.append(sys.argv[i])
save_to_json_file(lst, "add_item.json")
