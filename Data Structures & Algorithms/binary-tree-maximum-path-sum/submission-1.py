# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize a variable to store the global maximum path sum
        self.max_sum = float('-inf')

        # Helper function to perform DFS
        def dfs(node):
            if not node:
                return 0

            # Recursively calculate max path sum for left and right subtrees
            left_max = max(0, dfs(node.left))   # Ignore negative paths
            right_max = max(0, dfs(node.right))

            # Update global max_sum with the current node's contribution
            self.max_sum = max(self.max_sum, node.val + left_max + right_max)

            # Return the maximum path sum including the current node
            return node.val + max(left_max, right_max)

        # Start DFS from the root
        dfs(root)

        return self.max_sum

        