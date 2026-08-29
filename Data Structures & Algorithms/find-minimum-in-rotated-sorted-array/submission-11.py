class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        
        # Remove the incorrect initial check
        
        while L < R:
            m = (L + R) // 2
            
            # If mid element is greater than rightmost, 
            # minimum is in right half
            if nums[m] > nums[R]:
                L = m + 1
            # If mid element is less than or equal to rightmost, 
            # minimum is in left half or mid itself
            else:
                R = m
        
        return nums[L]