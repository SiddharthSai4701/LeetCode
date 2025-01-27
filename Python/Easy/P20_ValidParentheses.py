"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if len(s) % 2 != 0:
            return False

        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if stack:
                    bracket = stack.pop()
                    if (i == "]" and bracket == "[") or (i == ")" and bracket == "(") or (i == "}" and bracket == "{"):
                        continue
                    else:
                        return False

                else:
                    return False
        if len(stack) == 0:
            return True
        return False
    

s = Solution()
print(s.isValid("["))
# print(s.isValid("(]"))
