"""
Given two strings s and t, return true if t is an 
anagram
 of s, and false otherwise.

 

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

# My solution

# from collections import Counter
# class Solution(object):
#     def isAnagram(self, s, t):
#         """
#         :type s: str
#         :type t: str
#         :rtype: bool
#         """

#         s = Counter(s)
#         t = Counter(t)

#         if s == t:
#             return True
#         return False
# s = Solution()
# print(s.isAnagram("abc", "bac"))


# Greg's solution
from collections import Counter


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t): return False

        s = Counter(s)
        t = Counter(t)

        return s == t


s = Solution()
print(s.isAnagram("abc", "bac"))
