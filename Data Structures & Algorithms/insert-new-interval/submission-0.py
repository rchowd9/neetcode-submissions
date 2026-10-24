# time O(n) due to insertion, otherwise binary search should be considered
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        end = 0  # intervals[:end] is before newInterval and has no overlap
        start = len(intervals)  # intervals[start:] is after newInterval and has no overlap
        
        for i in range(len(intervals)):
            curr = intervals[i]
            if curr[-1] < newInterval[0]:
                end = i + 1
            elif curr[0] > newInterval[-1]:
                start = i
                break
            else:
                newInterval[0] = min(newInterval[0], curr[0])
                newInterval[-1] = max(newInterval[-1], curr[-1])
        
        return intervals[:end] + [newInterval] + intervals[start:]
        