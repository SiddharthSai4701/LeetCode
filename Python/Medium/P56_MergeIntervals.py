"""
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104


My Approach:

Take an interval and consider starti and endi to be the two values of this interval

Loop through the remaining intervals

If the starting index of the next interval is between starti and endi and the ending index
is greater than endi, update endi to be this new ending index

If the starting index of the next interval is between starti and endi and the ending index
is lesser than endi, update endi to be this new ending index

"""
# from typing import List
# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         sorted_intervals = sorted(intervals)
#         merged_intervals = []
        
#         for i in sorted_intervals:
            
#             if len(merged_intervals) == 0:
#                 merged_intervals.append(i)
#                 continue
            
#             if i[0] <= merged_intervals[-1][1]:
                
#                 if merged_intervals[-1][1] == i[1]:
#                     continue
#                 elif merged_intervals[-1][1] < i[1]:
#                     merged_intervals[-1][1] = i[1]
#                     continue
#             if i[1] < merged_intervals[-1][1]:
#                 continue
#             merged_intervals.append(i)
            
#         return merged_intervals
    
# s = Solution()
# print(s.merge([[1,3],[8,10],[2,6],[15,18]]))
# print(s.merge([[1,4],[2,3]]))


# Greg's code:

from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda interval: interval[0])
        merged = []
        
        for interval in intervals:
            
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
                
            else:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        return merged
    
s = Solution()
print(s.merge([[1,3],[8,10],[2,6],[15,18]]))
# print(s.merge([[1,4],[2,3]]))
            