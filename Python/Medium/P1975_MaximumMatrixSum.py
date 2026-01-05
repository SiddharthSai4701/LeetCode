"""
You are given an n x n integer matrix. You can do the following operation any number of times:

Choose any two adjacent elements of matrix and multiply each of them by -1.
Two elements are considered adjacent if and only if they share a border.

Your goal is to maximize the summation of the matrix's elements. Return the maximum sum of the matrix's elements using the operation mentioned above.

 

Example 1:


Input: matrix = [[1,-1],[-1,1]]
Output: 4
Explanation: We can follow the following steps to reach sum equals 4:
- Multiply the 2 elements in the first row by -1.
- Multiply the 2 elements in the first column by -1.
Example 2:


Input: matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
Output: 16
Explanation: We can follow the following step to reach sum equals 16:
- Multiply the 2 last elements in the second row by -1.
 

Constraints:

n == matrix.length == matrix[i].length
2 <= n <= 250
-105 <= matrix[i][j] <= 105
"""
"""
My approach

- If the number of negative numbers is odd, at best we can only reduce the matrix to have 1 negative number.
 - If the number of negative numbers is even, we can reduce the matrix to have 0 negative numbers.

1. Sum up the values in the matrix
2. Count the negative values
3. If odd, find the smallest absolute value and subtract it from the total
4. If even, return the total
"""
from typing import List
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        matrix_sum = 0
        negative_count  = 0
        smallest_abs_neg = float('inf')
        for row in matrix:
            for n in row:
                if n < 0:
                    negative_count += 1
                smallest_abs_neg = min(smallest_abs_neg, abs(n))
                matrix_sum += abs(n)

        if negative_count % 2 == 0:
            return matrix_sum

        return matrix_sum - (2 * smallest_abs_neg)