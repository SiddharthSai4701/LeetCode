"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.



Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0


Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).
"""

from typing import List

# My solution - 18/21 tests pass. Time limit exceeded for remaining

# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         L = 0
#         minLen = float('inf')
#         l = len(nums)

#         for L in range(l):
#             R = L
#             s = 0
#             while s <= target and R<=l-1:
#                 s+= nums[R]

#                 if s >= target:
#                     minLen = min(minLen, (R-L+1))

#                 R += 1

#         if minLen == float('inf'):
#             return 0
#         return minLen

# s = Solution()
# # print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
# print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))

#####################################################################################################################################

# Greg's solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        summ = 0
        l = 0

        for r in range(len(nums)):
            # summ will track the current sum of the window
            summ += nums[r]

            # if the sum is greater than or equal to the target, we store the minimum of the current and prev min length
            while summ >= target:
                min_len = min(min_len, r-l+1)

                # Next we contract the window (by increasing L) in order to try and find a better min length
                # To do this, we first minus the value of nums[L] from summ
                summ -= nums[l]
                l += 1

        return min_len if min_len < float('inf') else 0

s = Solution()
# print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(s.minSubArrayLen(11, [1, 2, 3, 4, 5]))
