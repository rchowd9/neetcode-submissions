from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Returns the maximum amount of money that can be robbed without robbing two adjacent houses.
        
        :param nums: List[int] - non-negative integers representing money in each house
        :return: int - maximum money that can be robbed
        """
        # Validate input
        if not isinstance(nums, list) or not all(isinstance(x, int) and x >= 0 for x in nums):
            raise ValueError("nums must be a list of non-negative integers")

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]

        # dp[i] will store the max money that can be robbed up to house i
        prev2 = nums[0]  # dp[i-2]
        prev1 = max(nums[0], nums[1])  # dp[i-1]

        for i in range(2, n):
            # Either rob this house (prev2 + nums[i]) or skip it (prev1)
            current = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, current

        return prev1


# Example usage
if __name__ == "__main__":
    solution = Solution()
    try:
        houses = [2, 7, 9, 3, 1]
        print("Max money robbed:", solution.rob(houses))  # Expected output: 12
    except ValueError as e:
        print("Error:", e)
