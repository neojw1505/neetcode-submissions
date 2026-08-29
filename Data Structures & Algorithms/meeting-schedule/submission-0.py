"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort based on start time
        intervals.sort(key=lambda x:x.start)
        for i in range(1, len(intervals)):
            # overlap 
            if intervals[i].start < intervals[i-1].end:
                return False
        return True
