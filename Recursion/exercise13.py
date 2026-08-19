"""
The Goal: Write a recursive function is_palindrome(s) that returns True if a string reads the same forwards and backwards, and False otherwise.
"""


def is_palindrome(s):
    s = s.strip().lower()
    if len(s) <= 1:
        return True
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False


print(is_palindrome("hello"))
