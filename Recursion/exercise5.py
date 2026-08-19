"""
Write a recursive function in Python named reverse_string(s) that takes a string s and returns a new string with its characters in reverse order.

Constraint: You must use recursion. Do not use s[::-1], reversed(), or any loops.
"""
# Author: Mathias Nerd


def reverse_string(s):
    if len(s) <= 1:
        return s
    first_letter = s[0]
    remaining_letter = s[1:]
    return reverse_string(remaining_letter) + first_letter


print(reverse_string("Hello"))
print(reverse_string(""))
print(reverse_string("H"))
