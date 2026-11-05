from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        result = []

        while top <= bottom and left <= right:
            # Traverse top row → left to right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Traverse right column → top to bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Traverse bottom row → right to left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Traverse left column → bottom to top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
