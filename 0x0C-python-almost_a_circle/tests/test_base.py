#!/usr/bin/python3
"""
Module to test the base module
"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    Class that contains code to test the Base class contained in models/base.py
    """

    def setUp(self):
        """ Setup all code to be reused in this class """
        self.new_object = Base()

    def test_existence(self):
        """ Test that Base class exists and an
        instance can be created off of it  """
        self.assertIsInstance(self.new_object, Base)

    def test_attribute(self):
        """
        Test if instance of Base class has private instance
        attribute `id` and it's either None or an int """
        self.assertEqual(hasattr(self.new_object, "id"), True)
        opt1 = self.new_object.id is None
        opt2 = isinstance(self.new_object.id, int)
        self.assertEqual(opt1 or opt2, True)


if __name__ == "__main__":
    unittest.main()
