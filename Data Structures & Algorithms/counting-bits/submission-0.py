from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize result array with n+1 zeros
        ans = [0] * (n + 1)
        
        # Fill the array using the DP relation:
        # f(i) = f(i // 2) + (i & 1)
        # i // 2 shifts right by 1 bit (removes LSB)
        # i & 1 extracts the least significant bit
        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i & 1)
        
        return ans
