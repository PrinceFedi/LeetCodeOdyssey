# Question 1 - Missing Number (LeetCode 268)


"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
missing from the array.

Example:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the
range since it does not appear in nums.
"""

# Method for unsorted:

# array = [i for i in range(1, 101)]
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
         59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
         87, 88, 89, 90, 91, 92, 93, 94, 95, 97, 98, 99, 100]


def missing_number(my_list, number):
    sum1 = number * (number + 1) / 2  # Sum of numbers series n(n+1)/2 - Gauss's formula
    sum2 = sum(my_list)
    return sum1 - sum2


print(missing_number(array, 100))

# Time complexity : O(n) - although Gauss's formular can be used in constant time. Using the sum func is linear time tho

# Space complexity: O(1) - we don't need any extra space to preform this operation


# Explanation:

"""
By using the sum of a series of numbers, we can compare the expected sum of an array with integers 1-100,
to the actual sum we have in our array. By subtracting the expected sum by the actual sum, we get our 
difference which ends up being the missing number (between 1-100) in our array.

Cons: If you do the first method you must traverse all numbers in list in the sum function (99 steps) and do 
100*101/2 (1 step) That is 100 steps. 

If the missing number is 1 then you did extra 99 steps.

"""


# sorted list
def missing_number2(nums):
    nums.sort()
    for i in range(0, len(nums)):
        if nums[i] != i + 1:
            return i + 1


# Time complexity: O(nlog(n)) - The sort method is a slower run time then the for loop which dominates performance
# Space complexity - O(n) - sort function is n space complexity - fucking garbage

# Explanation:
"""
Starting with the index at 0 declared with the variable i, we iterate through the entire array with an infinite
while loop. Here we compare the while loops index with its given number. So at index 0, our number should be 1 (i+1)
in an array of elements from 1 -> 100 (SORTED). We will then return the missing element when it fails to equal the 
corresponding value at the given index. Otherwise we will continue to increment i.

"""
print(missing_number2(array))
