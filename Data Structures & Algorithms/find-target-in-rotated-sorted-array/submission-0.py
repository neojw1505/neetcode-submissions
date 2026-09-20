class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L,R = 0, len(nums) - 1
        
        while L <= R:
            m = (L + R) // 2
            if target == nums[m]:
                return m

            if nums[m] >= nums[R]:
                if target > nums[m]:
                    R = m - 1
                elif target < nums[m]:
                    L = m + 1
            elif nums[m] <= nums[R]:
                if target > nums[m]:
                    L = m + 1
                elif target < nums[m]:
                    R = m - 1
        return -1


