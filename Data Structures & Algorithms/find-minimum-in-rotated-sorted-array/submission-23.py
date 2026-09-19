class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l+r) // 2
            # curr ele less than right bound, potential answer
            if nums[m] < nums[r]:
                r = m
            # curr ele greater than or equal to right bound, cfm wrong
            else:
                l = m + 1
                
        return nums[l]

                
            
            
