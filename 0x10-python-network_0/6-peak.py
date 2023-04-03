#!/usr/bin/python3
""" Module finds the peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """
    Function finds the highest int in fastest possible way
    """
    ln = len(list_of_integers)
    low, high = 0, ln - 1

    while low <= high:
        mid = (low + high) // 2

        if ((mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and
            (mid == ln - 1 or list_of_integers[mid + 1] > list_of_integers[mid])):
            return list_of_integers[mid]
        elif mid > 0 and list_of_intergers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        else:
            low = mid + 1
