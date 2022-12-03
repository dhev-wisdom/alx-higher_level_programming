#!/usr/bin/python3
import sys
print("{:d} {:s}".format(len(sys.argv) - 1, "argument" if len(sys.argv) == 2 else "arguments"))
if len(sys.argv) > 1:
    for arg in range(1, len(sys.argv)):
        print("{:d}: {:s}".format(arg, sys.argv[arg]))
