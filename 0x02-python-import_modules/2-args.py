#!/usr/bin/python3
from sys import argv
print("{:d} {:s}".format(len(argv) - 1, "argument" if len(argv) == 2 else "arguments"))
if len(argv) > 1:
    for arg in range(1:len(argv)):
        print("{:d}: {:s}".format(arg, str(argv[arg]))
