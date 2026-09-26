class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        n = len(nums)
        curSum = nums[0]
        maxSum = nums[0]
        for i in range(1, n):
            if curSum > 0:
                curSum += nums[i]
            else:
                curSum = nums[i]
            
            if curSum > maxSum:
                maxSum = curSum

        return maxSum