from typing import Optional, List

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        Clones an undirected graph using DFS.
        :param node: The starting node of the graph.
        :return: The cloned starting node.
        """
        if node is None:
            return None  # Edge case: empty graph

        visited = {}  # Map original node -> cloned node

        def dfs(current: 'Node') -> 'Node':
            # If already cloned, return the clone
            if current in visited:
                return visited[current]

            # Clone the current node
            clone = Node(current.val)
            visited[current] = clone

            # Recursively clone neighbors
            for neighbor in current.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone

        return dfs(node)
        