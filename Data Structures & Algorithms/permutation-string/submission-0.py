from typing import List

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Edge case: if s1 is longer than s2, no permutation can exist
        if len(s1) > len(s2):
            return False
        
        # Frequency arrays for characters 'a' to 'z'
        s1_count = [0] * 26
        window_count = [0] * 26
        
        # Fill s1_count with frequency of each char in s1
        for ch in s1:
            s1_count[ord(ch) - ord('a')] += 1
        
        # Initialize the first window in s2
        for ch in s2[:len(s1)]:
            window_count[ord(ch) - ord('a')] += 1
        
        # If initial window matches, return True
        if window_count == s1_count:
            return True
        
        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            # Add new char to window
            window_count[ord(s2[i]) - ord('a')] += 1
            # Remove char that is no longer in window
            window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            # Check if current window matches s1_count
            if window_count == s1_count:
                return True
        
        return False


# Example usage & testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))  # True (contains "ba")
    print(sol.checkInclusion("ab", "eidboaoo"))  # False
    print(sol.checkInclusion("a", "a"))          # True
    print(sol.checkInclusion("abc", "ccccbbbbaaaa"))  # True
