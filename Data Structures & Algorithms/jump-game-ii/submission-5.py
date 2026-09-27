class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        curr_window_end = 0
        farthest = 0

        for i in range(n-1):
            farthest = max(farthest, i + nums[i])

            if i == curr_window_end:
                curr_window_end = farthest
                jumps += 1
        
        return jumps 

    # curr_window_end = 5
    # farthest = 5
    # jumps = 2
    # i = 3