#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")

        except (ValueError, TypeError):
            pass

        else:
            printed = printed + 1
    print()
    return printed
