#Unit Test Script for calculator.py
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(5, 3), 8)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        with self.assertRaises(Exception):
            self.calc.divide(10, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)

if __name__ == '__main__':
    unittest.main()

# Unit Test Script for string_utils.py

import unittest
from string_utils import StringUtils

class TestStringUtils(unittest.TestCase):
    def setUp(self):
        self.utils = StringUtils()

    def test_reverse_string(self):
        self.assertEqual(self.utils.reverse_string("hello"), "olleh")

    def test_to_uppercase(self):
        self.assertEqual(self.utils.to_uppercase("hello"), "HELLO")

    def test_is_palindrome(self):
        self.assertTrue(self.utils.is_palindrome("racecar"))
        self.assertFalse(self.utils.is_palindrome("hello"))

    def test_count_vowels(self):
        self.assertEqual(self.utils.count_vowels("hello"), 2)

    def test_contains_special_characters(self):
        self.assertTrue(self.utils.contains_special_characters("#hello$"))
        self.assertFalse(self.utils.contains_special_characters("hello"))

if __name__ == '__main__':
    unittest.main()
