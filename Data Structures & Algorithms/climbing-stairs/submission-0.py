class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Returns the number of distinct ways to climb to the top of a staircase
        with n steps, where you can climb either 1 or 2 steps at a time.
        
        Uses iterative dynamic programming for O(n) time and O(1) space.
        """
        # Input validation
        if not isinstance(n, int) or n < 0:
            raise ValueError("n must be a non-negative integer.")

        # Base cases
        if n == 0:
            return 0  # No steps to climb
        if n == 1:
            return 1  # Only one way: single step
        if n == 2:
            return 2  # Two ways: (1+1) or (2)

        # Iterative DP approach
        prev1, prev2 = 1, 2  # Ways to climb 1 and 2 stairs
        for _ in range(3, n + 1):
            current = prev1 + prev2
            prev1, prev2 = prev2, current

        return prev2