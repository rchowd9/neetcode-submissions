import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = []  # min-heap storing the k largest values
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)  # insert new value
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)    # remove smallest if too many
        return self.heap[0]            # k-th largest

