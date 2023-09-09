#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list):
        e_max = my_list[0]
        for i in my_list:
            e_max = i if i > e_max else e_max
        return e_max
    return None
