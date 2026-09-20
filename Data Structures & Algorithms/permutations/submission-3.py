class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        seen = set() # to track the current path numbers

        def dfs(seen):
            # base case
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            # choices rules
            # - number cannot choose itself again, must choose other number -> 1 can only choose 2,3
            #   - use a seen set to check at O(1) time if the number used, if yes, skip. 
            for i in range(len(nums)):
                if nums[i] in seen:
                    continue

                path.append(nums[i]) # select choice
                seen.add(nums[i]) # add to seen set
                dfs(seen) # recurse down with updated seen
                path.pop() # undo
                seen.remove(nums[i]) # undo
        dfs(seen)
        return res