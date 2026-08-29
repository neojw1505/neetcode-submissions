class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # reverse greedy approach
        n = len(nums)
        target = n - 1
        for i in range(n-2, -1, -1):
            if i + nums[i] >= target:
                target = i 
        return target == 0

        # T:O(n) S:O(1)
