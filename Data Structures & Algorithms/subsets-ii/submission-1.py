class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        nums.sort()

        def dfs(start_index):
            res.append(path[:]) #  Every state we reach is a valid subset. Save it immediately!

            # choices rules:
            # - solution must not contain duplicate subsets -> sort and skip duplicates
            # - every choice can only be chosen once 
            for i in range(start_index, len(nums)):
                if i > start_index and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i]) # add
                dfs(i+1) # every choice can only be chosen once  -> i+1
                path.pop() # undo
        dfs(0)
        return res 



