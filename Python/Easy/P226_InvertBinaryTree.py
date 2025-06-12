"""
Given the root of a binary tree, invert the tree, and return its root.



Example 1:


Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
Example 2:


Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
# My Solution

from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

#         if root and root.left and root.right:
#             temp = root.left
#             root.left = root.right
#             root.right = temp
#             self.invertTree(root.left)
#             self.invertTree(root.right)
#         elif root and root.left and not root.right:
#             root.right = root.left
#             root.left = None
#             self.invertTree(root.right)
#         elif root and root.right and not root.left:
#             root.left = root.right
#             root.right = None
#             self.invertTree(root.left)
#         return root

#     def pre_order_traversal(self, node):

#         if not node:
#             return

#         print(node.val, end=" ")
#         self.pre_order_traversal(node.left)
#         self.pre_order_traversal(node.right)


# Greg's Solution
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None
        
        root.left, root.right = root.right, root.left
        
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def pre_order_traversal(self, node):

        if not node:
            return

        print(node.val, end=" ")
        self.pre_order_traversal(node.left)
        self.pre_order_traversal(node.right)


# Test Case 1
TN1 = TreeNode(4)
TN2 = TreeNode(2)
TN3 = TreeNode(7)
TN4 = TreeNode(1)
TN5 = TreeNode(3)
TN6 = TreeNode(6)
TN7 = TreeNode(9)

TN1.left = TN2
TN1.right = TN3

TN2.left = TN4
TN2.right = TN5

TN3.left = TN6
TN3.right = TN7

s = Solution()
# s.invertTree(TN1)
# s.pre_order_traversal(TN1)
s.pre_order_traversal(s.invertTree(TN1))
print()


# Test Case 2
A = TreeNode(2)
B = TreeNode(1)
C = TreeNode(3)

A.left = B
A.right = C
# s.invertTree(A)
# s.pre_order_traversal(A)
