"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
"""

# My Code
# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """

#         d = dict()

#         for i in magazine:
#             if i not in d.keys():
#                 d[i] = 1
#             else:
#                 d[i] += 1

#         for i in ransomNote:
#             if i not in d.keys():
#                 return False

#             elif d[i] > 1:
#                 d[i]-=1

#             elif d[i] == 1:
#                 del d[i]
#         return True


# s = Solution()
# print(s.canConstruct(ransomNote="aa", magazine="ab"))


# Alternate  ways to build up the dictionary

from collections import defaultdict, Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        # In an ordinary dict, accessing a key that doesn't exist will throw an error
        # But that doesn't happen in a defaultdict
        d = defaultdict(int)
        for i in magazine:
            d[i]+=1

        # An even simpler method is to use Counter
        # d = Counter(magazine)


        for i in ransomNote:
            if i not in d.keys():
                return False

            elif d[i] > 1:
                d[i] -= 1

            elif d[i] == 1:
                del d[i]
        return True


s = Solution()
print(s.canConstruct(ransomNote="aa", magazine="ab"))
