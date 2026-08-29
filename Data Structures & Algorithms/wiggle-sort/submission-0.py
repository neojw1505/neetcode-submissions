class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(1, n):
            # odd index - should be greater than prev 
            if i % 2 == 1 and nums[i] < nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
            # even index - should be less than prev
            elif i % 2 == 0 and nums[i] > nums[i-1]:
                nums[i],nums[i-1] = nums[i-1],nums[i]
        return nums