class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []
        nums.sort()
        used_indices = set()
        def dfs():
            # base
            if len(sol) == len(nums):
                res.append(sol[:])
                return

            # for choice in choices
            for i in range(len(nums)):
                if i in used_indices: continue
                if i > 0 and nums[i] == nums[i-1] and (i-1) not in used_indices: continue
                
                used_indices.add(i)
                sol.append(nums[i])
                dfs()
                sol.pop()
                used_indices.remove(i)

        dfs()
        return res 

    # sol = [1, 1]
    # res = [[1,1,2]]

