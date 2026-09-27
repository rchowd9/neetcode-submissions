class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Determines if a word exists in the board by traversing adjacent cells.
      
        Args:
            board: 2D grid of characters
            word: Target word to search for
          
        Returns:
            True if word exists in board, False otherwise
        """
      
        def backtrack(row: int, col: int, word_index: int) -> bool:
            """
            Performs DFS with backtracking to search for the word.
          
            Args:
                row: Current row position in board
                col: Current column position in board
                word_index: Current index in the word being matched
              
            Returns:
                True if word can be formed from current position
            """
            # Base case: reached the last character of the word
            if word_index == len(word) - 1:
                return board[row][col] == word[word_index]
          
            # Current cell doesn't match the expected character
            if board[row][col] != word[word_index]:
                return False
          
            # Mark current cell as visited by temporarily changing its value
            original_char = board[row][col]
            board[row][col] = "#"  # Use "#" as visited marker
          
            # Explore all four directions: up, right, down, left
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
          
            for delta_row, delta_col in directions:
                next_row = row + delta_row
                next_col = col + delta_col
              
                # Check if next position is valid and not visited
                if (0 <= next_row < rows and 
                    0 <= next_col < cols and 
                    board[next_row][next_col] != "#"):
                  
                    # Recursively search from the next position
                    if backtrack(next_row, next_col, word_index + 1):
                        board[row][col] = original_char  # Restore before returning
                        return True
          
            # Backtrack: restore the original character
            board[row][col] = original_char
            return False
      
        # Get board dimensions
        rows = len(board)
        cols = len(board[0])
      
        # Try starting the search from every cell in the board
        for start_row in range(rows):
            for start_col in range(cols):
                if backtrack(start_row, start_col, 0):
                    return True
      
        return False
