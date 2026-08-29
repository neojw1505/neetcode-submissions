class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        while L < R:
            m = (L + R) // 2            

            if nums[m] > nums[R]:
                L = m + 1
            else:
                R = m
        
        # Add boundary check before returning
        return nums[L]