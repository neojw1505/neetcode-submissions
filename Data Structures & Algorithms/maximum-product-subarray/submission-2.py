class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # 1 ele, product = that 1 ele
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0]*nums[1], nums[1])

        dp_min = [0] * len(nums)
        dp_min[0] = nums[0]
        dp_min[1] = min(nums[0]*nums[1], nums[1])

        n = len(nums)
        for i in range(2, n):
            dp[i] = max(dp[i-1] * nums[i], nums[i], dp_min[i-1] * nums[i])
        return max(dp)

    # 2,4,-3,5
    # dp = [2,8,-3,5]
    # i = 2
    # nums[i] = 5
    # dp[i-1] = -3
    # dp[3] = 5



