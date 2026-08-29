class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        cur_min = arrays[0][0]
        cur_max = arrays[0][-1]
        res = 0
        for i in range(1, len(arrays)):
            res = max(res, cur_max - arrays[i][0], arrays[i][-1] - cur_min)
            cur_min = min(arrays[i][0], cur_min)
            cur_max = max(arrays[i][-1], cur_max)
        return res
