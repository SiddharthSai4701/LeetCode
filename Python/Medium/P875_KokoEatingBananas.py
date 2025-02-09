"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
"""
from typing import List
from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # k is an acceptable number if Koko can finish all the piles by eating at this rate
        def k_works(k):
            hours = 0
            for p in piles:
                hours += ceil(p / k)
            return hours <= h

        # We know that by eating bananas equal to the largest pile every hour will ensure that we finish all the piles within the given time frame.
        # But this may not provide the best solution. Koko must eat at least 1 banana per hour and at most the max of the pile. So we begin
        # by iterating in this interval
        L = 1
        R = max(piles)

        while L < R:
            k = L + (R - L) // 2

            # If we have an acceptable k, we should search between [L, k]. We could potentially find a smaller value to the left of it
            if k_works(k):
                R = k

            # If it doesn't work, it means k is too small and we should look to the right of the mid value. [k+1, R]
            else:
                L = k + 1
        return R
