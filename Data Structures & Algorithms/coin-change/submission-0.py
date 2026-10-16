from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Returns the fewest number of coins needed to make up the given amount.
        If it's not possible, returns -1.
        """
        # Validate inputs
        if not isinstance(coins, list) or not all(isinstance(c, int) and c > 0 for c in coins):
            raise ValueError("Coins must be a list of positive integers.")
        if not isinstance(amount, int) or amount < 0:
            raise ValueError("Amount must be a non-negative integer.")

        # DP array: dp[i] = minimum coins needed for amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed for amount 0

        # Build up the dp array
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        # If dp[amount] is still infinity, no solution exists
        return dp[amount] if dp[amount] != float('inf') else -1


# Example usage
if __name__ == "__main__":
    solution = Solution()
    try:
        coins = [1, 2, 5]
        amount = 11
        result = solution.coinChange(coins, amount)
        print(f"Minimum coins needed: {result}")  # Expected output: 3 (5+5+1)
    except ValueError as e:
        print(f"Input error: {e}")

        