#!/usr/bin/python3
"""Console Module"""


def factorial(n):
    """Calculate the factorial of a non-negative integer._summary_

    Args:
        n (int): Non-negative integer
    
    Return:
        Factorial of n
    """
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result