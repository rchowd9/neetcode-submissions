from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        Returns a list of the maximum values in each sliding window of size k.
        
        Args:
            nums (List[int]): The input list of integers.
            k (int): The size of the sliding window.
        
        Returns:
            List[int]: List of maximums for each window.
        """
        # Input validation
        if not isinstance(nums, list) or not all(isinstance(x, int) for x in nums):
            raise ValueError("nums must be a list of integers.")
        if not isinstance(k, int) or k <= 0:
            raise ValueError("k must be a positive integer.")
        if k > len(nums):
            raise ValueError("k cannot be larger than the length of nums.")

        dq = deque()  # Will store indices of elements in decreasing order
        result = []

        for i, num in enumerate(nums):
            # Remove indices that are out of the current window
            while dq and dq[0] <= i - k:
                dq.popleft()

            # Remove indices whose corresponding values are less than current num
            while dq and nums[dq[-1]] < num:
                dq.pop()

            dq.append(i)

            # Append the max for the current window
            if i >= k - 1:
                result.append(nums[dq[0]])

        return result


# Example usage
if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(sol.maxSlidingWindow(nums, k))  # Output: [3, 3, 5, 5, 6, 7]
