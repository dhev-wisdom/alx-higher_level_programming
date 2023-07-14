#!/usr/bin/python3
"""
Module inherits from class List
"""


class MyList(list):
    """
    Class inherites from list class
    """
    def print_sorted(self):
        """
        function prints sorted list
        """
        sorted_list = sorted(self)
        print(sorted_list)
