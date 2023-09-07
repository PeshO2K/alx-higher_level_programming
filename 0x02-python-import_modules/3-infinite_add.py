#!/usr/bin/python3
from sys import argv
argc = len(argv)
sum = 0
if __name__ == "__main__":
    for i in range (1, argc):
        sum += int(argv[i])
    print(sum)