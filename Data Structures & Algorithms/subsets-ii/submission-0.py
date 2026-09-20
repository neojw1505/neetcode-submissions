class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()
        
        def dfs(i):
            # base case
            if i == len(nums):
                res.append(path[:])
                return
            
            # choices rules:
            #  - no duplicates subsets, but a path can have duplicate number 
            #  - can only choose number once -> need start_index passed in for loop
            #  - only 2 choices, pick or don't pick
            
            # pick
            path.append(nums[i])
            dfs(i+1)
            path.pop()
            
            # don't pick
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            dfs(i+1)
        
        dfs(0)
        return res
