class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        if n == 0:
            return 0
        def dp(i):
            if i == 0:
                memo[0] = nums[0]
                return memo[0]
            if i == 1:
                memo[1] = max(nums[0], nums[1])
                return memo[1]
            if i in memo:
                return memo[i]
            memo[i] = max(nums[i] + dp(i-2), dp(i-1))
            return memo[i]
        return dp(n-1)        