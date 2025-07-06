"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 105
-104 <= nums[i] <= 104
"""
from typing import List
import heapq

# My Solution
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heapq.heapify(nums)

#         n = len(nums)
#         new_list = [0] * n

#         for i in range(n):
#             minn = heapq.heappop(nums)
#             new_list[i] = minn
#         print(new_list)
#         return new_list[-k]


# Greg's First Solution - use a max heap
# The largest element will be at the top of the heap (the largest value will be negated so it's actually the smallest)
# Popping k times will give the kth smallest. But since we've negated at the start, we negate again and get the kth largest.
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         # Max heap of size N
#         # Time: O(N + k log N)
#         # Space: O(1)

#         for i in range(len(nums)):
#             nums[i] = -nums[i]

#         heapq.heapify(nums)

#         for _ in range(k-1):
#             heapq.heappop(nums)

#         return -heapq.heappop(nums)

# Greg's Second solution - use a min heap that we build up
# Heap will never contain more than k elements
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(N log k)
        # Space: O(k)

        l = len(min_heap)
        min_heap = []

        for num in nums:
            if l < k:
                heapq.heappush(min_heap, nums)
            else:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]


s = Solution()
# print(s.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
print(s.findKthLargest(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
