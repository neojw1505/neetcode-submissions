class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        N = len(intervals)
        res = [intervals[0]]

        for i in range(1, N):
            start2, end2 = intervals[i]
            start1, end1 = res[-1][0], res[-1][1]

            if end1 >= start2: # overlap
                if end1 > end2:
                    continue
                res[-1] = [start1, end2]
            else:
                res.append([start2, end2])
        
        return res

