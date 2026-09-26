class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0] * nums[1])
        cur_min = nums[1]

        for i in range(2, n):
            dp[i] = max(nums[i], dp[i-1] * nums[i], cur_min * nums[i])
            cur_min = min(nums[i], cur_min * nums[i], dp[i-1] * nums[i])
        return max(dp)