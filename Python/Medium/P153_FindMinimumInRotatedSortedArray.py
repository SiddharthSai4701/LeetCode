"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.

 

Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
 

Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""

"""
My Approach (Didn't work):

We know that the elements are all unique

THere are 2 possibilities:
    1. The array has been rotated n times which is equivalent to no rotation at all. So all elements are in strictly increasing order
    2. The array has been rotated some n - 1 times in which case we can partition the array into two parts:
        i.  One half with strictly increasing elements
        ii. The other half with strictly decreasing elements

        Eg. [0,1,2,4,5,6,7] -> After 4 rotations: [4,5,6,7,0,1,2] -> From index 4, elements strictly increase
                                                                     From index 3, moving backwards, elements strictly decrease
    The partition can be identified by finding the index M where M - 1 is greater than M and M + 1 is less than M


Greg's Approach:

Divide the array into 2
Check if the value at the mid index is less than the value of the right pointer
If yes, it means that the minimum vale lies somewhere in the range (M, R]
If not, it means that the minimum value lies somewhere in the range [L, M]
"""
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        L = 0
        R = len(nums) - 1

        while L < R:
            M = L + (R - L) // 2

            if nums[M] < nums[R]:
                R = M
            elif nums[M] > nums[R]:
                L = M + 1

        return nums[R]

s = Solution()
print(s.findMin([4, 5, 6, 7, 0, 1, 2]))
