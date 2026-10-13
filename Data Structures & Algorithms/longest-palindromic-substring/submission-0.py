class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Returns the longest palindromic substring in s.
        Uses expand-around-center approach.
        """
        if not isinstance(s, str):
            raise TypeError("Input must be a string.")
        if len(s) <= 1:
            return s  # Single char or empty string is itself a palindrome

        start, end = 0, 0  # Track indices of longest palindrome found

        def expand_from_center(left: int, right: int) -> tuple[int, int]:
            """
            Expand around the given center and return the start and end indices
            of the palindrome found.
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # After loop, left and right are one step beyond palindrome bounds
            return left + 1, right - 1

        for i in range(len(s)):
            # Odd-length palindrome
            l1, r1 = expand_from_center(i, i)
            # Even-length palindrome
            l2, r2 = expand_from_center(i, i + 1)

            # Choose the longer palindrome
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end + 1]


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    test_str = "babad"
    print("Longest palindrome:", sol.longestPalindrome(test_str))  # Output: "bab" or "aba"
