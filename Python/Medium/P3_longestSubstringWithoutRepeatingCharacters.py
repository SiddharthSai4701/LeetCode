"""
Given a string s, find the length of the longest substring without repeating characters.


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

# My solution - didn't work
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         L = R = 0
#         n = len(s) - 1

#         seen = set()
#         maxLen = 1

#         while R <= n:
#             if s[R] not in seen:
#                 seen.add(s[R])
#                 R += 1
#             else:
#                 maxLen = max(len(s[L:R]), maxLen)
#                 seen = set()
#                 L = R - 1

#         return maxLen


# s = Solution()
# print(s.lengthOfLongestSubstring("abcabcbb"))
# print(s.lengthOfLongestSubstring("dvdf"))
# print(s.lengthOfLongestSubstring(" "))


#######################################################################################
# Greg's Solution

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        longest = 0
        seen = set()
        n = len(s)

        for R in range(n):
            while s[R] in seen:
                seen.remove(s[L])
                L += 1

            # Because we're always looking at at least 1 character
            w = R - L + 1
            longest = max(longest, w)
            seen.add(s[R])

        return longest


s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))
print(s.lengthOfLongestSubstring("dvdf"))
print(s.lengthOfLongestSubstring(" "))
