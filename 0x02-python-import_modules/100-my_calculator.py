#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
argc = len(argv)
res = 0
msg_1 = "Unknown operator. Available operators: +, -, * and /"


def print_err(msg):

    print(msg)
    exit(1)


if __name__ == "__main__":

    if argc == 4:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]
        if op == "+":
            res = add(a, b)
        elif op == "-":
            res = sub(a, b)
        elif op == "*":
            res = mul(a, b)
        elif op == "/":
            res = div(a, b)
        else:
            print_err(msg_1)
        print(f"{a:d} {op:s} {b:d} = {res:d}")
    else:
        print_err("Usage: ./100-my_calculator.py <a> <operator> <b>")
