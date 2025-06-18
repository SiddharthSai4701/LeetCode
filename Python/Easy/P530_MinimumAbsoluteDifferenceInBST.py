"""
Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.



Example 1:


Input: root = [4,2,6,1,3]
Output: 1
Example 2:


Input: root = [1,0,48,null,null,12,49]
Output: 1


Constraints:

The number of nodes in the tree is in the range [2, 104].
0 <= Node.val <= 105
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My Solution - super slow
# Approach: Perform an in order traversal of the tree, add the values of the nodes to a list, sort them and then compute the differences
# between consecutive elements until you find the lowest one
# class Solution:
#     def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

#         nodes = []
#         min_diff = float('inf')

#         def in_order_traversal(node):
#             if not node:
#                 return

#             in_order_traversal(node.left)
#             nodes.append(node.val)
#             in_order_traversal(node.right)

#         in_order_traversal(root)

#         l = len(nodes)
#         for i in range(0,l-1):
#             min_diff = min(min_diff, abs(nodes[i] - nodes[i+1]))
#         return min_diff


# Greg's Solution
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        min_distance = [float("inf")]
        prev = [None]

        def dfs(root):
            if root is None:
                return

            dfs(root.left)

            if prev[0] is not None:
                # The
                min_distance[0] = min(min_distance[0], root.val - prev[0])

            prev[0] = root.val

            dfs(root.right)

        dfs(root)

        return min_distance[0]


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
print(s.getMinimumDifference(A))
