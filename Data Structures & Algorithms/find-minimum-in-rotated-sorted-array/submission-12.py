class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        
        while L <= R:
            m = (L + R) // 2
            
            # If mid element is greater than leftmost, 
            # minimum is in right half
            if nums[m] >= nums[L]:
                L = m + 1
            # If mid element is less than leftmost, 
            # minimum is in left half or mid itself
            else:
                R = m
        
        return nums[L]