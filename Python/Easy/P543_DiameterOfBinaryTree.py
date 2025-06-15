"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.



Example 1:


Input: root = [1,2,3,4,5]
Output: 3
Explanation: 3 is the length of the path [4,2,1,3] or [5,2,1,3].
Example 2:

Input: root = [1,2]
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 104].
-100 <= Node.val <= 100
"""

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My SOlution - passed 1 test case
# class Solution:
#     def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
#         maxLen = [0]

#         def length(root):

#             if not root:
#                 return 0

#             left_diameter = length(root.left)
#             if left_diameter > 0:
#                 maxLen[0] += 1
#             right_diameter = length(root.right)
#             if right_diameter > 0:
#                 maxLen[0] += 1

#             return 1 + left_diameter + right_diameter

#         length(root)
#         return maxLen[0]


# Greg's Solution
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = [0]

        def height(root):

            if root is None:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)

            largest_diameter[0] = max(largest_diameter[0], left_height + right_height)

            return 1 + max(left_height, right_height)
        
        height(root)
        return largest_diameter[0]
        



# Test Case 1
TN1 = TreeNode(1)
TN2 = TreeNode(2)
TN3 = TreeNode(3)
TN4 = TreeNode(4)
TN5 = TreeNode(5)


TN1.left = TN2
TN1.right = TN3

TN2.left = TN4
TN2.right = TN5


s = Solution()
print(s.diameterOfBinaryTree(TN1))
