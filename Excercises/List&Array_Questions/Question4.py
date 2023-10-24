# Question 4 - Maximum product of Two elements (LeetCode 1464)

"""
Given an array of integers num you will choose two different indices i and j of that array.
Return the maximum value of ((nums[i]-1) * (nums[j]-1))

Example 1:

Input: nums = [3,4,5,2]
Output: 12
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get
the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
"""
array = [3, 4, 5, 2]


# Brute Force

def max_product(nums: list[int]) -> int:
    max_prod = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            prod = ((nums[i] - 1) * (nums[j] - 1))
            if prod > max_prod:
                max_prod = prod
    return max_prod


print(max_product(array))

# Time Complexity: O(n^2) - we traverse through the array twice comparing each combination of indices to get the max
# Space Complexity: O(1) - no extra calls are made to the stack

# Explanation:
"""
To find the maximum product of two indices we have to traverse through the array twice. Traverse twice will allow us to
pair each iteration of i with its corresponding j index (i+1). This allows us to use have every combination of each 
index pair. However, we need something to keep track of each product our pairs generate so we can later compare and see
which is the max one. To do this, we can create a place holder variable before the first loop instantiated at 0. Now,
as we get the product of each pair, we will check to see if its value is greater then our previous product max value. If
it is we will reassign that current product's value to the placeholder variable. When we are finished traversing the
list, are max product will be the last value stored in that placeholder variable. 
"""


# Built-in method solution

def max_product_b(nums: list[int]) -> int:
    i = max(nums)
    nums.pop(nums.index(i))
    j = max(nums)
    return (i - 1) * (j - 1)


#print(max_product_b(array))

# Time Complexity: O(n) - Using the max function, we only traverse through a list once, which is linear time
# Space Complexity: O(1) - No extra space in memory is created


# Explanation:
"""
Now this method requires a bit of knowledge of the language of python. Since we know we want the index of our array with
the max value... we can just use the max method. This will return the desired value we want. Now we know from our 
previous implementation and the question at hand, that we are using the product of two indices. Therefore, we have to
remove the max value we originally got from out list to find the second biggest value. Here we can use the pop method 
from the list library to remove that value by combining it with the index method to find the exact index that value
corresponds too. Now once our list is modified to contain every element but the previous max, we can reuse the max 
method to find the new max. Once this is done, we return the product of both of those max values. This is a way better
solution because it is linear time complexity since we do not have to check for every possible index combination.
"""