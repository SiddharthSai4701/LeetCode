"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.


Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""

# My Solution - Beats 100% of other solutions in runtime, beats 17.54% of other solutions in space
# class Solution:
#     def lengthOfLastWord(self, s: str) -> int:
#         return len(s.split()[-1])


# Greg's Solution - Beats 100% of other solutions in runtime, beats 37.73%% of other solutions in space
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        n = len(s)
        i = n - 1

        # Use i to ignore all trailing white spaces
        while s[i] == " ":
            i -= 1

        letter_count = 0

        # This will loop through till i which will be the last letter of the last word
        for i in range(i + 1):
            if s[i] != " ":
                letter_count += 1
            else:
                letter_count = 0

        return letter_count


s = Solution()
print(s.lengthOfLastWord("   fly me   to   the moon  "))
