class Solution:
    def rob(self, nums: List[int]) -> int:
        # take note edge case if 1 hse slicing wont work
        if len(nums) == 1:
            return nums[0]

        def helper(houses):
            prev2 = 0
            prev1 = houses[0]
            for i in range(1, len(houses)):
                best = max(prev2 + houses[i], prev1)
                prev2 = prev1
                prev1 = best
            return prev1
        
        return max(helper(nums[1:]), helper(nums[:len(nums)-1]))

# T:O(n) S:O(1)