"""
Write a recursive function reverse_string(s) that takes a string s and returns the reversed string.
"""


def reverse_string(s):
    if len(s) <= 1:
        return (s)
    return reverse_string(s[1:]) + s[0]


print(reverse_string("hello"))
print(reverse_string("recursion"))
