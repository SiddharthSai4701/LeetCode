"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

 

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
Example 2:

Input: nums = [5], k = 1
Output: 5.00000
 

Constraints:

n == nums.length
1 <= k <= n <= 105
-104 <= nums[i] <= 104
"""
# My SOlution - passed 122/127
# from typing import List
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:

#         def calcAvg(subArr: List[int]):
#             return sum(subArr)/len(subArr)

#         L = 0
#         R = k - 1
#         n = len(nums)

#         maxAvg = float("-inf")

#         while R < n:
#             avg = calcAvg(nums[L:R + 1])
#             maxAvg = max(avg, maxAvg)
#             L += 1
#             R += k

#         return maxAvg

# s = Solution()
# print(s.findMaxAverage([5], 1))


# Solution 2 - also failed. 122/127
# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:

#         def calcAvg(subArr: List[int]):
#             return round(sum(subArr) / len(subArr), 5)

#         L = 0
#         R = k - 1
#         n = len(nums)

#         maxAvg = float("-inf")

#         while R < n:
#             avg = calcAvg(nums[L : R + 1])
#             maxAvg = max(avg, maxAvg)
#             L += 1
#             R = L + k - 1

#         return maxAvg


# Greg's Solution

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr_sum = 0

        for i in range(k):
            curr_sum += nums[i]

        max_avg = curr_sum / k

        for i in range(k, n):

            curr_sum += nums[i]
            curr_sum -= nums[i-k]

            avg = curr_sum / k
            max_avg = max(max_avg, avg)

        return max_avg
