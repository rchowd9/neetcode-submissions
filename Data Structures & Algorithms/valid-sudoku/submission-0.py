from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Checks if a given 9x9 Sudoku board is valid.
        Rules:
        - Each row must contain digits 1-9 without repetition.
        - Each column must contain digits 1-9 without repetition.
        - Each 3x3 sub-box must contain digits 1-9 without repetition.
        Empty cells are represented by '.'.
        """
        if not board or len(board) != 9 or any(len(row) != 9 for row in board):
            return False  # Invalid board dimensions

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # 3x3 sub-boxes

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue  # Skip empty cells

                # Validate digit
                if val not in {'1','2','3','4','5','6','7','8','9'}:
                    return False

                # Check row
                if val in rows[r]:
                    return False
                rows[r].add(val)

                # Check column
                if val in cols[c]:
                    return False
                cols[c].add(val)

                # Check 3x3 box
                box_index = (r // 3) * 3 + (c // 3)
                if val in boxes[box_index]:
                    return False
                boxes[box_index].add(val)

        return True


# Example usage
if __name__ == "__main__":
    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    sol = Solution()
    print(sol.isValidSudoku(board))  # Output: True
