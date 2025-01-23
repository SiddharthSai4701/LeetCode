"""
Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 104
text consists of lower case English letters only.
 

Note: This question is the same as 2287: Rearrange Characters to Make Target String.
"""

"""
My approach

Convert the given string into a dictionary

Loop through the word balloon, decrementing the count of each letter if it exists in the dictionary

After every complete iteration over the word balloon, increment the count by 1

If a letter's count in the dictionary becomes 0, delete the key

If a letter isn't present in the dictionary, break out of the loop and return the current count
"""

# My solution
# from collections import Counter

# class Solution(object):
#     def maxNumberOfBalloons(self, text):
#         """
#         :type text: str
#         :rtype: int
#         """
#         text_dict = dict(Counter(text))

#         count = 0

#         while True:
#             for i in "balloon":
#                 if i not in text_dict:
#                     return count
#                 elif text_dict[i] - 1 == 0:
#                     del text_dict[i]
#                 else:
#                     text_dict[i] -= 1
#             count+=1


# s = Solution()
# print(s.maxNumberOfBalloons("loonbalxballpoon"))


# Greg's solution

from collections import defaultdict


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        counter = defaultdict(int)

        for c in text:
            if c in "balloon":
                counter[c] += 1

        if any(c not in counter for c in "balloon"):
            return 0
        else:
            return min(
                counter["b"],
                counter["a"],
                counter["l"] // 2,
                counter["o"] // 2,
                counter["n"],
            )


s = Solution()
print(s.maxNumberOfBalloons("loonbalxballpoon"))
