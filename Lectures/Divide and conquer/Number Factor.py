"""
Given n find the number of ways to express n as the sum of 1,3,4"

"""


def number_factor(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        return number_factor(n - 1) + number_factor(n - 4) + number_factor(n - 3)


print(number_factor(5))
