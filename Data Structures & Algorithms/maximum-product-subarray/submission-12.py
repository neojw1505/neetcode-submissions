class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        cur_min = nums[0] # minimum found so far
        cur_max = nums[0] # maximum found so far
        global_max = nums[0] 

        for i in range(1, n):
            tmp = cur_min
            cur_min = min(nums[i], cur_max * nums[i], tmp * nums[i])
            cur_max = max(nums[i], cur_max * nums[i], tmp * nums[i])
            global_max = max(cur_max, global_max)
        return global_max