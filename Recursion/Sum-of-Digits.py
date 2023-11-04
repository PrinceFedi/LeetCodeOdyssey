""" Question: How to find the sum of digits of a positive integer using recursion """

# Recursive case

""" Say we have a number 10. If we divided 10 by 10 we get 1 with a remainder of 0 """
# 10  -> 10/10 = 1 and remainder 0 """ We want to add 1 and 0 together to get the sum of digits """
# 54  -> 54/10 = 5 and remainder 4 
# 112 -> 112/10 = 11 and reaminder 2 """ Still gotta divide 11 """

# f(n) = n%10 + f(n/10)

# base case

""" in most cases the base case is 0 and 1 will be our terminating case"""
 # n == 0

# Constraint -> has to be a positive int 

def SumofDigits(n):
    assert n >= 0 and int(n) == n, " The parameter has to be a postivite int you goof"
    if n == 0:
        return 0
    else:
        return SumofDigits(n//10) + (n%10)

print(SumofDigits(165))
