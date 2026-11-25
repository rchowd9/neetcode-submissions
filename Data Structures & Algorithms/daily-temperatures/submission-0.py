from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        Given a list of daily temperatures, returns a list where each element
        represents the number of days until a warmer temperature occurs.
        If no warmer day exists, the value is 0.
        """
        n = len(temperatures)
        answer = [0] * n  # Initialize result array with zeros
        stack = []  # Stack to store indices of days

        for i, temp in enumerate(temperatures):
            # While current temp is warmer than the temp at stack's top index
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = i - prev_day  # Days waited for warmer temp
            stack.append(i)  # Push current day's index

        return answer


# Example usage and testing
if __name__ == "__main__":
    sol = Solution()
    temps = [73, 74, 75, 71, 69, 72, 76, 73]
    print(sol.dailyTemperatures(temps))  # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
