"""
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.



Example 1:

Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
Example 2:

Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.
Example 3:

Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.


Constraints:

1 <= customers.length <= 105
customers consists only of characters 'Y' and 'N'.
"""

"""
INITIAL APPROACH

Assume shop is closed - count total Ys and Ns. The difference gives the penalty for closing the store at the 0th hour
Create a new array with 0th index having the penalty of closing the store at 0th hour
Length of new array will be length of original array + 1
The new array can have "-" in the last index
For each index after that, if Y, subtract 1 from penalty and assign that to the corresponding index of the new array

This won't work because we need to consider the penalty for closing the store at each hour.

------------------------------------------------------------------------------------------------
ALTERNATE APPROACH

Assume store is closed

For each index, all the Y's after it add to the penalty
All the N's before it add to the penalty

Store the penalty for each index in a new penalties array

Return the first occurence of the minimum penalty penalties.index(min(penalties))
"""  

# My solution - 23/42 tests pass. 
# from collections import Counter
# class Solution:
#     def bestClosingTime(self, customers: str) -> int:
#         penalties = [0 for i in range(len(customers))]

#         for index, value in enumerate(customers):
#             counts_Y = Counter(customers[index+1:])
#             counts_N = Counter(customers[:index])
#             if value == "Y":
#                 penalties[index] = 1 + counts_Y["Y"] + counts_N["N"]
#             else:
#                 penalties[index] = counts_Y["Y"] + counts_N["N"]

#         min_penalty_index = penalties.index(min(penalties))

#         if min_penalty_index == len(penalties) -1:
#             return min_penalty_index + 1
#         else:
#             return min_penalty_index

# s = Solution()
# print(s.bestClosingTime("YYNY"))

# NeetCode Solution
# Prefix sum and postfix sum

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        postfix_Y = [0] * (n+1)
        prefix_N = [0] * (n+1)

        for i in range(n - 1, -1, -1):
            postfix_Y[i] = postfix_Y[i+1]
            if customers[i] == "Y":
                postfix_Y[i] += 1

        for i in range(1, n+1):
            prefix_N[i] = prefix_N[i-1]
            if customers[i-1] == "N":
                prefix_N[i] += 1

        min_penalty, idx = float('inf'), 0

        for i in range(n+1):
            penalty = prefix_N[i] + postfix_Y[i]
            if penalty < min_penalty:
                min_penalty = penalty
                idx = i
        return idx

        

s = Solution()
print(s.bestClosingTime("YYNY"))