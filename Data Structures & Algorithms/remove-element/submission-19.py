class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        last = n - 1
        i = 0
        while i <= last:
            while last >= 0 and nums[i] == val:
                nums[i], nums[last] = nums[last], nums[i] # swap
                last -= 1 
            i += 1
        return last + 1

    
    # [1], val = 1
    #    i
    # l