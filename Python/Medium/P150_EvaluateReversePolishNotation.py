"""
You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
"""
# from typing import List
# class Solution:
#     def evalRPN(self, tokens: List[str]) -> int:
#         operands = ("+", "-", "*", "/")
#         stack = []
#         total = 0

#         for i in tokens:

#             if i not in operands:
#                 stack.append(int(i))
#             else:
#                 if len(stack) >=2:
#                     secondValue = stack.pop()
#                     firstValue = stack.pop()

#                     match i:
#                         case "+":
#                             total = firstValue + secondValue

#                         case "-":
#                             total = firstValue - secondValue

#                         case "*":
#                             total = firstValue * secondValue

#                         case "/":
#                             total = firstValue / secondValue

#                 stack.append(int(total))

#         if stack:
#             return sum(stack)

#         return total

# s = Solution()
# # print(s.evalRPN(["2", "1", "+", "3", "*"]))
# # print(s.evalRPN(["18"]))
# # print(s.evalRPN(["4", "13", "5", "/", "+"]))
# print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
# # print(s.evalRPN(["4", "13", "5", "/", "+"]))

# Greg's solution
from typing import List
from math import ceil, floor
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if t in "+=*/":
                b, a = stk.pop(), stk.pop()

                if t == "+":
                    stk.append(a + b)
                elif t == "-":
                    stk.append(a - b)
                elif t == "*":
                    stk.append(a * b)
                elif t == "/":
                    division = a / b
                    if division > 0:
                        stk.append(floor(division))
                    else:
                        stk.append(ceil(division))
            else:
                stk.append(int(t))

        return stk[0]


s = Solution()
# print(s.evalRPN(["2", "1", "+", "3", "*"]))
# print(s.evalRPN(["18"]))
# print(s.evalRPN(["4", "13", "5", "/", "+"]))
# print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
print(s.evalRPN(["4", "3", "-"]))
