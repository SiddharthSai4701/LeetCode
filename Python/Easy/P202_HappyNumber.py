"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        cur = str(n)

        while cur not in seen:
            seen.add(cur)
            summ = 0

            for digit in cur:
                digit = int(digit)
                summ += pow(digit, 2)

            if summ == 1:
                return True
            cur = str(summ)

        return False
s = Solution()
print(s.isHappy(19))