class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums)
        last = n - 1

        while i <= last:
            if nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i] # swap
                last -= 1
            else:
                i += 1
        return i
                