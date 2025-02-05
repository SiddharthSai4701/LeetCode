"""
You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""
# My Solution
# from collections import Counter
# class Solution:
#     def areAlmostEqual(self, s1: str, s2: str) -> bool:
#         if set(s1) != set(s2) or Counter(s1) != Counter(s2):
#             return False
#         l = len(s1)
#         count = 0
#         for i in range(l):
#             if s1[i] != s2[i]:
#                 count += 1
#         return count == 0 or count == 2

#################################################################################################

from collections import Counter
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        indexes = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indexes.append(i)
            if len(indexes) > 2:
                return False
            
        if len(indexes) == 2:
            i, j = indexes
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        return len(indexes) == 0
        