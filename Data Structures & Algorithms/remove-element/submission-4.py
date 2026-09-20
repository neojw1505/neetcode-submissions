class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        last = n - 1
        i = 0
        while i < last:
            while nums[i] == val:
                if last >= 0:
                    nums[i], nums[last] = nums[last], nums[i] # swap
                last -= 1 
            i += 1
        return i + 1