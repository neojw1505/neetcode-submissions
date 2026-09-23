"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x:x.start)
        min_heap = [intervals[0].end]
        rooms = 1

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i].start, intervals[i].end
            if curr_start < min_heap[0]: # overlap 
                rooms += 1
                heapq.heappush(min_heap, curr_end)
            else: # no overlap 
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, curr_end)
        return rooms