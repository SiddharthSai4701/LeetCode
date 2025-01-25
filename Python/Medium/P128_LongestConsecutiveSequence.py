"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""
"""
Greg's solution

Approach

Create a set of the nums array.

For each element in the set, check if the previous number exists. For eg, if the current number is 1, check if 0 exists.

If it does, then the current number cannot be the beginning of a sequence so ignore it.

If a number does not have a number before it, it means it could potentially be the start of a sequence. Proceed to check if it has numbers
after it as well.

Continue until you find a break in the sequence. Then store the length.

Proceed in this manner and each time a sequence breaks, compare the length of the current sequence with the previous longest sequence.

Store the larger value.

Return this value at the end.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s = set(nums)

        longest = 0

        for num in s:
            if num - 1 not in s:
                length = 1
                next_num = num + 1

                while next_num in s:
                    length += 1
                    next_num += 1
                longest = max(longest, length)
                
        return longest

                


s = Solution()
print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))
# print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
# print(s.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
