import heapq

class MedianFinder:
    def __init__(self):
        # Max-heap for the lower half (store negatives for max-heap behavior)
        self.lower_half = []
        # Min-heap for the upper half
        self.upper_half = []

    def addNum(self, num: int) -> None:
        # Step 1: Add to max-heap (lower_half)
        heapq.heappush(self.lower_half, -num)

        # Step 2: Ensure every element in lower_half <= every element in upper_half
        if self.lower_half and self.upper_half and (-self.lower_half[0] > self.upper_half[0]):
            val = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, val)

        # Step 3: Balance sizes (difference should be at most 1)
        if len(self.lower_half) > len(self.upper_half) + 1:
            val = -heapq.heappop(self.lower_half)
            heapq.heappush(self.upper_half, val)
        elif len(self.upper_half) > len(self.lower_half):
            val = heapq.heappop(self.upper_half)
            heapq.heappush(self.lower_half, -val)

    def findMedian(self) -> float:
        # If odd number of elements, median is top of the larger heap
        if len(self.lower_half) > len(self.upper_half):
            return float(-self.lower_half[0])
        # If even, median is average of tops
        return (-self.lower_half[0] + self.upper_half[0]) / 2.0
        