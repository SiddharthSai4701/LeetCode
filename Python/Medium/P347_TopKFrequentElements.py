"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.


Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

"""

from typing import List
import heapq
from collections import Counter

# My first solution - worst code I've ever written
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         heapq.heapify(nums)
#         freq = {}
#         seen = set()

#         while nums:
#             n = heapq.heappop(nums)
#             if n in seen:
#                 freq[n] += 1
#             else:
#                 seen.add(n)
#                 freq[n] = 1
#         # print(freq)
#         most_freq = len(seen) * [0]

#         i = 0
#         for ob in freq:
#             most_freq[i] = (ob, freq[ob])
#             i+=1

#         # print(most_freq)
#         # freq = sorted(freq)
#         freq = sorted(most_freq, key=self.sortBasedOnTuple, reverse=True)
#         final = []
#         for i in range(k):
#             final.append(freq[i][0])
#         return final

# def sortBasedOnTuple(self, freq):
#     return freq[1]

# My Second Solution - better
# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         counts = Counter(nums)
#         freq = []

#         for c in counts.keys():
#             freq.append((c, counts[c]))

#         freq = sorted(freq, key=self.sortBasedOnTuple, reverse=True)

#         return [freq[i][0] for i in range(k)]

#     def sortBasedOnTuple(self, freq):
#         return freq[1]

# Greg's Solution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []

        for key, val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                heapq.heappushpop(heap, (val, key))

        return [h[1] for h in heap]

        


s = Solution()
# print(s.findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
# print(s.topKFrequent(nums=[3, 2, 3, 1, 2, 4, 5, 5, 6], k=4))
print(s.topKFrequent(nums=[1, 1, 1, 2, 2, 3], k=2))
