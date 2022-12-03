#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = 0
    if len(argv) > 1:
        for arg in range(1, len(argv)):
            a += int(argv[arg])
    print("{:d}".format(a))
