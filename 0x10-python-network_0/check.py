#!/usr/bin/python3
def find_peak(arr):
    """
    This function finds a peak in an unsorted list of integers
    using Binary Search algorithm.
    """
    n = len(arr)
    low, high = 0, n - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if ((mid == 0 or arr[mid - 1] <= arr[mid]) and
            (mid == n - 1 or arr[mid + 1] <= arr[mid])):
            return arr[mid]
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
