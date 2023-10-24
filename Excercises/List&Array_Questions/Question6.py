# Question 6 - Remove Duplicate (LeetCode 26)
"""

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique
element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be
placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates,
then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k
elements.

Return k after placing the final result in the first k slots of nums.

Example:
Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 2, nums = [0,1,3,4,4, _, _, _, _, _]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

"""

array1 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
array2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

# Slice approach

def remove_duplicates(nums: list) -> int:
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            nums[i] = "_"
    print(nums)
    nums[:] = (i for i in nums if i != "_")
    print(nums)
    return len(nums)




# Time Complexity: O(n) - We traverse through the array once comparing the respective indexes in linear time
# Space Complexity: O(1) - We are not using any extra space

# Explanation:
"""
In this solution we iterate through the indices of the given list. We create a condition which checks if the current
index's value is equal to the next index's value then we will assign the current index to a null or arbitrary character.
This will remove the repetitions and keep the last repeated value in our list. After the list has been traversed, we 
will use the slice operator to return all the elements in the list. However, as we do this we will assign to it all the
elements that do not have are designated arbitrary value, which is our repeated values. Once this is done we can return 
the length of our modified list. 
"""


# Two pointers approach

def remove_duplicate_2p(nums: list[int]) -> int:
    left_pointer = 1
    for right_pointer in range(1, len(nums)):

        if nums[right_pointer] != nums[right_pointer - 1]:
            nums[left_pointer] = nums[right_pointer]
            left_pointer += 1

        print(f"left pointer is {left_pointer} when right pointer is on iteration {right_pointer}")
        print(nums)
    return left_pointer


# Time complexity: O(n) - since we only have 2 pointers, and both the pointers will traverse the array at most once
# Space complexity: O(1) - we are not using any extra space so our solution is constant time

# Explanation:
"""
With the two pointer approach, we will initialize both to begin at the second index in our array. These will be our 
right and left pointers. 

Note: We have to sort them in ascending order so thats why we start at 1, we can already assume the the first element in our array is distinct

right pointer - looks at the previous index value in our list and compares it the current index, its always treversing through our array
left pointer - stays at temporary index that value will be assigned to the index value of the newest unique element in 
               the list. Unique element - a new element that has not been seen yet in the array

Once this is done, we will traverse through the list comparing the previous index value to the current index value. 
A condition will handle this checking if they are equal or not. If they are not equal, we will replace the left pointers
index with the value at the right pointers index since are output is arranged in ascending order. If this condition is 
satisfied we will manually increment the left pointer to the next index (the right gets incremented by our loop). We 
will then return the total value of the left pointer based on how many incrementation it made+1. That will be how many 
total unique elements there are in original list.


"""

print(remove_duplicate_2p(array1))
#print(remove_duplicate_2p(array2))


