import heapq
from typing import List

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        # Sort by start time
        intervals.sort(key=lambda x: x.start)

        # Min-heap to store end times
        heap = []

        for interval in intervals:
            # If heap not empty and earliest end <= current start
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap)  # Reuse room
            heapq.heappush(heap, interval.end)

        return len(heap)
