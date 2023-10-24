# Rank 15 - Maximum Subarray (LeetCode 53)

"""Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.



# Constraints & Questions:
       1 <= nums.length <= 10^5
      -10^4 <= nums[i] <= 10^4
    - Does our array contain negative numbers?
    - Do we care if the original array/dataset is modified?

"""


# Dynamic programming approach (Kadane's Algorithm)

def maximum_subarray(nums):
    maximum_sum = current_sum = nums[0]
    for nums in nums[1:]:
        current_sum = max(nums, nums + current_sum)
        maximum_sum = max(maximum_sum, current_sum)
    return maximum_sum


nums_array = [5, -4, 1, -3, 6, -2, 7, -9, 6, -8]
print(maximum_subarray(nums_array))

# Time complexity -> O(n), we traverse the list once with n in this case being the length of our `nums array`.
# Space Complexity -> O(1), no extra calls are made to the stack, we are only using two constant variables current & max

"""This case involves the use of dynamic programming, an algorithmic paradigm based upon two properties, 
Optimal substructure and Overlapping problems. A way we can initially approach this would be by parsing the array into
it individual sub-arrays, and then comparing their sums. This brue force approach will be rather time consuming however
as we'd have to consistently traverse through the list while testing reoccurring cases (repeated sub-array sums).

A way to solve this would be dynamic programming using kadane's algorithm. In its nature, this is a greedy approach 
which uses the technique of tabulation (going from the bottom up) or in our case the start of the list. How we can 
start approach is by having two pointers, the maximum sum will we be returning and current sum we will need to keep 
track of. Using tabulation principles we will assume that the first index (being a sub-array of its own) will be the 
first initial sum we will compare against. Both our pointers will be assigned to this values. From there we will 
begin to iterate through our array starting specifically at the second value in the array. This is because we have
already dealt with the first element as its own subarray and it needs to be compared against. Now through each iteration
we will compare the current index's element to the sum of the current index's and the previous index's elements. Which
ever element is greater gets assigned to our current sum pointer. This allows us to eliminate overlapping subarray sums
since we are consistently keeping track of their value if they are the bigger then the current sum pointer. After the 
current sum pointer has been assigned, we compare it to the maximum sums pointer. If the current sum is greater, its 
value will be assigned to max sum pointer. At the end of our traversal we return the value stored in our max sum pointer
which should give us our answer."""
