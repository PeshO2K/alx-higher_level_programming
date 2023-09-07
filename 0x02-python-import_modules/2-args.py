#!/usr/bin/python3
from sys import argv
argc = len(argv)
msg = "argument"

if __name__ == "__main__":
    if argc == 1:
        msg = msg + "s."
    elif argc == 2:
        msg = msg + ":"
    else:
        msg = msg + "s:"
    print("{:d} {:s}". format(argc - 1, msg))
    for i in range(1, argc):
        print("{:d}: {:s}". format(i, argv[i]))
