class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = maxLength = 0
        usedChar = {}

        for end in range(len(s)):
            if s[end] in usedChar and start <= usedChar[s[end]]:
                start = usedChar[s[end]] + 1
            else:
                maxLength = max(maxLength, end - start + 1)

            usedChar[s[end]] = end

        return maxLength 
        