class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            m = (L + R) // 2
            
            if nums[m] == target:
                return m
            
            # Check which side is sorted
            if nums[L] <= nums[m]:  # Left side is sorted
                if nums[L] <= target < nums[m]:  # Target in left sorted range
                    R = m - 1
                else:  # Target in right side
                    L = m + 1
            else:  # Right side is sorted
                if nums[m] < target <= nums[R]:  # Target in right sorted range
                    L = m + 1
                else:  # Target in left side
                    R = m - 1
        
        return -1  # Target not found
