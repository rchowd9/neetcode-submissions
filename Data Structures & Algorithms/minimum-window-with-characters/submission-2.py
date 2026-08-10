from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(t) > len(s):
            return ""

        target_count = Counter(t)
        required = len(target_count)

        left = 0
        formed = 0
        window_count = defaultdict(int)
        min_len = float("inf")
        min_window_bounds = (0, 0)

        for right, char in enumerate(s):
            window_count[char] += 1

            if char in target_count and window_count[char] == target_count[char]:
                formed += 1

            while left <= right and formed == required:
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    min_window_bounds = (left, right)

                left_char = s[left]
                window_count[left_char] -= 1

                if left_char in target_count and window_count[left_char] < target_count[left_char]:
                    formed -= 1

                left += 1

        if min_len == float("inf"):
            return ""

        l, r = min_window_bounds
        return s[l:r+1]

        