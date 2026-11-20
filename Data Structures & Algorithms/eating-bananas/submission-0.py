from typing import List
import math
import bisect

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(k: int) -> bool:
            # Total hours needed at speed k
            hours = sum((pile + k - 1) // k for pile in piles)
            return hours <= h

        # Binary search for the minimum k
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            if can_eat(mid):
                right = mid
            else:
                left = mid + 1
        return left
