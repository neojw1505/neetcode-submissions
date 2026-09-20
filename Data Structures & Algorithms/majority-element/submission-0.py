class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        candidate = nums[0]
        count = 0
      
        for num in nums:
            if num != candidate: 
                count -= 1
                candidate = num
            else:
                count += 1
                candidate = num
        return candidate




