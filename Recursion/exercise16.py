"""
Write a recursive function fibonacci(n) that returns the $n$-th number in the Fibonacci sequence ($0, 1, 1, 2, 3, 5, 8, 13, 21 ots$).
"""


def fibonacci(n):
    if n < 0:
        return "Wrong input"
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(7))
