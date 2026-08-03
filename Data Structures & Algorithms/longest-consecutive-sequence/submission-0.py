class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in numSet:
            if (n - 1) not in numSet:
                len = 1
                while (n + len) in numSet:
                    len += 1
                longest = max(len, longest)

        return longest
        