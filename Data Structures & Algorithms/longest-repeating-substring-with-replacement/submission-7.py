class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring that can be obtained by replacing
        at most k characters so that all characters in the substring are the same.

        :param s: Input string (uppercase English letters)
        :param k: Maximum number of allowed replacements
        :return: Length of the longest valid substring
        """
        count = {}       # Dictionary to store frequency of characters in the current window
        max_len = 0      # Result: maximum length found
        max_count = 0    # Count of the most frequent character in the current window
        left = 0         # Left pointer for sliding window

        for right in range(len(s)):
            # Add current character to the count dictionary
            count[s[right]] = count.get(s[right], 0) + 1

            # Track the highest frequency of any single character in the window
            max_count = max(max_count, count[s[right]])

            # If replacements needed exceed k, shrink the window from the left
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            # Update maximum length found
            max_len = max(max_len, right - left + 1)

        return max_len
