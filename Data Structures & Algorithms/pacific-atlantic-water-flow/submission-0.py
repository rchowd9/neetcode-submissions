from collections import deque
from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Find all cells where water can flow to both Pacific and Atlantic oceans.
        Water flows from higher or equal height cells to lower or equal height cells.
        Pacific ocean touches left and top edges, Atlantic ocean touches right and bottom edges.
        """
      
        def bfs(queue: deque, visited: set) -> None:
            """
            Perform BFS to find all cells that can reach the ocean.
            Start from ocean edges and move to cells with equal or greater height.
            """
            while queue:
                # Process all cells at current level
                level_size = len(queue)
                for _ in range(level_size):
                    curr_row, curr_col = queue.popleft()
                  
                    # Check all 4 adjacent cells (up, down, left, right)
                    directions = [[0, -1], [0, 1], [1, 0], [-1, 0]]
                    for delta_row, delta_col in directions:
                        next_row = curr_row + delta_row
                        next_col = curr_col + delta_col
                      
                        # Check if next cell is valid and water can flow backwards
                        # (from next cell to current cell, which means next >= current)
                        if (0 <= next_row < rows and 
                            0 <= next_col < cols and 
                            (next_row, next_col) not in visited and 
                            heights[next_row][next_col] >= heights[curr_row][curr_col]):
                          
                            visited.add((next_row, next_col))
                            queue.append((next_row, next_col))
      
        # Get grid dimensions
        rows = len(heights)
        cols = len(heights[0])
      
        # Initialize visited sets and queues for both oceans
        pacific_visited = set()
        atlantic_visited = set()
        pacific_queue = deque()
        atlantic_queue = deque()
      
        # Add border cells to respective ocean queues
        for row in range(rows):
            for col in range(cols):
                # Pacific ocean: top edge (row=0) or left edge (col=0)
                if row == 0 or col == 0:
                    pacific_visited.add((row, col))
                    pacific_queue.append((row, col))
              
                # Atlantic ocean: bottom edge (row=rows-1) or right edge (col=cols-1)
                if row == rows - 1 or col == cols - 1:
                    atlantic_visited.add((row, col))
                    atlantic_queue.append((row, col))
      
        # Find all cells reachable from each ocean
        bfs(pacific_queue, pacific_visited)
        bfs(atlantic_queue, atlantic_visited)
      
        # Return cells that can reach both oceans (intersection of both sets)
        result = []
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific_visited and (row, col) in atlantic_visited:
                    result.append([row, col])
      
        return result

        