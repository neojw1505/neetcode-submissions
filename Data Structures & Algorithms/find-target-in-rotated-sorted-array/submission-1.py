class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums) - 1

        while L <= R:
            m = (L + R) // 2

            if nums[m] == target:
                return m

            # in the left sorted 
            if nums[m] >= nums[R]:
                # check target inside here 
                if target > nums[m]:
                    # target must be on the right of mid
                    L = m + 1
                else:
                    # target smaller than middle value, 
                    # can be left of middle or right
                    # to determine search left or right side of middle
                    # check the right corner, if bigger than right corner 
                    # means must be in the left
                    if target > nums[R]:
                        R = m - 1
                    # target is within the right side 
                    else:
                        L = m + 1 
            # in the right sorted
            # mid value is somewhere in right sorted region
            # because all numbers to left of mid are smaller
            elif nums[m] < nums[R]:
                if target > nums[m]:
                    L = m + 1
                else:
                    R = m - 1
        return -1


