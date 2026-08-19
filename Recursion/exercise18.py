"""
The Goal: Write a recursive function power(base, exponent) that calculates $base^{exponent}$ (e.g., $2^4 = 16$).
"""


def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)


print(power(5, 3))
