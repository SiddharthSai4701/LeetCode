"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.



Example 1:


Input: p = [1,2,3], q = [1,2,3]
Output: true
Example 2:


Input: p = [1,2], q = [1,null,2]
Output: false
Example 3:


Input: p = [1,2,1], q = [1,1,2]
Output: false


Constraints:

The number of nodes in both trees is in the range [0, 100].
-104 <= Node.val <= 104
"""

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My First Solution - passed 2 test cases
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         flag = [True]

#         def check(p, q):

#             if not p and not q:
#                 flag[0] = True
#                 return

#             if p.left and q.left:
#                 check(p.left, q.left)
#             if p.right and q.right:
#                 check(p.right, q.right)

#             if p == q:
#                 flag[0] = True
#                 return
#             else:
#                 flag[0] = False
#                 return

#         check(p, q)
#         return flag[0]


# My Second Solution - Solved 1 out of 3. First approach was better as we have to compare each of the nodes of both trees so it's
# better to pass both of them to the helper function
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         flag = [True]

#         def check(node):
#             if not node:
#                 return True

#             isSame = check(node.left) == check(node.right)
            
#             if p.val == q.val:
#                 return True

#             return isSame
        
#         isSame = check(p) == check(q)

#         return isSame
        


# Greg's Solution
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def same(p, q):
            if not p and not q:
                return True
            
            if (p and not q) or (q and not p):
                return False
            
            if p.val != q.val:
                return False
            
            return same(p.left, q.left) and same(p.right, q.right)
        
        return same(p, q)


# Test Case 1
TN1 = TreeNode(1)
TN2 = TreeNode(2)
TN3 = TreeNode(3)


TN1.left = TN2
TN1.right = TN3

TN1_2 = TreeNode(1)
TN2_2 = TreeNode(3)
TN3_2 = TreeNode(2)


TN1_2.left = TN2_2
TN1_2.right = TN3_2

s = Solution()
print(s.isSameTree(TN1, TN1_2))
