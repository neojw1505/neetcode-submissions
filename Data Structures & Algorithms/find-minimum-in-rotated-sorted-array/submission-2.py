class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Handle single element array
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # If subarray is already sorted, leftmost is minimum
            if nums[l] < nums[r]:
                return nums[l]
            
            m = (l + r) // 2
            
            # Check if mid is the pivot point
            if m > 0 and nums[m] < nums[m-1]:
                return nums[m]
            
            # Decide which half to search
            # If mid is greater than or equal to leftmost, 
            # minimum is in right half
            if nums[m] >= nums[l]:
                l = m + 1
            # Otherwise, minimum is in left half
            else:
                r = m - 1
        
        return nums[l]