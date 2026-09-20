class Solution:
    def findMin(self, nums: List[int]) -> int:
        L, R = 0, len(nums) - 1
        # already sorted without rotations
        if nums[0] <= nums[len(nums)-1]:
            return nums[0]

        while L <= R:
            m = (L + R) // 2            

            # If mid element is greater than leftmost, 
            # minimum is in right half
            if nums[m] >= nums[L]:
                L = m + 1
            # If mid element is less than leftmost, 
            # minimum is in left half or mid itself
            else:
                R = m - 1
        
        # Add boundary check before returning
        return nums[L]