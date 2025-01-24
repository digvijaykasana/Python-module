#Test Script for calculator.py
from calculator import Calculator

calc = Calculator()

# Test operations
print("5 + 3 =", calc.add(5, 3))
print("5 - 3 =", calc.subtract(5, 3))
print("5 * 3 =", calc.multiply(5, 3))

# Handle division by zero gracefully
try:
    print("5 / 0 =", calc.divide(5, 0))
except Exception as e:
    print("Error:", e)

print("5 ^ 3 =", calc.power(5, 3))

# Test Script for string_utils.py

from string_utils import StringUtils

utils = StringUtils()

# Test operations
print("Reversed 'hello':", utils.reverse_string("hello"))
print("'hello' to uppercase:", utils.to_uppercase("hello"))
print("Is 'racecar' a palindrome?:", utils.is_palindrome("racecar"))
print("Vowel count in 'hello':", utils.count_vowels("hello"))
print("Contains special characters '#hello$':", utils.contains_special_characters("#hello$"))
