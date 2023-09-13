#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        numerals = {'I': 1,
                    'V': 5,
                    'X': 10,
                    'L': 50,
                    'C': 100,
                    'D': 500,
                    'M': 1000}
        new_list = [numerals.get(c) for c in roman_string]
        for i, (curr, nxt) in enumerate(zip(new_list, new_list[1:])):
            if curr < nxt:
                new_list[i] = -curr
        return new_list
    return 0
