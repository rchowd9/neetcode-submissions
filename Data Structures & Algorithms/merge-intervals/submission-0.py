from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If no intervals yet or no overlap with the last merged interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap: extend the last interval's end if needed
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
        
        return merged
