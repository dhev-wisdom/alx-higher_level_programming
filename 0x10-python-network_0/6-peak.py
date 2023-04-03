#!/usr/bin/python3
""" Module finds the peak in a list of unsorted integers """


def find_peak(list_of_integers):
    peak = 0
    if list_of_integers:
        for idx in range(len(list_of_integers)-1):
            if list_of_integers[idx] > peak:
                peak = list_of_integers[idx]
        return peak
    else:
        return None


if __name__ == '__main__':
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
