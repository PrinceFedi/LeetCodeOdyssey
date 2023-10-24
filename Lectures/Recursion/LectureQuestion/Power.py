""" Question: How to calcutate the power of a number using recursion? """

# Note: x^n = x*x*x*..(n times)*..x
#       x^a * x^b = x^a+b -> when we multiply two variables that have the same base we can add the exponents 
"""Based off this equation, we should have two parameters...base which represents x in our equation and exponent as n"""

# Recursive Case -> x^n = x*x^(n-1) 
"""
Because we can add together exponents with the same base variable, we can solve our recurisve equation by saying x^1 * x^n-1. The 
n-1 allows us to get smaller sastifying our recursive conditon and since 1+(-1) = 0 all thats left in our exponent is n which means
x^n is our answer. This is demonstrated above.
"""

# Base case -> b^0 = 1
""" Anything to the power of zero is 1"""

# Constraint -> Only positive integer exponents
def Power(base, exponent:int):
    assert exponent >= 0 and int(exponent) == exponent, "We are not doing floating point or negative exponents you goof"
    return 1 if exponent == 0 else base * Power(base, exponent-1)

print(Power(2,3))


# implementation with negative exponents

def NegativePower(base,exponent:int):
    assert exponent == int(exponent), "exponent has to be an integer goofy" 
    if exponent == 0:
        return 1
    elif exponent < 0: 
        return 1/base * NegativePower(base, exponent+1) 
    else:
        return base * NegativePower(base, exponent-1)

print(NegativePower(2, -3))
