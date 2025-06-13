"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 3
Example 2:

Input: root = [1,null,2]
Output: 2


Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:

#         depth = 1

#         if not root:
#             return depth

#         if root.left and root.right:
#             print(root.left.val)
#             print(root.right.val)

#             depth = max(self.maxDepth(root.left), self.maxDepth(root.right))
#         elif not root.left:
#             depth = self.maxDepth(root.right)
#         elif not root.right:
#             depth = self.maxDepth(root.left)


# Greg's Solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)


# Test Case 1
TN1 = TreeNode(3)
TN2 = TreeNode(9)
TN3 = TreeNode(20)
TN4 = TreeNode(15)
TN5 = TreeNode(7)


TN1.left = TN2
TN1.right = TN3

TN3.left = TN4
TN3.right = TN5


s = Solution()
print(s.maxDepth(TN1))


# Test Case 2
A = TreeNode(1)
B = TreeNode(2)

A.right = B
# s.invertTree(A)
