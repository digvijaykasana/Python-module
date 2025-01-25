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