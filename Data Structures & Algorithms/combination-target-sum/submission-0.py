class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, path = [], []
        n = len(nums)
        def backtrack(start, cur_sum):
            # base case
            if cur_sum == target:
                res.append(path[:])
                return
            if cur_sum > target:
                return
            # recurse
            for i in range(start, n):
                path.append(nums[i])
                backtrack(i, cur_sum + nums[i])
                path.pop()
        backtrack(0,0)
        return res