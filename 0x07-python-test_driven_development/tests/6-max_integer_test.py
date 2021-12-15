#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        """will test max_integer"""

        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1, 2, 34, 4]), 34)
        self.assertEqual(max_integer([None]), None)
        self.assertEqual(max_integer([1, 3, 5, 2.5]), 5)
        self.assertEqual(max_integer([1, 3, 5, 22.5]), 22.5)
