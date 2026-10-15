class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Given a string s containing only digits, return the number of ways to decode it.
        'A' -> 1, 'B' -> 2, ..., 'Z' -> 26
        """
        # Edge case: empty string
        if not s:
            return 0
        
        n = len(s)
        
        # dp[i] = number of ways to decode up to index i-1
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty string has 1 way to decode
        
        # First character check
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, n + 1):
            # Single digit decode (last digit not '0')
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            # Two digit decode (10 to 26)
            two_digit = int(s[i - 2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]
        
        return dp[n]


# Example usage:
if __name__ == "__main__":
    sol = Solution()
    print(sol.numDecodings("12"))   # Output: 2 ("AB", "L")
    print(sol.numDecodings("226"))  # Output: 3 ("BZ", "VF", "BBF")
    print(sol.numDecodings("06"))   # Output: 0 (invalid)

        