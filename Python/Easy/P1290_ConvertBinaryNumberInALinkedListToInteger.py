"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.



Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0


Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        num = ""
        while head:
            num += str(head.val)
            head = head.next

        decimalEquivalent = 0
        for i in range(0, len(num)):
            print(i)
            if num[i] == "1":
                decimalEquivalent += pow(2, len(num) - i - 1)
        return decimalEquivalent


# n1 = ListNode(1)
# n2 = ListNode(0)
# n3 = ListNode(1)

# n1.next = n2
# n2.next = n3

arr = [1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
# arr = [1, 0, 1]

# Create all nodes
nodes = [ListNode(val) for val in arr]

# Link them together
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

s = Solution()
print(s.getDecimalValue(nodes[0]))
