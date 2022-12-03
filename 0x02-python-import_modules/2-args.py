#!/usr/bin/python3
import sys
if len(sys.argv) == 2:
    what_to_print = "argument."
elif len(sys.argv) == 1:
    what_to_print = "arguments."
else:
    what_to_print = "arguments:"
print("{:d} {:s}".format(len(sys.argv) - 1, what_to_print))
if len(sys.argv) > 1:
    for arg in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(arg, sys.argv[arg]))
