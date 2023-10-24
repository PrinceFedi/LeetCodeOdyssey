# Question 5 - Contains Duplicate (LeetCode 217)

"""
Given an array of integer number, return True if value appears at least twice in the array , and return False, if every
element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true
"""
List = [1, 10, 3, 10]

# Sort method

def contains_duplicate(nums: list[int]) -> bool:
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


print(contains_duplicate(List))

# Time Complexity: O(nlog(n)) - The built in sort function takes O(nlog(n)) time complexity which dominates runtime
# Space Complexity: O(n) - Trash ass function also takes O(n) space do to the auxiliary space needed to store elements

# Explanat///ion:
"""
In our first method, we rely heavily on the list library method, sort. This method sorts each element from least to 
greatest in order from first to last index). Using this method, our list is sorted. Now iterating through the list by 
index, we check if the element in the next index in our list is equal to the current index's element. If this is true, 
we have a duplicate.
"""


# Set method

def contains_duplicate_set(nums: list[int]) -> bool:
    nums_set = set(nums)
    if len(nums) == len(nums_set):
        return False
    return True


# Time Complexity: O(n) - We have to insert every element in our list to our hash table which then creates our set
# Space Complexity: O(n) - Set functions are implemented in python using hashing. So linear space complexity.

# Explanation:
"""
One of the main conditions Sets have is that have no duplicate members. So if we convert our given list into a set 
using the built in method set, we get a data structure that contains only distinct elements. We can use this as our test
expression to see if the length of our set is the same as our list, then we know its all distinct elements. If the list
contains a greater length then the set, then there are duplicate elements in our list because we are using the same 
elements and they would be erased making the sets length reduced due to their non-duplicate restraint. If they are the
same length, then both data structures are distinct.
"""


# Hash table

def contains_duplicate_hash(nums: list[int]) -> bool:
    hash_map = {}
    for i in nums:
        if i in hash_map:
            return True
        else:
            hash_map[i] = 1
    return False


# Time Complexity: O(n) - We search and insert elements in our hash table n times, when iterating through our list
# Space Complexity: O(n) - A hash table takes linear space in memory to store each element

# Explanation:

"""
For this implementation we instantiate a empty dictionary which uses hashing principles under the hood to create it.
We then will iterate through each element in the list (not index). If the element is not in the hashtable we will store
it as a key with a arbitrary value. For our first iteration, we will always do the second part of this condition and 
store it since our dictionary is empty. On our next iterations continuing, we know that if our current element is in our
non empty dictionary it is a duplicate value and thus means our original list contains duplicate members.
 
"""
