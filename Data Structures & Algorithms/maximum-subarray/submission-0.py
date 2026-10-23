class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')  # global maximum sum
        curr_sum = 0            # current subarray sum

        for num in nums:
            # Either extend the current subarray or start fresh with num
            curr_sum = max(num, curr_sum + num)
            # Update global maximum
            max_sum = max(curr_sum, max_sum)

        return max_sum
