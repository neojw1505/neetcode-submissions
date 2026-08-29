class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # 2 binary search left most and right most
        l,r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        left = l
        l,r = 0, len(nums)-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        right = r
        if left <= right:
            return [left, right]
        return [-1, -1]