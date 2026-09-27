class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        for r in range(1, len(nums)):
            while l < r and nums[l] != 0:
                l += 1
            if r != 0:
                nums[l], nums[r] = nums[r], nums[l]

