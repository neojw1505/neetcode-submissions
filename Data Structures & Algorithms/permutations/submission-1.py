class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        n = len(nums)
        def backtrack(start):
            # base
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            # recurse
            for i in range(n):
                if nums[i] not in sol:
                    sol.append(nums[i])
                    backtrack(i)
                    sol.pop()
        backtrack(0)
        return res