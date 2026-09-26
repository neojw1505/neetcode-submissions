class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        n = len(nums)
        global_max = nums[0]
        cur_max = nums[0] 
        cur_min = nums[0]
     
        for i in range(1, n):
            tmp_max = cur_max 
            cur_max = max(cur_min*nums[i], tmp_max * nums[i], nums[i])
            cur_min = min(cur_min*nums[i], tmp_max * nums[i], nums[i])
            global_max = max(global_max, cur_max)

        return global_max
