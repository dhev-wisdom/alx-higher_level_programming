#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]
    if len(argv) == 4:
        if op == "+":
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
        elif op == "-":
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
        elif op == "*":
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))
        elif op =="/":
            print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
    else:
        print("Usage: ./100-my_calculator.py a op b")
        exit (1)
