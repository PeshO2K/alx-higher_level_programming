#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div
argc = len(argv)
res = 0

def print_err(msg):
    print(msg)
    exit(1)
if __name__ == "__main__":
    if argc == 4:
        a = int(argv[1])
        b = int(argv[3])
        op = argv[2]
        match op:
            case "+":
                res = add(a, b)
            case "-":
                res = sub(a, b)
            case "*":
                res = mul(a, b)
            case "/":
                res = div(a, b)
            case _:
                print_err("Unknown operator. Available operators: +, -, * and /")
        print(f"{a:d} {op:s} {b:d} = {res:d}")
    else:
        print_err("Usage: ./100-my_calculator.py <a> <operator> <b>")
