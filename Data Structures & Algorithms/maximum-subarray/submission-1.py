class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = nums[0]
        for n in nums:
            # 1. Add the current number to our running total
            currSum += n
            # 2. Update the absolute maximum found so far
            maxSum = max(maxSum, currSum)
            # 3. If the running total drops below 0, reset it to 0
            if currSum < 0:
                currSum = 0
        return maxSum