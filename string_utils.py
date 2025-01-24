import re

class StringUtils:
    def reverse_string(self, s):
        return s[::-1]

    def to_uppercase(self, s):
        return s.upper()

    def is_palindrome(self, s):
        cleaned_string = re.sub(r'\W+', '', s).lower()
        return cleaned_string == cleaned_string[::-1]

    def count_vowels(self, s):
        return len(re.findall(r'[aeiou]', s, re.IGNORECASE))

    def contains_special_characters(self, s):
        return bool(re.search(r'[^a-zA-Z0-9\s]', s))
