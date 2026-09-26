class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        

        dp = [1] * (len(nums))
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0] * nums[1])

        dp_min = [1] * (len(nums))
        dp_min[0] = nums[0]
        dp_min[1] = min(nums[1], nums[0] * nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])
            dp_min[i] = min(dp[i-1] * nums[i], dp_min[i-1] * nums[i], nums[i])

        return max(dp)