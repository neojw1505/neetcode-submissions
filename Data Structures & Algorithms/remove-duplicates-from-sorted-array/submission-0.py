class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0
        for i in range(n):
            if nums[i] != nums[i-1]: # found a new element
                nums[j] = nums[i]
                j += 1
        return j

