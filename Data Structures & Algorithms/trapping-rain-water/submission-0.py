from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Calculate the total amount of rainwater trapped given an elevation map.
        
        :param height: List[int] - non-negative integers representing elevation heights
        :return: int - total units of trapped water
        """
        # Validate input
        if not isinstance(height, list) or not all(isinstance(h, int) and h >= 0 for h in height):
            raise ValueError("Height must be a list of non-negative integers.")
        
        n = len(height)
        if n < 3:
            return 0  # Less than 3 bars can't trap water
        
        left, right = 0, n - 1
        left_max, right_max = 0, 0
        trapped_water = 0
        
        # Two-pointer approach
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    trapped_water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    trapped_water += right_max - height[right]
                right -= 1
        
        return trapped_water


# Example usage
if __name__ == "__main__":
    sol = Solution()
    example_heights = [0,1,0,2,1,0,1,3,2,1,2,1]
    print("Trapped water:", sol.trap(example_heights))  # Expected output: 6
