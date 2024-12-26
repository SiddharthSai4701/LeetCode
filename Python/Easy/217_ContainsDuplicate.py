"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true

 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# My Solution
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         numSet = set(nums)

#         if len(numSet) < len(nums):
#             return True
#         else:
#             return False


# Alternate solution
# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         return len(nums) > len(set(nums))


# Greg's Solution - faster because when iterating through a list you can stop at the first duplicate, while set(list) will always continue
# till the end of list, and this is what makes it slower
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h = set()
        for i in nums:
            if i not in h:
                h.add(i)
            else:
                return True
        
        return False


s = Solution()
s.containsDuplicate(nums=[1, 2, 3, 4])
