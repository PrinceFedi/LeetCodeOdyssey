# Question 7 - Rotate Image (LeetCode #48)

"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:
matrix1 = [1 ,2 ,3,             [7, 4, 1,
           4, 5, 6,       ->     8, 5, 2,
           7, 8, 9 ]             9, 6, 3 ]


"""
array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# Transpose & Reverse Matrix

def rotate_90(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    transpose(matrix)
    reverse_row(matrix)


def rotate_180(matrix: list[list[int]]) -> None:
    reverse_row(matrix)
    reverse_column(matrix)


def rotate_270(matrix: list[list[int]]) -> None:
    transpose(matrix)
    reverse_column(matrix)


def transpose(matrix: list[list[int]]) -> None:
    """
   Iterations for 3x3 matrix       0 1 2     0 1 2   - index J
    i j        j i              0 [1,2,3   0 [1,4,7
    0,1        1,0              1  4,5,6   1  2,5,8
    0,2        2,0              2  7,8,9]  2  3,6,9]
    1,2        2,1              |
                            index I
    """
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp


def reverse_row(matrix: list[list[int]]) -> None:
    for i in range(len(matrix)):
        matrix[i].reverse()  # matrix[i] = matrix[i][::-1]


def reverse_column(matrix: list[list[int]]) -> None:
    for i in range(len(matrix[0])):
        start = 0
        stop = len(matrix) - 1
        while start < stop:
            temp = matrix[start][i]
            matrix[start][i] = matrix[stop][i]
            matrix[stop][i] = temp
            start += 1
            stop -= 1


# Time complexity: O(M) - Transposing the matrix cost linear time since we are moving the value of each cell once while
#                         reversing each row also has a cost of linear O(m), because again we are moving the value once

# Space complexity: O(1) - We do not require any other additional data structures

# Explanation:
"""
Using linear algebra principles, we can apply two steps to rotate our matrix... Transposing & Reversing. 

Transposing - in linear algebra, the transpose of a matrix is an operator which flips a matrix over its diagonal;
that is, it switches the row and column indices of the matrix. 
Example: 
A = [1, 2          [1,3,5 
     3, 4   ->      2,4,6]
     5, 6 ]

To preform this in code, we will iterate through the matrix creating control flows (loops) that iterate through the rows
and columns. Our logic needs our columns iteration to start at the second column. From there, we will use the swap
algorithm to transpose the corresponding index. Once this is complete we can reverse the index value of each row to 
complete our rotation at 90 degrees. To reverse elements, either iterate through the row like this [::-1] and reassign
it to the corresponding row, or just use the reverse function for list.

90 degrees Rotation - transpose matrix then reverse row values
180 degrees Rotation - reverse row values then reverse column values
270 degrees Rotation - transpose matrix, then reverse column values
"""


# Rotation by cells

def rotate_math(matrix: list[list[int]]) -> None:
    left, right = 0, len(matrix) - 1
    while left < right:
        for i in range(right - left):  # right - left is the number of rotations we do,(n - 1 = r as n is length of row)
            top, bottom = left, right
            # Save top left element for later
            top_left = matrix[top][left + i]  # left + i will shift us one position to the right
            # move bottom left element into top left corner
            matrix[top][left + i] = matrix[bottom - i][left]  # bottom - i will shift us one position up
            # move bottom right element into bottom right corner
            matrix[bottom - i][left] = matrix[bottom][right - i]  # right - i will shift us one position to the left
            # move top right element into bottom right corner
            matrix[bottom][right - i] = matrix[top + i][right]  # top + i will shift us one position down
            # move top left element into top right
            matrix[top + i][right] = top_left

            # decrement our right and left pointers to handle each layer in our matrix

        right -= 1
        left += 1


# Time Complexity - O(M) - each cell gets read once and written once
# Space Complexity - O(1) - no additional data structures are used

# Explanation:
"""
For this implementation we want to iterate through a group of cells and rotate them. We can treat the matrix as multiple
layered boundaries in which we will preform our rotation from outer to inner. To preform our 90 degree rotation a simple
way would be to start out our boundaries origin point which is indices [0][0] for our matrix. We will then assign the
previous rotation cells index value to our current one in reverse order. It will go as such... 

Algorithm:
temp_variable = top left
top left = bottom left
bottom left = bottom right
bottom right = top right
top right = bottom right

We will need two pointers to preform this which represent the indices we want. Our left pointer will be initialized at 0
for our starting point while our stopping point (the right most cell (index value on farthest point of our layer)) will
be our right pointer, which is an initialization at last index in our row. We will then create a loop that terminates 
when the left pointer is not less the right pointer. In this loop, we will iterate in range of the number of rotations, 
which is the length of values in the row (n) - 1 so (n-1). We do this since, we dont have to account for the final index 
in each rotation since that last index gets replaced. We can set this up as right - left pointer which equates to us 
iterating through the first index to the last index of our row -1. Now once we do that we preform our algorithm stated 
above. We will first save the top left index into a temporary variable where we can store it for use later. Then going
counter clockwise, we store the previous cells into each other. The i variable in our rotation loop will be used to 
shift our indices to the exact places as shown in the comments above. After the loop finishes we decrement the right 
pointer and increment the left pointer as a way of shifting to the next layer inwards in our matrix.
"""
