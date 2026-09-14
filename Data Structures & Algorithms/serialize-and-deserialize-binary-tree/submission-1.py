from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Encodes a tree to a single string using BFS.
        Null nodes are represented by '#'.
        """
        if not root:
            return ""

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("#")  # Marker for null

        # Remove trailing null markers for compactness
        while result and result[-1] == "#":
            result.pop()

        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Decodes your encoded data to tree using BFS.
        """
        if not data:
            return None

        values = data.split(",")
        root = TreeNode(int(values[0]))
        queue = deque([root])
        index = 1

        while queue and index < len(values):
            node = queue.popleft()

            # Left child
            if values[index] != "#":
                node.left = TreeNode(int(values[index]))
                queue.append(node.left)
            index += 1

            # Right child
            if index < len(values) and values[index] != "#":
                node.right = TreeNode(int(values[index]))
                queue.append(node.right)
            index += 1

        return root