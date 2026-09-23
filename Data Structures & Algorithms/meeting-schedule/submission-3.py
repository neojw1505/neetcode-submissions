"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)

        prev_start, prev_end = intervals[0].start, intervals[0].end
        
        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i].start, intervals[i].end
            # overlap
            if prev_end > curr_start:
                return False
            # no overlap
            else:
                prev_end = curr_end 
        
        return True
