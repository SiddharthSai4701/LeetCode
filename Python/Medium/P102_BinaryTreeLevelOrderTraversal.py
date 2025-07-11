"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
from typing import Optional, List
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        
        queue = deque()
        queue.append(root)
        ans = []

        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)

                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            
            ans.append(level)
        
        return ans

# Test Case 1
TN1 = TreeNode(1)

# Test Case 2
A = TreeNode(3)
B = TreeNode(9)
C = TreeNode(20)
D = TreeNode(15)
E = TreeNode(7)

A.left = B
A.right = C

C.left = D
C.right = E

s = Solution()
print(s.levelOrder(A))
