class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        running_count = 1
        for i in range(n):
            res[i] = running_count
            running_count *= nums[i]
        
        running_count = 1
        for i in range(n-1, -1, -1):
            res[i] *= running_count
            running_count *= nums[i]
        
        return res