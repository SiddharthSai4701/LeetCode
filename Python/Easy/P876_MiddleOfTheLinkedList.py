"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.
Example 2:


Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Constraints:

The number of nodes in the list is in the range [1, 100].
1 <= Node.val <= 100
"""

"""
My first solution

Very rudimentary - just loops through the linked list twice and identifies the mid node
"""
# from typing import Optional
# import math

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __str__(self):
#         return str(self.val)


# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         curr = head
#         numNodes = 1

#         while curr.next:
#             curr = curr.next
#             numNodes+=1

#         midNode = math.floor(numNodes/2)

#         i = 0
#         curr = head
#         while i < midNode:
#             curr = curr.next
#             i+=1
#         return curr

#     # Added for easy visualization - not part of LeetCode solution
#     def display(self, head):
#         curr = head
#         elements = []

#         while curr:
#             elements.append(str(curr.val))
#             curr = curr.next
#         print(" -> ".join(elements))


# Node1 = ListNode(1)
# Node2 = ListNode(2)
# Node3 = ListNode(3)
# Node4 = ListNode(4)
# Node5 = ListNode(5)
# Node6 = ListNode(6)

# Node1.next = Node2
# Node2.next = Node3
# Node3.next = Node4
# Node4.next = Node5
# Node5.next = Node6


# s = Solution()
# s.display(Node1)
# midNode = s.middleNode(Node1)
# s.display(midNode)

#################################################################################################################################

"""
My second solution - perhaps two pointers would help

The idea:

Use fast and slow pointers

SLow moves ahead by 1 node while fast moves ahead by 2

Stop when fast becomes None

Return the node which slow is pointing to
"""
# from typing import Optional

# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     def __str__(self):
#         return str(self.val)


# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         dummyNode = ListNode()

#         dummyNode.next = head

#         slow = fast = dummyNode

#         while fast:
#             slow = slow.next
#             if fast.next is None:
#                 return slow
#             fast = fast.next.next

#         return slow


#     # Added for easy visualization - not part of LeetCode solution
#     def display(self, head):
#         curr = head
#         elements = []

#         while curr:
#             elements.append(str(curr.val))
#             curr = curr.next
#         print(" -> ".join(elements))


# Node1 = ListNode(1)
# Node2 = ListNode(2)
# Node3 = ListNode(3)
# Node4 = ListNode(4)
# Node5 = ListNode(5)
# Node6 = ListNode(6)

# Node1.next = Node2
# Node2.next = Node3
# Node3.next = Node4
# Node4.next = Node5
# Node5.next = Node6


# s = Solution()
# s.display(Node1)
# midNode = s.middleNode(Node1)
# s.display(midNode)


####################################################################################################

"""
Greg's Solution - same as my second solution but a little more elegantly written xD
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
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow

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
Node3 = ListNode(3)
Node4 = ListNode(4)
Node5 = ListNode(5)
Node6 = ListNode(6)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6


s = Solution()
s.display(Node1)
midNode = s.middleNode(Node1)
s.display(midNode)
