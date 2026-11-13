from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Finds two distinct indices in 'numbers' whose values sum to 'target'.
        
        Args:
            numbers (List[int]): List of integers.
            target (int): Target sum.
        
        Returns:
            List[int]: Indices (1-based) of the two numbers that sum to target.
        
        Raises:
            ValueError: If no valid pair exists.
        """
        # Input validation
        if not isinstance(numbers, list) or not all(isinstance(x, int) for x in numbers):
            raise TypeError("numbers must be a list of integers.")
        if not isinstance(target, int):
            raise TypeError("target must be an integer.")
        if len(numbers) < 2:
            raise ValueError("At least two numbers are required.")

        # Dictionary to store seen numbers and their indices
        seen = {}
        for i, num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                # Return 1-based indices (common in LeetCode's 'Two Sum II')
                return [seen[complement] + 1, i + 1]
            seen[num] = i

        # If no pair found
        raise ValueError("No two numbers sum to the target.")

# Example usage
if __name__ == "__main__":
    sol = Solution()
    try:
        result = sol.twoSum([2, 7, 11, 15], 9)
        print("Indices:", result)  # Output: [1, 2]
    except Exception as e:
        print("Error:", e)
