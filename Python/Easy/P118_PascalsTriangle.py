"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:




Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]


Constraints:

1 <= numRows <= 30
"""

from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        first_row = [1]
        rows = [first_row]

        for _ in range(1, numRows):
            row = [1]
            for i in range(1, len(rows[-1])):
                num = rows[-1][i - 1] + rows[-1][i]
                row.append(num)
            row.append(1)
            rows.append(row)
        return rows
