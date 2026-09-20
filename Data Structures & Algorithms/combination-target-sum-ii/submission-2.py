class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort() # must sort to put duplicates together 

        def dfs(start_index, curr_sum):
            # base case
            if curr_sum == target: # equal sum
                res.append(path[:])
                return
            if curr_sum > target: # overshot!
                return
            
            # choices rules:
            # - no duplicates, means need to check previous candidate same val, if yes need to skip
            # - chosen at most once means only can move forward -> dfs(i+1)
            for i in range(start_index, len(candidates)):
                if candidates[i] > target or (i > start_index and candidates[i] == candidates[i-1]): # impossible to sum to target
                    continue
                path.append(candidates[i]) # select
                curr_sum += candidates[i] # select
                dfs(i+1, curr_sum) # dive deeper
                path.pop()  # undo
                curr_sum -= candidates[i] # undo
        dfs(0,0)
        return res


