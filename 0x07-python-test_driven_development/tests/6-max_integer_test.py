#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([2, 3, 1, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-11, -2, -30, -4]), -2)
        self.assertEqual(max_integer([-2, -4, -6, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-10, 12, 23, -14]), 23)
        self.assertEqual(max_integer([-1, 2, -30, 4]), 4)
        self.assertEqual(max_integer([-10, 2, 37, -4]), 37)
        self.assertEqual(max_integer([1, -20, 2, 4]), 4)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([-5, -5, -5, -5]), -5)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_large_numbers(self):
        self.assertEqual(max_integer([1, 1000000000, 999999999]), 1000000000)
        self.assertEqual(max_integer([-999999999, -1000000000, -1]), -1)
        self.assertEqual(max_integer([999999999, 1000000000, 1]), 1000000000)

    def test_very_large_numbers(self):
        self.assertEqual(max_integer([87521, 9999999999999, 9]), 9999999999999)
        self.assertEqual(max_integer([-9999999999, -1800000000000, -1]), -1)
        self.assertEqual(max_integer([9999, 1000, 890000000000]), 890000000000)


if __name__ == "__main__":
    unittest.main()
