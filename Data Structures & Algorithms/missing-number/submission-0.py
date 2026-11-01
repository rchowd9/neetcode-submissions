from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n  # start with the expected number of elements
        for i, num in enumerate(nums):
            ans ^= i ^ num  # XOR index, number, and result
        return ans
