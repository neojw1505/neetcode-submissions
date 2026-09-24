class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: # only 1 hse to rob
            return nums[0]
        if n == 0: # no house to rob
            return 0
        
        
        dp = [0] * n # dp[i] stands for max money robbed from ith hse

        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])
        
        return max(dp)