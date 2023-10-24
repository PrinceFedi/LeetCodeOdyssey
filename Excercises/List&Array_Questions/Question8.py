# Question 8 - Matrix Diagonal sum (LeetCode 1572)

"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the
secondary diagonal that are not part of the primary diagonal.

Example:
1 2 3
4 5 6           1 + 5 + 9 + 3 + 7 = 25
7 8 9
"""

# Modulo operator approach

array = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
array2 = [[1, 1, 1, 1]]
array2 *= 4


def diagonal_sum(mat: list[list[int]]) -> int:
    result = 0
    n = len(mat)
    middle_indices = n // 2
    for i in range(n):
        result += mat[i][i]
        result += mat[i][-1-i]

    if n % 2 == 1:
        result -= mat[middle_indices][middle_indices]

    return result


print(diagonal_sum(array))

# Time complexity: O(M) - Our dataset is a matrix, and we don't traverse it twice, if it was an array it would be O(n^2)
# Space complexity: O(1) - No additional space is added to our heap since matrix are contiguous in memory

# Explanation:
"""For this solution we start by creating an accumulation variable. This will be the sum of both diagonals in the 
matrix. Next, we get the length of the rows in our matrix. This is important because our matrix is a square meaning 
the same number of rows by columns (3*3 matrix, 4*4 matrix 5*5 matrix... etc). Therefore the amount of elements and 
more importantly, amount of indices are the same for both rows and columns. Once we have that we create a variable that
will always get our middle index or indices in our array.

Note: We cannot include intersecting elements in the diagonal or our matrix. Odd length matrices such as (3*3, 
5*5) always have a intersecting index right in middle. We can satisfy our constraint in odd cases by subtracting the 
index value at the middle from our accumulator variable. To do this we will write and condition checking if it is an 
odd length matrix. The condition will be an expression which uses the modulo operator to check if our length has a 
remainder of 1 when our length is divided by 2. If our remainder is 1, it is an odd length matrix and we will then 
preform our subtraction from the accumulator. 

We start by iterating through the indices of our matrix. To get the index values of the left to right diagonal, we use
the same index number for both row and column indices ([0][0], [1,1] [2,2].. etc). Now for the right to left diagonal 
for the index in the column place, we want to access the values in the reverse index order going from last element to
first. To do this we can use negative indexing to do this. By using index arithmetic (-1-i) this operation can be done.
Through each iteration of both diagonals we simultaneously add them to our accumulator variable.

Once both the loop and condition is done and checked, we will return our accumulator variable which should now equal the 
sum of diagonals.
"""
