class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        
        dp_max = [0] * n
        dp_max[0] = nums[0]
        dp_max[1] = max(nums[1], nums[1] * nums[0])

        dp_min = [0] * n
        dp_min[0] = nums[0]
        dp_min[1] = min(nums[1], nums[1] * nums[0])

        for i in range(2, n):
            dp_max[i] = max(nums[i], nums[i] * dp_max[i-1], nums[i] * dp_min[i-1])
            dp_min[i] = min(nums[i], nums[i] * dp_max[i-1], nums[i] * dp_min[i-1])
        return max(dp_max)


