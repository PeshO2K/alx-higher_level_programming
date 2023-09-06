#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        i = 90 - (122 - i)
    print("{:s}".format(chr(i)), end="")
