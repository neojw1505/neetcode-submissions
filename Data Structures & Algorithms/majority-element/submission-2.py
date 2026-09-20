class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        candidate = None
        count = 0
      
        for num in nums:
            if count == 0:
                candidate = num
            if num != candidate: 
                count -= 1
                candidate = num
            else:
                count += 1
                candidate = num
        return candidate




