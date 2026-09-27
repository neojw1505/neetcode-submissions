class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        farthest = 0
        jumps = 0
        curr_end_bound = 0
        for i in range(n-1):
            farthest = max(farthest, i + nums[i])
            if i == curr_end_bound:
                jumps += 1
                curr_end_bound = farthest
        return jumps
