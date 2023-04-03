#!/usr/bin/python3
""" Module finds the peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """
    Function finds the highest int in fastest possible way
    """
    peak = 0
    if list_of_integers:
        for idx in range(len(list_of_integers)-1):
            if list_of_integers[idx] > peak:
                peak = list_of_integers[idx]
    else:
        peak = None

    return peak
