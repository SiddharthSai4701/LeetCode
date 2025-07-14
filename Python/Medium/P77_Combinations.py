"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.


Constraints:

1 <= n <= 20
1 <= k <= n
"""

from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(x: int):
            if len(sol) == k:
                res.append(sol[:])
                return
            
            # Don't use the number
            remaining_nums = x
            still_required = k - len(sol)

            if remaining_nums > still_required:
                backtrack(x-1)

            
            # Use number
            sol.append(x)
            backtrack(x-1)
            sol.pop()


        backtrack(n)

        return res
    
s = Solution()
print(s.combine(4,2))