"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
0 <= k <= nums.length
"""
# from typing import List
# class Solution:
#     def longestOnes(self, nums: List[int], k: int) -> int:
#         flipped = 0
#         L = R = 0
#         length = len(nums)
#         maxConsecutiveOnes = 0

#         while R < length - 1:
#             count = 0

#             while flipped <= k:
#                 if nums[R] == 0:
#                     if flipped < k:
#                         nums[R] = 1
#                         flipped += 1
#                     else:
#                         break
#                 R += 1
#             count = R - L + 1
#             maxConsecutiveOnes = max(maxConsecutiveOnes, count)
#             flipped = 0
#             L += 1
#             R = L
#         return maxConsecutiveOnes
# s = Solution()
# print(s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))


from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_w = 0
        num_zeros = 0
        n = len(nums)
        L = 0

        for R in range(n):
            if nums[R] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[L] == 0:
                    num_zeros -= 1
                L += 1
            
            w = R - L + 1
            max_w = max(max_w, w)
        
        return max_w


s = Solution()
print(s.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], 3))
