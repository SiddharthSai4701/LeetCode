"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

 

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achieve this answer too.
 

Constraints:

1 <= s.length <= 105
s consists of only uppercase English letters.
0 <= k <= s.length
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        L = 0
        counts = [0] * 26

        for R in range(len(s)):
            # The counts array will be used to keep track of the uppercase English letters that we've seen
            counts[ord(s[R]) - 65] += 1

            # While this condition is true, it means we have more characters that need to be changes than we are allowed to (k)
            # Therefore, we have to make our window valid by shortening it
            while (R - L + 1) - max(counts) > k:
                counts[ord(s[L]) - 65] -= 1
                L += 1

            longest = max(longest, (R - L + 1))

        return longest

            
            

s = Solution()
print(s.characterReplacement("ABAB", 2))