from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to minimize binary search space
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2
        
        left, right = 0, m
        
        while left <= right:
            # Partition nums1
            i = (left + right) // 2
            # Partition nums2 based on nums1's partition
            j = half - i
            
            # Handle boundaries
            nums1_left = nums1[i - 1] if i > 0 else float('-inf')
            nums1_right = nums1[i] if i < m else float('inf')
            nums2_left = nums2[j - 1] if j > 0 else float('-inf')
            nums2_right = nums2[j] if j < n else float('inf')
            
            # Check if correct partition
            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # Found correct partition
                if total % 2 == 0:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
                else:
                    return min(nums1_right, nums2_right)
            elif nums1_left > nums2_right:
                # Move partition left
                right = i - 1
            else:
                # Move partition right
                left = i + 1
        
        # Should never reach here if inputs are valid
        raise ValueError("Input arrays are not sorted or invalid.")

# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays([1, 3], [2]))       # Output: 2.0
    print(sol.findMedianSortedArrays([1, 2], [3, 4]))    # Output: 2.5
