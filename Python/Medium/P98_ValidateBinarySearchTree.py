"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:


Input: root = [2,1,3]
Output: true
Example 2:


Input: root = [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.


Constraints:

The number of nodes in the tree is in the range [1, 104].
-231 <= Node.val <= 231 - 1
"""

"""
Thought process - immediate thought was to do an in order traversal to get the order of the nodes
If they are sorted, then it's a valid BST
The only issue is when there are multiple nodes with the same value
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My First Solution - Passes 35/86 tests because I'm only considering immediate children
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:

#         isValid = [True]

#         def validated(root):

#             if not root:
#                 return

#             if root.left:
#                 if root.val <= validated(root.left):
#                     isValid[0] = False
#                     return

#             if root.right:
#                 if root.val >= validated(root.right):
#                     isValid[0] = False
#                     return

#             return root.val
#         validated(root)
#         return isValid[0]

# My Second Solution - Passes 73/86 tests but fails if there are trees with equal nodes
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:

#         nodes = []

#         def in_order_traversal(root):

#             if not root:
#                 return

#             in_order_traversal(root.left)
#             nodes.append(root.val)
#             in_order_traversal(root.right)

#         in_order_traversal(root)

#         return nodes == sorted(nodes)

# My Third Solution - Finally worked but doesn't seem too efficient
# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:

#         nodes = []

#         def in_order_traversal(root):

#             if not root:
#                 return

#             in_order_traversal(root.left)
#             nodes.append(root.val)
#             in_order_traversal(root.right)

#         in_order_traversal(root)

#         return nodes == sorted(nodes) and nodes == set(nodes)

# Greg's Solution - wayyy faster
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def is_valid(root, minn, maxx):

            if not root:
                return True
            
            if root.val >= maxx or root.val <= minn:
                return False
            
            return is_valid(root.left, minn, root.val) and is_valid(root.right, root.val, maxx)
        
        return is_valid(root, float('-inf'), float('inf'))


# Test Case 1
A = TreeNode(2)
B = TreeNode(2)
C = TreeNode(2)
# D = TreeNode(1)
# E = TreeNode(3)

A.left = B
A.right = C

# B.left = D
# B.right = E

s = Solution()
print(s.isValidBST(A))
