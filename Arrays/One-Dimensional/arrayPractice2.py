# Question 3 - Finding a number in an Array

"""
Check if an array contains a number in python

Constraints: Cannot use list
"""

import numpy as np

my_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])


def search_for_number(array, number):
    for i in range(len(my_array)):
        if array[i] == number:
            return f"{number} is in the array "
    return f"{number} is not in the array"


print(search_for_number(my_array, 12))

# Time Complexity: O(n) - We iterate through the n size of array and check if each element corresponds to the number
# Space Complexity: O(1) - No extra space in memory is needed
