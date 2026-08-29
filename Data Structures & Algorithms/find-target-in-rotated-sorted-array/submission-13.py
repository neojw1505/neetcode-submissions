class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # left sorted half from [l:m]
            if nums[l] <= nums[m]:
                # check target within [l:m]
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # currNum in right sorted half
            else:
                # check target within [m:r]
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
