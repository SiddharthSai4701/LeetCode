"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        # print("val: ",curr.val)
        # print("next: ",curr.next)

        while curr and curr.next:
            # print("Curr is: ", curr)
            # print("Curr.next is: ", curr.next)
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
    
    def display(self, head):
        curr = head
        elements = []

        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(' -> '.join(elements))


Node1 = ListNode(1)
Node2 = ListNode(1)
Node3 = ListNode(3)

Node1.next = Node2
Node2.next = Node3


s = Solution()
print("Before deleting duplicates:")
s.display(Node1)
s.deleteDuplicates(Node1)
print("After deleting duplicates:")
s.display(Node1)
