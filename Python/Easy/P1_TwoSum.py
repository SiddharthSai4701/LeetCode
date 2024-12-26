"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?



Approach:

Create an empty dictionary. It will contain the elements of the array and their indices.

Loop through the elements of the array and find the difference of the target and the current element.

Check if the difference is present in the dictionary.

If it is, return the index of the current element and the index of the difference from the dictionary.


"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for index, item in enumerate(nums):
            diff = target - item
            if diff in d:
                return [d[diff], index]
            d[item] = index
        return
    
sol = Solution()
print(sol.twoSum([2,7,11,15], 9))