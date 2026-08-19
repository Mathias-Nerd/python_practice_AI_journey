"""
Write a recursive function in Python named is_palindrome(s) that takes a string s and returns True if s is a palindrome (reads the same forwards and backwards) and False otherwise.
"""
# Author: Mathias Nerd


def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])


print(is_palindrome("RACAR"))
