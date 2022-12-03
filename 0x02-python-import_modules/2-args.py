#!/usr/bin/python3
if __name__ = "__main__":
    import sys
    for l in range(len(sys.argv)):
        print("{:d}: {:s}".format(l, sys.argv[l + 1]))
        print()
