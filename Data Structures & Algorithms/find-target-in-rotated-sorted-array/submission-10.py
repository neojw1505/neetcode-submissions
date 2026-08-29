class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:  # ✓ Include when l == r
            m = (l + r) // 2
            
            if nums[m] == target:
                return m
            
            # Check which half is sorted
            if nums[l] <= nums[m]:  # Left half is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1  # Target in sorted left
                else:
                    l = m + 1  # Target in right
            else:  # Right half is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1  # Target in sorted right
                else:
                    r = m - 1  # Target in left
        
        return -1