"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.



Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1
Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


Constraints:

The number of nodes in the tree is n.
1 <= k <= n <= 104
0 <= Node.val <= 104


Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution
# Approach: Perform an in order traversal of the tree, add the values of the nodes to a list, sort them and return the
# k-1 th element (because it's 1 indexed)
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

#         nodes = []

#         def in_order_traversal(node):
#             if not node:
#                 return

#             in_order_traversal(node.left)
#             nodes.append(node.val)
#             in_order_traversal(node.right)

#         in_order_traversal(root)
#         nodes.sort()

#         return nodes[k -1]


# Greg's Solution - faster
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        count = [k]
        ans = [0]

        def dfs(node):

            if not node:
                return
            
            dfs(node.left)

            if count[0] == 1:
                ans[0] = node.val


            count[0] -= 1

            if count[0] > 0:
                dfs(node.right)

        dfs(root)
        return ans[0]


# Test Case 1
A = TreeNode(3)
B = TreeNode(1)
C = TreeNode(4)
D = TreeNode(2)

A.left = B
A.right = D

B.right = C

s = Solution()
print(s.kthSmallest(A, 1))
