""" Convert a number from Decimal to Binary using Recursion """

# Recusive case -> f(n) = n mod 2 + 10 * f(n/2)
"""
Step 1: Divide the number by 2
Step 2: Get the integer quotient for the next iteration
Step 3: Get the remainder for the binary digit
Step 4: Repeat the steps until quotient is equal to 0

"""

# Base case -> number or (quotient) == 0 then we return 0
def DecimaltoBinary(number):
    assert int(number) == number, "we aren't doing floating point integers"
    if number == 0:
        return 0
    else:
        return number % 2 + 10 * DecimaltoBinary(number//2)

print(DecimaltoBinary(10))
