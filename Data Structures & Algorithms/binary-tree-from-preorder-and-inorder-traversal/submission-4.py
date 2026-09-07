# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map each value to its index in inorder for O(1) lookups
        index_map = {val: i for i, val in enumerate(inorder)}
        
        # Pointer to track current root in preorder
        self.pre_idx = 0

        def array_to_tree(left, right):
            # No elements to construct the tree
            if left > right:
                return None
            
            # Select the current root value
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            
            # Build the root node
            root = TreeNode(root_val)
            
            # Build left and right subtrees
            root.left = array_to_tree(left, index_map[root_val] - 1)
            root.right = array_to_tree(index_map[root_val] + 1, right)
            
            return root
        
        return array_to_tree(0, len(inorder) - 1)
