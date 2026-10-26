from typing import List
import math

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by their end time
        intervals.sort(key=lambda x: x[1])
        
        ans = 0
        # Track the end of the last kept interval
        currentEnd = -math.inf
        
        for start, end in intervals:
            if start >= currentEnd:
                # No overlap, keep this interval
                currentEnd = end
            else:
                # Overlap found, remove the current interval (increment count)
                ans += 1
        
        return ans
