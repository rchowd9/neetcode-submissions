# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
            """
            Helper function to check if two trees are identical.
            Two trees are identical if they have the same structure and node values.
            """
            # Base case: if either tree is None, both must be None to be identical
            if tree1 is None or tree2 is None:
                return tree1 is tree2

            # Check if current nodes match and recursively check left and right subtrees
            return (tree1.val == tree2.val and
                   is_same_tree(tree1.left, tree2.left) and
                   is_same_tree(tree1.right, tree2.right))

        # Base case: if root is None, subRoot cannot be its subtree
        if root is None:
            return False

        # Check if current tree matches subRoot, or if subRoot exists in left or right subtree
        return (is_same_tree(root, subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        