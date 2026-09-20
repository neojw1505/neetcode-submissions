class Solution:
    def findMin(self, nums: List[int]) -> int:
        L,R = 0, len(nums)-1
        res = nums[0]
        # rotated n times, as if no rotation
        if nums[0] < nums[len(nums)-1]:
            return nums[0]

        # from here array is rotated with pivot
        while L <= R:
            m = (L + R) // 2
            # currNum in left half, find in right half
            if nums[m] >= nums[L]:
                L = m + 1
            # currNum in right half, minNum in right half
            else:
                R = m - 1
        
        return res