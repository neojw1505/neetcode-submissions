class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        def dfs(i):
            # base case
            if i == len(nums):
                res.append(path[:])
                return
            # choices: binary type -> include or exclude, forward only (no duplicates)
            
            # choice 1: include
            path.append(nums[i]) # add or push forward
            dfs(i+1) # recurse (dive deeper)
            path.pop() # pop and undo (backtracking)

            # choice 2: exclude
            dfs(i+1)# recurse (dive deeper)
        dfs(0)
        return res
