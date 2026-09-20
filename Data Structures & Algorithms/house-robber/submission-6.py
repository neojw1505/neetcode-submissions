class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0
        prev1 = nums[0]

        for num in nums:
            best = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = best
        return prev1 