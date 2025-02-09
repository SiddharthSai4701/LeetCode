"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

"""
My Approach (Didn't work):

A Binary Search approach can be adopted to solve this problem

Start with two pointers, L and R at the extremes of the array
Identify the mid index
If the value at the mid index is equal to the target, return it
If the value at the mid index is greater than the target, the target must be to the left of the mid index 
So the next iteration must search between the indices in the range [M+1, R]
If the value at the mid index is less than the target, the target must be somewhere before the mid index
So the next iteration must search between the indices in the range [L, M]

Greg's Approach:

First perform binary search on the array and identify the minimum index
Check the element at the min index. If it is greater than 
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        L = 0
        R = n - 1


        while L < R:
            M = L + (R - L) // 2

            if nums[M] > nums[R]:
                L = M + 1
            elif nums[M] < nums[R]:
                R = M

        # Now we have the min index (L or R since both are equal)
        minIdx = L

        # If the minIdx is 0, it means that the array is already sorted. Therefore, a traditional binary search will work
        if minIdx == 0:
            L, R = 0, n - 1

        elif target >= nums[0] and target <= nums[minIdx-1]:
            L, R = 0, minIdx - 1

        else:
            L, R = minIdx, n - 1

        while L <= R:
            M = L + (R - L) // 2

            if nums[M] == target:
                return M
            elif nums[M] > target:
                R = M - 1
            else:
                L = M + 1


        return -1

s = Solution()
print(s.search([4, 5, 6, 7, 0, 1, 2], 3))
