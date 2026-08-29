class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        n = len(intervals)
        start,end = newInterval
        res = []
        # no overlap, current interval ends before newInterval start
        while i < n and intervals[i][1] < start:
            res.append(intervals[i])
            i += 1
        # overlap, current interval starts before newInterval ends
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        res.append([start,end])
        # no overlap, current interval start after newInterval ends
        while i < n and intervals[i][0] > end:
            res.append(intervals[i])
            i += 1
        return res
