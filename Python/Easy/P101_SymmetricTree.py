"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:


Input: root = [1,2,2,3,4,4,3]
Output: true
Example 2:


Input: root = [1,2,2,null,3,null,3]
Output: false


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100


Follow up: Could you solve it both recursively and iteratively?
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# My First Solution - passed all tests
# Approach similar to P 100  except that instead of comparing the left nodes of two different trees, we compare the
# left and right nodes of the same tree
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(p, q):
            if not p and not q:
                return True

            if (p and not q) or (q and not p):
                return False

            if p.val != q.val:
                return False

            return symmetric(p.left, q.right) and symmetric(p.right, q.left)

        return symmetric(root.left, root.right)

# Greg's Solution
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def same(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1 or not root2:
                return False
            
            if root1.val != root2.val:
                return False
            
            return same(root1.left, root2.right) and same(root1.right, root2.left)
        
        return same(root, root)




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
