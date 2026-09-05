# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional
from math import inf

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Validates if a binary tree is a valid Binary Search Tree (BST).
        Uses in-order traversal to check if values are in strictly increasing order.
      
        Args:
            root: The root node of the binary tree
          
        Returns:
            True if the tree is a valid BST, False otherwise
        """
      
        def inorder_traversal(node: Optional[TreeNode]) -> bool:
            """
            Performs in-order traversal and validates BST property.
            In a valid BST, in-order traversal yields values in strictly increasing order.
          
            Args:
                node: Current node being processed
              
            Returns:
                True if subtree rooted at node is a valid BST, False otherwise
            """
            # Base case: empty tree is valid
            if node is None:
                return True
          
            # Recursively validate left subtree
            if not inorder_traversal(node.left):
                return False
          
            # Check current node value against previous value
            # BST property: current value must be greater than all values in left subtree
            nonlocal previous_value
            if previous_value >= node.val:
                return False
          
            # Update previous value for next comparison
            previous_value = node.val
          
            # Recursively validate right subtree
            return inorder_traversal(node.right)
      
        # Initialize previous value to negative infinity
        # This ensures the first node value will always be greater
        previous_value = -inf
      
        # Start validation from root
        return inorder_traversal(root)