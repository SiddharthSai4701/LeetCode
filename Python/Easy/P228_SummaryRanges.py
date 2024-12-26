"""
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
 

Example 1:

Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
Example 2:

Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: The ranges are:
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"
 

Constraints:

0 <= nums.length <= 20
-231 <= nums[i] <= 231 - 1
All the values of nums are unique.
nums is sorted in ascending order.


My Approach:

Have an index variable

While index is less than length of list, continue

Maintain a start and end index

Initially, both are 0

Inside the while, iterate over the elements as long as the difference between the i th and i+1 th element is 1

With each iteration, increment end index and current index

When the condition isn't true and start index isn't equal to end index, append "[startIdx element]->[endIdx element]"

Set startIdx = endIdx + 1

Increment endIdx

if start index is equal to end index, just append the element

Continue
"""

# My Solution
# from typing import List

# class Solution:
#     def summaryRanges(self, nums: List[int]) -> List[str]:
#             currentIdx = startIdx = endIdx = 0
#             finalArray = []
#             while currentIdx < len(nums):
                
#                 if ((currentIdx+1 < len(nums)) and (nums[currentIdx + 1] - nums[currentIdx] == 1)):
#                     endIdx+=1
#                     currentIdx+=1
#                 else:
#                     if(startIdx != endIdx and endIdx < len(nums)):
#                         print(f"{nums[startIdx]}->{nums[endIdx]}")
#                         finalArray.append(f"{nums[startIdx]}->{nums[endIdx]}")
#                         startIdx = endIdx+1
#                         endIdx+=1
#                     elif startIdx == endIdx:
#                         finalArray.append(str(nums[startIdx]))
#                         startIdx+=1
#                         endIdx+=1
#                     currentIdx+=1
#             return finalArray
                    
        
# s = Solution()
# print(s.summaryRanges([0,2,3,4,6,8,9]))


# Greg's Solution
from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        
        while i < len(nums):
            start = nums[i]
            
            while i < len(nums) - 1 and nums[i] + 1 == nums[i + 1]:
                i+=1
                
            if start != nums[i]:
                ans.append(str(start) + '->' + str(nums[i]))
            else:
                ans.append(str(nums[i]))
            
            i+=1
            
        return ans
                    
        
s = Solution()
print(s.summaryRanges([0,2,3,4,6,8,9]))