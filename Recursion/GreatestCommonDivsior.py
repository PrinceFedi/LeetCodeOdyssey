""" Question: Find the Greatest Common Divisor of two numbers using recursion? """

# Note: the greatest common divsior is largest positive integer that divides the numbers without a reaminder
"""
 Euclidean algorithm: https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm#:~:text=The%20Euclidean%20Algorithm%20for%20finding,%3D%20GCD(B%2CR)

 gcd(48,18):
 Step1: 48/18 = 2 reaminder 12
 Step2: 18/12 = 1 reaminder 6
 Step3: 12/6 =  2 raminder 0

gcd(a,0) = a
gcd(a,b) = gcd(b, a mod b)
"""


def gcd(number1: int, number2: int):
    assert int(number1) == number1 and int(number2) == number2, "Should be integers for both" 
    if number1 < 0:
        number1 *= -1
    if number2 < 0:
        number2 *= -1
    if number2 == 0:
        return number1
    else:
        return gcd(number2, (number1 % number2))

print(gcd(-8,12))
