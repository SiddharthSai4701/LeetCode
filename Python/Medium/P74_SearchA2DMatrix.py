"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
"""


"""
My approach

Use two pointers i and j

For each one, have a left and a right. Let's call them L_i, R_i, L_j and R_j

Start with:
    L_i = 0
    R_i = m - 1

    L_j = 0
    R_j = n - 1

Do a binary search on the rows of the matrix.

We're told that the matrix is in ascending order where the first element of each row is greater than
the last element of the previous row.

So, first do a binary search to identify which row the target lies in. This can be done as follows:

    1.) M_i = L_i + (R_i - L_i) -> This will give the row
    2.) Check if the target is lesser than the first element of M_i. If yes, set R_i to be M_i - 1
    3.) Else, check if the target is greater than the last element of M_i. If yes, set R_i to be M_i + 1
    4.) If the target is equal to either of these values, return the index
    5.) If the value is greater than the first value in M_i but smaller than the last value of M_i,
        use the indexes L_j and R_j to do a binary search on that row until the target is found

"""

# First attempt - worked on local for a couple of tests but passed just 1 test on LeetCode because the time limit exceeded
# from typing import List
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         m = len(matrix)
#         n = len(matrix[0])

#         L_i = L_j = 0
#         R_i = m - 1
#         R_j = n - 1

#         while L_i <= R_i:
#             # This will point me to a row
#             M_i = L_i + (R_i - L_i) // 2

#             if target == matrix[M_i][0] or target == matrix[M_i][n - 1]:
#                 return True

#             elif target < matrix[M_i][0]:
#                 R_i = M_i - 1

#             elif target > matrix[M_i][n - 1]:
#                 L_i = M_i + 1

#             else:
#                 while L_j <= R_j:
#                     M_j = L_j + (R_j - L_j) // 2

#                     if target == matrix[M_i][M_j]:
#                         return True

#                     elif target < matrix[M_i][M_j]:
#                         R_j = M_j - 1

#                     elif target > matrix[M_i][M_j]:
#                         L_i = M_j + 1

#         return False


# s = Solution()
# print(s.searchMatrix(
#     [
#         [1,3,5,7],
#         [10,11,16,20],
#         [23,30,34,60]
#     ],
# 13))

###########################################################################################################################

# Second solution - worked like a charm
from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        L_i  = 0
        R_i = m - 1

        while L_i <= R_i:
            # This will point me to a row
            M_i = L_i + (R_i - L_i) // 2

            if target in matrix[M_i]:
                return True

            elif target < matrix[M_i][0]:
                R_i = M_i - 1

            elif target > matrix[M_i][n - 1]:
                L_i = M_i + 1

            else:
                return False


        return False


s = Solution()
print(s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
