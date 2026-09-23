class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        
        prev_start, prev_end = intervals[0][0], intervals[0][1]
        del_count = 0

        for i in range(1, len(intervals)):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if prev_end > curr_start:
                del_count += 1
                prev_end = min(prev_end, curr_end)
            else: 
                prev_end = curr_end 

        return prev_end


