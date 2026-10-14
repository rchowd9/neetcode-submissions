class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Count the number of palindromic substrings in the given string.
        
        Args:
            s (str): Input string.
        
        Returns:
            int: Total count of palindromic substrings.
        """
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")
        
        n = len(s)
        count = 0
        
        # Helper function to expand around center and count palindromes
        def expand_from_center(left: int, right: int) -> int:
            local_count = 0
            while left >= 0 and right < n and s[left] == s[right]:
                local_count += 1
                left -= 1
                right += 1
            return local_count
        
        # Each character and gap between characters is a center
        for center in range(2 * n - 1):
            left = center // 2
            right = left + (center % 2)
            count += expand_from_center(left, right)
        
        return count


# Example usage
if __name__ == "__main__":
    sol = Solution()
    test_str = "aaa"
    print(f"Number of palindromic substrings in '{test_str}': {sol.countSubstrings(test_str)}")

        