class Solution:
    def findMin(self, nums: List[int]) -> int:  
        L, R = 0, len(nums)-1 
        minValue = float('inf') # max big number

        while L <= R:
            m = (L + R) // 2
            # compare mid value with minimum found so far
            minValue = min(minValue, nums[m]) 

            # if mid value > right corner value. 
            # e.g [4,5,6,1,2,3] m = 6, right corner = 3
            # min value must be in the range m+1 to right corner
            if nums[m] > nums[R]:
                L = m + 1
            # likewise, if mid value < right corner value
            # e.g [1,2,3,4,5,6] m = 3, right corner = 6
            # min value must be in the range left corner to m - 1
            else:
                R = m - 1
        
        return minValue