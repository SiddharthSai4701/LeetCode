"""
Given an array of strings strs, group the 
anagrams
 together. You can return the answer in any order.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
# My solution - 111/126 passed - fails because time limit is exceeded
# Approach was to sort each word and store them as a dictionary w

# from collections import defaultdict
# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """

#         d = defaultdict(str)

#         for i in strs:
#             if tuple(sorted(i)) in d:
#                 d[tuple(sorted(i))] += 1
#             else:
#                 d[tuple(sorted(i))] = 1

#         returnList = []

#         for i in d.keys():
#             s = []
#             for j in strs:
#                 if tuple(sorted(j)) == i:
#                     s.append(j)
#             returnList.append(s)
#         return returnList


# s = Solution()
# print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# Greg's Solution

from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagrams_dict = defaultdict(list)

        for s in strs:
            # Initialize a list of 26 zeros, one for each letter of the alphabet
            count = [0] * 26

            for c in s:
                # Increment the corresponding index of the count array by 1 based on the current letter
                count[ord(c) - ord('a')] += 1

            # The count array will now look something like [0, 1, 0, ..., 0] based on the string we just processed
            key = tuple(count)

            # We append because if the key was not already present, it would have been initialized with an empty list
            anagrams_dict[key].append(s)

        return anagrams_dict.values()

s = Solution()
print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
