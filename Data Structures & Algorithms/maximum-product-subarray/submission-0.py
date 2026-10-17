from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Input validation
        if not nums or not all(isinstance(x, int) for x in nums):
            raise ValueError("nums must be a non-empty list of integers")

        # Initialize variables
        max_prod = nums[0]  # Maximum product ending here
        min_prod = nums[0]  # Minimum product ending here
        result = nums[0]    # Global maximum product

        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            current = nums[i]

            # If current number is negative, swap max_prod and min_prod
            if current < 0:
                max_prod, min_prod = min_prod, max_prod

            # Update max_prod and min_prod
            max_prod = max(current, max_prod * current)
            min_prod = min(current, min_prod * current)

            # Update global result
            result = max(result, max_prod)

        return result


# Example usage
if __name__ == "__main__":
    sol = Solution()
    try:
        nums = [2, 3, -2, 4]
        print("Maximum product subarray:", sol.maxProduct(nums))  # Output: 6

        nums = [-2, 0, -1]
        print("Maximum product subarray:", sol.maxProduct(nums))  # Output: 0

        nums = [-2, 3, -4]
        print("Maximum product subarray:", sol.maxProduct(nums))  # Output: 24
    except ValueError as e:
        print("Error:", e)

        