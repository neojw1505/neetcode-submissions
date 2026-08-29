"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start_times = [interval.start for interval in intervals]
        end_times = [interval.end for interval in intervals]
        events = []
        for s in start_times:
            events.append((s, 1))
        for e in end_times:
            events.append((e, -1))
        events.sort(key=lambda event: (event[0],event[1]))
        max_cnt = 0
        running_cnt = 0
        for event in events:
            running_cnt += event[1]
            max_cnt = max(max_cnt, running_cnt)
        return max_cnt