class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0] * nums[1], nums[1])
        cur_min = min(dp[0] * nums[1], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i-1] * nums[i], nums[i], cur_min * nums[i])
            cur_min = min(dp[i-1] * nums[i], nums[i], cur_min * nums[i])
        return max(dp)