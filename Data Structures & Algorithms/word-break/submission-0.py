from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determines if the string `s` can be segmented into a sequence of one or more words from `wordDict`.
        
        Args:
            s (str): The input string.
            wordDict (List[str]): List of valid words.
        
        Returns:
            bool: True if segmentation is possible, False otherwise.
        """
        if not isinstance(s, str) or not isinstance(wordDict, list):
            raise ValueError("Invalid input: s must be a string and wordDict must be a list of strings.")
        
        # Convert wordDict to a set for O(1) lookups
        word_set = set(wordDict)
        
        # dp[i] will be True if s[:i] can be segmented into words from wordDict
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string can always be segmented
        
        for i in range(1, len(s) + 1):
            for j in range(i):
                # If s[:j] is segmentable and s[j:i] is a word, mark dp[i] as True
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # No need to check further for this i
        
        return dp[len(s)]


# Example usage
if __name__ == "__main__":
    solution = Solution()
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(solution.wordBreak(s, wordDict))  # Output: True

    s2 = "catsandog"
    wordDict2 = ["cats", "dog", "sand", "and", "cat"]
    print(solution.wordBreak(s2, wordDict2))  # Output: False
