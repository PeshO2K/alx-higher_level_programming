#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Testing Class """
    def test_max(self):
        """#Test with empty and non empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())
        self.assertIsNone(max_integer([None]))

    def test_positive(self):
        """#Test with positive numbers"""
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3]), 4)

    def test_negative(self):
        """#Test with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -4, -3]), -1)
        self.assertEqual(max_integer([-2, -1, -4, -3]), -1)

    def test_floats(self):
        """#Test with floats"""
        self.assertEqual(max_integer([1.0, 2.0, 3.0, 4.0]), 4.0)

    def test_mixed(self):
        """#Test with mixed """
        self.assertEqual(max_integer([-1, 2.0, -4, 3]), 3.0)
        self.assertEqual(max_integer([1.0, -2, -4, -3]), 1.0)

    def test_tuples_strings(self):
        """#test with strings and tuples"""
        self.assertEqual(max_integer("abcDe"), 'e')
        self.assertEqual(max_integer((4, -1, 7.0, 3)), 7.0)

    def test_types(self):
        """#Raise necesary errors"""
        with self.assertRaises(Exception):
            max_integer(None)
        with self.assertRaises(Exception):
            max_integer(1.0)
        with self.assertRaises(Exception):
            max_integer({1: 2, 2: 3, 3: 1})
        with self.assertRaises(Exception):
            max_integer({1, 2})
        with self.assertRaises(Exception):
            max_integer([1, 2, "3", {1, 2}])
