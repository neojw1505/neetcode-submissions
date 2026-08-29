class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        ones = 0
        twos = 0
        for num in nums:
            if num == 0: zeroes += 1
            if num == 1: ones += 1
            if num == 2: twos += 1
        i = 0
        for _ in range(zeroes):
            nums[i] = 0
            i += 1
        for _ in range(ones):
            nums[i] = 1
            i += 1
        for _ in range(twos):
            nums[i] = 2
            i += 1
        