class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals: return []

        intervals.sort(key=lambda x: x[0])
        res = []
        i = 0

        new_start, new_end = newInterval[0], newInterval[1]

        # 1. all intervals before newInterval start
        while i < len(intervals) and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1

        # 2.  all intervals before newInterval ends
        while i < len(intervals) and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1

        # this is where interval should be
        res.append([new_start, new_end])

        # 3. all intervals after newInterval ends
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res