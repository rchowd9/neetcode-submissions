from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        Determines if you can reach the last index starting from the first index.
        
        Args:
            nums (List[int]): List of non-negative integers representing max jump lengths.
        
        Returns:
            bool: True if the last index is reachable, False otherwise.
        """
        # Edge case: empty list or single element
        if not nums or len(nums) == 1:
            return True
        
        max_reach = 0  # The farthest index we can reach
        
        for i, jump in enumerate(nums):
            # If current index is beyond max reachable point, we can't proceed
            if i > max_reach:
                return False
            
            # Update the farthest reachable index
            max_reach = max(max_reach, i + jump)
            
            # Early exit if we can already reach or pass the last index
            if max_reach >= len(nums) - 1:
                return True
        
        return False


# Example usage and testing
if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([2, 3, 1, 1, 4], True),  # Can reach last index
        ([3, 2, 1, 0, 4], False), # Stuck at index 3
        ([0], True),              # Already at last index
        ([1, 0, 1, 0], False)     # Can't reach last index
    ]
    
    for nums, expected in test_cases:
        result = sol.canJump(nums)
        print(f"nums={nums} -> {result} (expected: {expected})")
