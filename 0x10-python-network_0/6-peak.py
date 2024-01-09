#!/usr/bin/python3
'''Module to find peak'''


def find_peak(mylist=[]):
    '''Function to find peak'''
    if len(mylist):
        low = 0
        high = len(mylist) - 1

        while low < high:
            mid = (low + high) // 2
            if mylist[mid] < mylist[mid + 1]:
                low = mid + 1
            else:
                high = mid

        return mylist[low]
    return None
