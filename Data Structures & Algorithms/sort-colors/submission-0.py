class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]
        for color in nums:
            counts[color] += 1
        
        i = 0
        while i < len(nums):
            for _ in range(counts[0]):
                nums[i] = 0
                i += 1
            for _ in range(counts[1]):
                nums[i] = 1
                i += 1
            for _ in range(counts[2]):
                nums[i] = 2
                i += 1
