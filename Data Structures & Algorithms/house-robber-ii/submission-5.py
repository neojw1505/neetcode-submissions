class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        if n == 1: return nums[0] 
        if n == 2: return max(nums[0],nums[1])

        def rob_house(nums):
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(dp[0],nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            return dp[-1]
        
        return max(rob_house(nums[1:]), rob_house(nums[:len(nums)-1]))
