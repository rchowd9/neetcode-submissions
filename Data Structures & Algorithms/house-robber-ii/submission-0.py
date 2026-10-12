class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Rob houses arranged in a circle where you cannot rob adjacent houses.
        Since first and last houses are adjacent, we consider two scenarios:
        1. Rob houses from index 1 to n-1 (exclude first house)
        2. Rob houses from index 0 to n-2 (exclude last house)
        Return the maximum of these two scenarios.
        """
      
        def rob_linear(houses: List[int]) -> int:
            """
            Helper function to rob houses in a linear arrangement.
            Uses dynamic programming with two variables to track:
            - rob_current: max money if we rob the current house
            - skip_current: max money if we skip the current house
            """
            skip_current = 0  # Max money when skipping current house
            rob_current = 0   # Max money when robbing current house
          
            for house_value in houses:
                # Calculate new states
                # If we skip this house, we take max of previous skip/rob
                # If we rob this house, we must have skipped the previous one
                skip_current, rob_current = max(skip_current, rob_current), skip_current + house_value
          
            # Return the maximum money we can rob
            return max(skip_current, rob_current)
      
        # Edge case: single house
        if len(nums) == 1:
            return nums[0]
      
        # Compare two scenarios: exclude first house vs exclude last house
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))
