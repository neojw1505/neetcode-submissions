class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            # check if target in left half
            if target > nums[r]:
                # check if currNum is also in left half
                if nums[m] > nums[r]:
                    # check if currNum greater than target
                    if nums[m] > target:
                        r = m - 1
                    # check if currNum smaller than target
                    elif nums[m] < target:
                        l = m + 1
                # currNum is in right half
                else:
                    r = m - 1
            # check if target in right half
            else:
                # check if currNum is also in right half
                if nums[m] < nums[l]:
                    # check if currNum greater than target
                    if nums[m] > target:
                        l = m + 1
                    elif nums[m] < target:
                        r = m - 1
                # currNum is in left half
                else:
                    l = m + 1
        return -1






