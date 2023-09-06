#!/usr/bin/python3
def uppercase(str):
    for a in str:
        if ord(a) in range(97, 123):
            a = chr(65 + ord(a) - 97)
        print("{:s}".format(a), end="")
    print("")
