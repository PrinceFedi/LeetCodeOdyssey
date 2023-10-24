# Question 2 - Pairs/Two Sums (LeetCode 1)

"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to
target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

List&Array_Questions before starting:
- Does the array contain only positive or negative numbers?
- What if the same pair repeats twice, should I always print?
- If the reverse of the pair is acceptable e.g. can (4,1) work like (1,4) when the sum/target is 5?
- Do we need to print only distinct pairs? Does (3,3) work for target 6 even if it's a duplicate?
- How big is the array
"""

# Brute force solution

nums = [0, 2, 6, 9]


def two_sums(array, target):
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                return i, j


# Time complexity -> O(n^2), we traverse the list twice. For every index we have to check each possible index pair
# Space Complexity -> O(1), no additional pointers or calls to the stack are made

# Explanation
"""
For our solution, we take our given array and traverse through its indices. However, we want to give each index a
chance to be paired with each possible combination. That means that we need a second iteration which begins at the next
index. Starting our second iteration also satisfies our condition of having only distinct indices. This means that (0,0)
when the target is 6 and the value at index 0 == 3 will not work. Once in the second loop just add the indexes elements
together and check if they equal the target. If so, return both of the indexes.

"""


# Hash map solution

def two_sum_hash(nums_hash, target):
    hash_map = {nums_hash[i]: i for i in range(len(nums_hash))}
    for i in range(len(nums_hash)):
        if target - nums_hash[i] in hash_map and hash_map[target - nums_hash[i]] != i:
            return i, hash_map[target - nums_hash[i]]


print(two_sum_hash(nums, 9))

# Time complexity: O(n). We traverse the list containing n elements exactly twice. Since the hash table reduces the
# lookup time to O(1), the overall time complexity is O(n).

# Space complexity: O(n). The extra space required depends on the number of items stored in the hash table,
# which stores exactly n elements.

# Explanation:

"""
To find the sum of a pair of index, we can implement it using a hash function. Our function will take an array/list as 
well as a target sum that we want the sum of our pair to equal. We first start our implementation by creating a hash map
which creates a key value pair with the key being the elements in the original array, and the value being the index of
the elements in the original inputted array. Example: nums = [0, 2, 7, 15]
                                             Hash map = {0 : 0, 2: 1, 7: 2, 15: 3}
We did this because once we find which pair of elements equal are target number, we need to able to map it back to its
corresponding index. Unlike are previous implementation, by using a hash map we have a near O(1) or constant look up 
time to get each index.

Now once our hash map is created we then can use a for loop that iterates through in each index of our original array.
In each iteration, we will check the possible combination of the current index with its complement index. A condition to
do test this goes as follows:
    Case 1: Find the complement of our current index's element (target - curr) and see if it exists at a different index
    Case 2: Check if the complement exist in our array by looking at our hash map which mapped each element to its index
    
    This works well because a map allows us to quickly search for the elements we looked at previously and allows us to
    easily look up the index of the complement, since in our hash map, we map the elements as keys and their index's as 
    values. That allows us to remember what we saw in the array and quicly look it up later rather then reiteration each
    time.
    
    If both conditions are good we can return the index that we are on and the index of its complement since as stated 
    above, the element + complement == target meaning that we would have our answer at the corresponding indexes.
    
    Tips:
    Its good to note that when you have a problem with O(n^2) time and O(1) space, it can often be converted to O(n)
    time and O(n) space since time complexity is more desired because memory can be increased but you can't recover
    wasted time.
    
    A map is suggested when we want to remember if we saw something and where we seen that something. We can then map
    this as a key:value pair using python dictionaries.

"""