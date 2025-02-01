"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
 

Follow up: Could you do this in one pass?
"""

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode()
        dummyNode.next = head
        A = B = dummyNode

        for _ in range(n+1):
            A = A.next

        while A:
            B = B.next
            A = A.next

        # There will always be at least 1 node as this is given in the problem constraints
        # Since we've started with a dummy node, even in the event of there being just 1 node (the head), B will be pointed at the dummy
        # and B.next will point to the head and B.next.next will point to None
        B.next = B.next.next

        return dummyNode.next

    # Added for easy visualization - not part of LeetCode solution
    def display(self, head):
        curr = head
        elements = []

        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(elements))


Node1 = ListNode(1)
Node2 = ListNode(2)
# Node3 = ListNode(3)
# Node4 = ListNode(4)
# Node5 = ListNode(5)
# Node6 = ListNode(6)

Node1.next = Node2
# Node2.next = Node3
# Node3.next = Node4
# Node4.next = Node5
# Node5.next = Node6


s = Solution()
s.display(Node1)
midNode = s.removeNthFromEnd(Node1, 2)
s.display(midNode)
