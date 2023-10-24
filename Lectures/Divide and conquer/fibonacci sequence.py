"""
Definitions:
    The fibonacci sequence is a series of numbers in which each number is a sum of the previous two numbers. First two
    numbers are denoted at f(0) = 0 and f(1) = 1.

Approach:
    We can solve this using the divide and conquer algorithm and then implementing it using recursion.

Recursion:
    Base Case(s): f(0) = 0
                  f(1) = 1
    Recursive step:
                  f(n) =  f(n-1) + f(n-2)
    Constraint(s):
                  n in f(n) has to be > 1, this is also zero base indexed
"""


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    elif n >= 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
