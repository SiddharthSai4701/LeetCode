"""
Given a binary tree, determine if it is height-balanced.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution - 203 / 228 testcases passed
"""
The approach

Find the depth of each subtree and return it

If the difference is greater than 1, return False
"""
# class Solution:
#     def isBalanced(self, root: Optional[TreeNode]) -> bool:
#         if not root:
#             return True

#         left = self.depth(root.left)
#         right = self.depth(root.right)

#         return abs(right-left) <= 1

#     def depth(self, root: Optional[TreeNode]) -> int:

#         if not root:
#             return 0

#         left = self.maxDepth(root.left)
#         right = self.maxDepth(root.right)

#         return abs(left-right)

# Greg's Solution
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        balanced = [True]

        def height(root):
            
            if not root:
                return 0
            
            left_height = height(root.left)
            if balanced[0] is False: return 0

            right_height = height(root.right)

            if abs(right_height-left_height) > 1:
                balanced[0] = False
                return 0

            return 1 + max(left_height, right_height)

        height(root)
        return balanced[0] 


        