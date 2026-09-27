class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        farthest = 0 
        jumps = 0
        curr_window_end = 0
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == curr_window_end:
                jumps += 1
                curr_window_end = farthest
        return jumps 
