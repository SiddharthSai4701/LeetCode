"""
Given the root of a binary tree, return the preorder traversal of its nodes' values.



Example 1:

Input: root = [1,null,2,3]

Output: [1,2,3]

Explanation:



Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [1,2,4,5,6,7,3,8,9]

Explanation:



Example 3:

Input: root = []

Output: []

Example 4:

Input: root = [1]

Output: [1]



Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100


Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        nodes = []

        def pre_order_traversal(root):

            if not root:
                return

            nodes.append(root.val)
            pre_order_traversal(root.left)
            pre_order_traversal(root.right)

        pre_order_traversal(root)

        return nodes


# Test Case 1
A = TreeNode(4)
B = TreeNode(2)
C = TreeNode(6)
D = TreeNode(1)
E = TreeNode(3)

A.left = B
A.right = C

B.left = D
B.right = E

s = Solution()
print(s.preorderTraversal(A))
