"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = ListNode()
        curr = d

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else:
                curr.next = list2
                curr = list2
                list2 = list2.next
        
        curr.next = list1 if list1 else list2

        return d.next

    # Added for easy visualization - not part of LeetCode solution
    def display(self, head):
        curr = head
        elements = []

        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(elements))

# 1 -> 2 -> 4
# 1 -> 3 -> 4

s = Solution()

# L1Node1 = ListNode(1)
# L1Node2 = ListNode(2)
# L1Node3 = ListNode(4)

# L1Node1.next = L1Node2
# L1Node2.next = L1Node3

# s.display(L1Node1)


# L2Node1 = ListNode(1)
# L2Node2 = ListNode(3)
# L2Node3 = ListNode(4)

# L2Node1.next = L2Node2
# L2Node2.next = L2Node3

# s.display(L2Node1)

# mergedList = s.mergeTwoLists(L1Node1, L2Node1)
# s.display(mergedList)


# EG 2
L2Node1 = ListNode(1)
L2Node2 = ListNode(2)
L2Node3 = ListNode(4)

L2Node1.next = L2Node2
L2Node2.next = L2Node3

s.display(L2Node1)


L1Node1 = ListNode(5)

s.display(L1Node1)


print("--------------------------------------------------")
mergedList = s.mergeTwoLists(L2Node1, L1Node1)
print("--------------------------------------------------")

s.display(mergedList)
