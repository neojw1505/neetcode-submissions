class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort(key=lambda x:x[0])
        start_1, end_1 = intervals[0][0], intervals[0][1]
        res = [[start_1, end_1]]
        
        for start, end in intervals[1:]:
            if res[-1][1] >= start: #. merge
                res[-1][1] = max(res[-1][1], end)
            else: # dont merge
                res.append([start, end])
        
        return res


            
