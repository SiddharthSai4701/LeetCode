# from typing import List
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
#         sortedStrs = sorted(strs, key=self.sortStrings)
#         print("SORTED STRS")
#         print(sortedStrs) 
        
#         shortestString = sortedStrs[0]
#         longestSubString = ""
#         # for letter in shortestString:
#             # for word in range(1, len(sortedStrs)):
#             #     if letter in sortedStrs[word]:
#             #         continue
#             #     else:
#             #         break
#         #     shortestString+=letter
#         breakFlag = False
#         i = 0
#         while i < len(shortestString):
#              for word in range(1, len(sortedStrs)):
#                 if longestSubString in sortedStrs[word]:
#                     continue
#                 else:
#                     breakFlag = True
#                     break
#              if breakFlag: 
#                  break
#              longestSubString+=shortestString[i]
#              i+=1
                    
        
#         return longestSubString[:i-1]
    
#     def sortStrings(self, str):
#         return len(str)
        
    
    
# s = Solution()
# print(s.longestCommonPrefix(["flower", "flow", "flight"]))
# print(s.longestCommonPrefix(["flower", "flow", "flowering"]))
# print(s.longestCommonPrefix(["abcd", "abcde", "ac"]))
        
        
"""
Initial approach

Sort the words in ascending order of length

Choose the shortest word

For each letter of the word, check if it exists in all the other words

Start from the first letter

Add to a string

Iterate over the letters of the shortest string and keep appending them to the longestSubString variable

If at any point the substring doesn't exist in any of the words, return the previous longest substring as the longest

If none match, return an empty string

"""

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_length = float('inf')

        for s in strs:
            if (len(s) < min_length):
                min_length = len(s)

        i = 0
        while i < min_length:
            for s in strs:
                if s[i] != strs[0][i]:
                    return s[:i]
            i+=1
        
        return s[:i]
                
        
    def sortStrings(self, str):
        return len(str)
        
    
    
s = Solution()
print(s.longestCommonPrefix(["flower", "flow", "flight"]))
print(s.longestCommonPrefix(["flower", "flow", "flowering"]))
print(s.longestCommonPrefix(["abcd", "abcde", "ac"]))