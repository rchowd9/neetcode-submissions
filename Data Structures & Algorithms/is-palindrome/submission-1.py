class Solution:
    def isPalindrome(self, s: str) -> bool:
        filter_char = [char.lower() for char in s if char.isalnum()]

        return filter_char == filter_char[::-1]
        