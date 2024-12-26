"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

 

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3
Example 2:

Input: jewels = "z", stones = "ZZ"
Output: 0
 

Constraints:

1 <= jewels.length, stones.length <= 50
jewels and stones consist of only English letters.
All the characters of jewels are unique.
"""
# My First Solution
# class Solution(object):
#     def numJewelsInStones(self, jewels, stones):
#         """
#         :type jewels: str
#         :type stones: str
#         :rtype: int
#         """
#         jewelSet = dict()
#         numberOfJewels = 0
#         for i in jewels:
#             if i not in jewelSet.keys():
#                 jewelSet.update({i: 0})
#         for i in stones:
#             if i in jewelSet.keys():
#                 numberOfJewels+=1

#         return numberOfJewels


# My Second Solution
# class Solution(object):
#     def numJewelsInStones(self, jewels, stones):
#         """
#         :type jewels: str
#         :type stones: str
#         :rtype: int
#         """
#         jc=0
#         for i in stones:
#             if i in jewels:
#                 jc+=1

#         return jc


# Greg's Solution
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jc = 0
        jewelSet = set(jewels)
        for i in stones:
            if i in jewelSet:
                jc+=1

        return jc


s = Solution()
s.numJewelsInStones(jewels="aA", stones="aAAbbbb")
# s.numJewelsInStones(jewels="z", stones="ZZ")
