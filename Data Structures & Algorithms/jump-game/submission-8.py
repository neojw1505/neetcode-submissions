class Solution:
    def canJump(self, nums: List[int]) -> bool:
        horizon = 0
        curr_window_end = 0
        n = len(nums)

        for i in range(n-1):
            horizon = max(horizon, i + nums[i])

            if i == curr_window_end:
                curr_window_end = horizon
            if curr_window_end == n-1:
                return True

        return False

