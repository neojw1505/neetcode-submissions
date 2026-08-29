"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)

        # pointers for starts and ends
        s,e = 0,0 

        maxCount, count = 0,0
        # iterate through all start time, once no more start time can stop 
        while s < len(intervals):
            if starts[s] < ends[e]:
                count += 1
                s += 1
                maxCount = max(maxCount, count)
            else:
                count -= 1
                e += 1
        return maxCount