"""
Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 

Example 1:


Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.
Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
-105 <= Node.val <= 105
"""
"""
Since we need to find the sum of each level, the immediate thought was to use BFS

Approach:
1. Create a queue and add the root to it
2. The first row will always have just one node which is the root
3. In each iteration, the queue will have all the nodes at the current level
4. We will dequeue the nodes from the queue and add the values to a sum variable
5. If the node has children, we'll add them to the queue
6. At the end of each iteration of the outer loop, compare the sum of the current level with the max_sum
7. If the sum is greater than the max_sum, we'll update the max_sum and the ans
8. Return the ans

"""


from typing import Optional
import collections

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_sum, ans, level = float('-inf'), 0, 0

        q = collections.deque()
        q.append(root)

        while q:
            level += 1
            sum_at_level = 0
            for _ in range(len(q)):
                node = q.popleft()
                sum_at_level += node.val

                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)
                
            if sum_at_level > max_sum:
                max_sum, ans = sum_at_level, level
        return ans
