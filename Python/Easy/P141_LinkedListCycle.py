"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

 

Example 1:


Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
Example 2:


Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
Example 3:


Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 

Constraints:

The number of the nodes in the list is in the range [0, 104].
-105 <= Node.val <= 105
pos is -1 or a valid index in the linked-list.
 

Follow up: Can you solve it using O(1) (i.e. constant) memory?
"""
# My approach - not optimal in terms of space. Makes use of extra hash set. However it is faster than the Floyd Algo

# from typing import Optional
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         visitedNodes = set()

#         curr = head
#         while curr and curr.next:
#             if curr not in visitedNodes:
#                 visitedNodes.add(curr)
#                 curr = curr.next
#             else:
#                 return True
#         return False


# s = Solution()

# Node1 = ListNode(3)
# Node2 = ListNode(2)
# Node3 = ListNode(0)
# Node4 = ListNode(-4)

# Node1.next = Node2
# Node2.next = Node3
# Node3.next = Node4
# Node4.next = Node2

# print(s.hasCycle(Node1))

#################################################################################################################################

"""
Greg's approach - use Floyd's Cycle Finding Algorithm

Floyd’s cycle finding algorithm or Hare-Tortoise algorithm is a pointer algorithm that uses only two pointers, moving through the sequence
at different speeds. This algorithm is used to find a loop in a linked list. It uses two pointers one moving twice as fast as the other
one. The faster one is called the fast pointer and the other one is called the slow pointer.

While traversing the linked list one of these things will occur-

The Fast pointer may reach the end (NULL) which shows that there is no loop in the linked list.
The Fast pointer again catches the slow pointer at some time therefore a loop exists in the linked list.
"""

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummyNode = ListNode()
        
        dummyNode.next = head
        slow = fast = dummyNode

        # We need to ensure that fast.next is a node and not None. It's enough to check only for fast because fast will always be ahead of
        # or at the same position as slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast is slow:
                return True
        return False


s = Solution()

Node1 = ListNode(3)
Node2 = ListNode(2)
Node3 = ListNode(0)
Node4 = ListNode(-4)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node2

print(s.hasCycle(Node1))
