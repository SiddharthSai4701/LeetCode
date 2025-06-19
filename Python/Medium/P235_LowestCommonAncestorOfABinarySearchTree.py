"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”



Example 1:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:


Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2


Constraints:

The number of nodes in the tree is in the range [2, 105].
-109 <= Node.val <= 109
All Node.val are unique.
p != q
p and q will exist in the BST.
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# My Solution - Passed 26/30
# class Solution:
#     def lowestCommonAncestor(
#         self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
#     ) -> "TreeNode":

#         lca = [root]

#         def checkLCA(root, p, q):
#             if not root:
#                 return

#             if root.val > p.val and root.val > q.val:
#                 checkLCA(root.left, p, q)

#             if root.val < p.val and root.val < q.val:
#                 checkLCA(root.right, p, q)

#             if root.val > p.val and root.val < q.val:
#                 lca[0] = root

#             if root.val == p.val or root.val == q.val:
#                 lca[0] = root

#             return

#         checkLCA(root, p, q)
#         return lca[0]


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lca = [root]

        def search(root):

            if not root:
                return
            
            lca[0] = root

            if root is p or root is q:
                return
            elif root.val < p.val and root.val < q.val:
                search(root.right)
            elif root.val > p.val and root.val > q.val:
                search(root.left)
            else:
                return
        search(root)
        return lca[0]


# Test Case 1
A = TreeNode(6)
B = TreeNode(2)
C = TreeNode(8)
D = TreeNode(0)
E = TreeNode(4)
F = TreeNode(7)
G = TreeNode(9)
H = TreeNode(3)
I = TreeNode(5)

A.left = B
A.right = C

B.left = D
B.right = E

C.left = F
C.right = G

E.left = H
E.right = I

s = Solution()
# print(s.lowestCommonAncestor(A, B, E).val)

# Test Case 2

A = TreeNode(5)
B = TreeNode(3)
C = TreeNode(6)
D = TreeNode(1)
E = TreeNode(4)
F = TreeNode(2)

A.left = B
A.right = C

B.left = D
B.right = E

D.left = F
print(s.lowestCommonAncestor(A, E, F).val)
