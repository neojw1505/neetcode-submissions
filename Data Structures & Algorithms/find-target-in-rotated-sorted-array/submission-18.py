class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l < r:
            m = (l+r)//2
            # condition 1: target is in left sub-array
            if target > nums[r]:
                # if m in right sub-array, throw away as not possible
                if nums[m] <= nums[r]:
                    r = m - 1
                # if m in left sub-array, possible as target also in left sub-array
                else:
                    if nums[m] == target:
                        return m
                    elif nums[m] < target:
                        l = m + 1
                    else:
                        r = m - 1
            # condition 2: target is in right sub-array
            elif target <= nums[r]:
                # if m in left sub-array, throw away as not possible
                if nums[m] > nums[r]:
                    l = m + 1
                # if m in right sub-array, possible as target is also in right sub-array
                else:
                    if nums[m] == target:
                        return m
                    elif nums[m] < target:
                        l = m + 1
                    else:
                        r = m - 1 
        return r if nums[r] == target else -1
            



