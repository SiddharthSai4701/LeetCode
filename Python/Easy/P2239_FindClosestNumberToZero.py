'''
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.

 

Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.
 

Constraints:

1 <= n <= 1000
-105 <= nums[i] <= 105
'''
from typing import List

# My solution
# 117 ms, 16.7 MB
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minDistance = float('inf')
        maxNumber = nums[0]

        for i in nums:
            distance = abs(i - 0)
            if distance == minDistance:
                maxNumber = max(maxNumber, i)
            elif distance < minDistance:
                minDistance = distance
                maxNumber = i
            
        return maxNumber

# Alternate solution
# 122 ms, 16.8 MB
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        closest = nums[0]
        for x in nums:
            if abs(x) < abs(closest):
                closest = x
        
        if closest < 0 and abs(closest) in nums:
            return abs(closest)
        else:
            return closest
        
        # Time: O(n)
        # Space: O(1)  