"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
"""

"""
My approach:

The key point seems to be that each version is based on the previous

Therefore, the moment we find a bad version, we need to check if the previous version is good.
    - If yes, then this is the first bad version and all subsequent versions must be ignored.
    - If the current version is not a bad version, we keep moving forward until we arrive at a bad version and then identify the first bad
      version as mentioned above.
To minimize the API calls, we could divide the array in half and pass the mid value to the API. If we get true, move forward.
If false, move backwards till you find the first false.

Once you arrive at a value, check if it is a bad version.
If it is, return it
If not, we've landed on the last good version so the next one must be bad. Return the next version.

This problem is an interesting variation of Binary Search
"""

# The isBadVersion API is already defined for you.
def isBadVersion(version: int, bad=2) -> bool: # My def of isBadVersion...ignore
    print("VERSION: ",version)
    if version >= bad:
        return True
    return False

def createArray(n: int): # Function written for my convenience...ignore
    print([i for i in range(1,n+1)])

# My solution
class Solution:
    def firstBadVersion(self, n: int) -> int:
        L = 1
        R = n

        while L <= R:
            M = L + (R - L) // 2
            result = isBadVersion(M)

            if result:
                R = M - 1
            else:
                L = M + 1

        if not isBadVersion(M):
            return M + 1
        else:
            return M


s = Solution()
createArray(3)
print(s.firstBadVersion(3))
