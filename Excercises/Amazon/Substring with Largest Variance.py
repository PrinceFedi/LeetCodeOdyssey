# Rank 1 - Substring with Largest Variance

"""The variance of a string is defined as the largest difference between the number of occurrences of any 2
characters present in the string. Note the two characters may or may not be the same.

Given a string s consisting of lowercase English letters only, return the largest variance possible among all
substrings of s.

Note:
A substring is a contiguous sequence of characters within a string.

Example:
    Input: s = "aababbb"
Output: 3
Explanation:
    All possible variances along with their respective substrings are listed below:
    - Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b", "bb", and "bbb".
    - Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb", and "bab".
    - Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
    - Variance 3 for substring "babbb".
    Since the largest possible variance is 3, we return it.
"""
from string import ascii_lowercase


def largestVariance(s):
    """
    :type s: str
    :rtype: int
    """

    def helper(a, b, string):
        max_var = 0
        variance = 0
        string_has_b = False
        first_b = False

        for i in string:
            if i == a:
                variance += 1
            elif i == b:
                string_has_b = True

                if first_b and variance >= 0:
                    first_b = False
                elif (variance - 1) < 0:
                    first_b = True
                    variance = -1
                else:
                    variance -= 1

            if string_has_b and max_var < variance:
                max_var = variance

        return max_var

    max_variance = 0
    for a in ascii_lowercase:  # see below
        for b in ascii_lowercase:  # rules dictate these 2 loops would be no more than O(26*26)
            if a == b:
                continue
            a_vs_b_variance = helper(a, b, s)
            max_variance = max(a_vs_b_variance, max_variance)
    return max_variance


string = "aababbb"
print(largestVariance(string))

