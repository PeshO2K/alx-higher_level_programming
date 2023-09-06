#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    number = -number
lastdigit = number % 10
if lastdigit > 5:
    msg = "greater than 5"
elif lastdigit == 0:
    msg = "0"
else:
    msg = "less than 6 and not 0"
print(f'Last digit of {number:d} is {lastdigit:d} and is {msg}')
