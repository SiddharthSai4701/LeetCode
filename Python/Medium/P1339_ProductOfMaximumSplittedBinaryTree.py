"""
Given the root of a binary tree, split the binary tree into two subtrees by removing one edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
 

Constraints:

The number of nodes in the tree is in the range [2, 5 * 104].
1 <= Node.val <= 104
"""
"""
The approach:
1. Find the sum of the entire tree first. This will allow us to find the sum of the two subtrees by subtracting the sum of the
current subtree from the total sum.
2. Traverse the tree and find each subtree's sum.
3. For each subtree's sum, calculate the product of the sum and the total sum - the sum of the current subtree.
4. Return the maximum product.
5. Return the maximum product modulo 10^9 + 7 as that is what's been asked in the problem.
"""


from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        all_sums = []

        def tree_sum(root):
            if root is None:
                return 0
            
            s = root.val + tree_sum(root.left) + tree_sum(root.right)
            all_sums.append(s)
            return s
        
        total_sum = tree_sum(root)
        best_sum = 0

        for s in all_sums:
            best_sum = max(best_sum, s * (total_sum - s))
        
        return best_sum % (10**9 + 7)
