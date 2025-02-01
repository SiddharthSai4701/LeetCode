"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.

 

Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
 

Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""

"""
My attempt

"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        newHead = Node(head.val)
        newCurr = newHead

        while curr and curr.next:
            curr = curr.next
            newNode = Node(curr.val)
            newCurr.next = newNode
            newCurr = newCurr.next

        curr = head
        newCurr = newHead
        while curr and curr.next:
            random = curr.random
            newCurr.random = random
            curr = curr.next
            newCurr = newCurr.next

        return newHead  
"""

# Greg's Solution

from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head: return None

        curr = head

        old_to_new_node_map = dict()

        while curr:
            node = Node(x=curr.val)
            old_to_new_node_map[curr] = node
            curr = curr.next
        
        curr = head
        while curr:
            new_node = old_to_new_node_map[curr]
            new_node.next = old_to_new_node_map[curr.next] if curr.next else None
            new_node.random = old_to_new_node_map[curr.random] if curr.random else None
            curr = curr.next

        old_to_new_node_map[head]

    # Added for easy visualization - not part of LeetCode solution
    def display(self, head):
        curr = head
        elements = []

        while curr:
            elements.append(str(curr.val))
            curr = curr.next
        print(" -> ".join(elements))


Node1 = Node(7)
Node2 = Node(13)
Node3 = Node(11)
Node4 = Node(10)
Node5 = Node(1)
# Node6 = Node(6)

Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
# Node5.next = Node6


s = Solution()
s.display(Node1)
midNode = s.copyRandomList(Node1)
s.display(midNode)
