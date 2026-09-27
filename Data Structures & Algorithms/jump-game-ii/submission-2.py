class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        n = len(nums)
        farthest = 0
        curr_window_end = 0

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == curr_window_end:
                curr_window_end = farthest
                jumps += 1
        return jumps