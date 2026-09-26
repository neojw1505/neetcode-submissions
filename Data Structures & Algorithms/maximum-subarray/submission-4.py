class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curSum = nums[0]
        maxSum = nums[0]
        n = len(nums)

        for i in range(1, n):
            curSum = max(0, curSum + nums[i])
            maxSum = max(maxSum, curSum)
        return maxSum