from typing import List

# Definition of Interval
class Interval:
    def __init__(self, start: int, end: int):
        if not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Start and end times must be integers.")
        if start > end:
            raise ValueError("Start time cannot be greater than end time.")
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        Determines if a person can attend all meetings without overlaps.
        :param intervals: List of Interval objects
        :return: True if no meetings overlap, False otherwise
        """
        if not isinstance(intervals, list):
            raise ValueError("Intervals must be provided as a list.")

        # Sort intervals by start time
        intervals.sort(key=lambda x: x.start)

        # Check for overlaps
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False  # Overlap detected
        return True

# Example usage
if __name__ == "__main__":
    meetings = [
        Interval(0, 30),
        Interval(5, 10),
        Interval(15, 20)
    ]
    sol = Solution()
    result = sol.canAttendMeetings(meetings)
    print("Can attend all meetings:", result)  # Expected output: False

    meetings2 = [
        Interval(7, 10),
        Interval(12, 15)
    ]
    print("Can attend all meetings:", sol.canAttendMeetings(meetings2))  # Expected output: True

