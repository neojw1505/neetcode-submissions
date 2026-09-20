class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        path = []
        
        def dfs(start_index, curr_sum): # add curr_sum because need track 
            # base case
            if curr_sum == target:
                res.append(path[:])
                return
            # overshot target also msut return
            if curr_sum > target:
                return
            
            # multiple choices: forward only, can pick same number again, but cannot go back index
            for i in range(start_index, len(nums)):
                path.append(nums[i]) # select choice
                curr_sum += nums[i] # select choice
                dfs(i,curr_sum) # pass i because can select same num again? 
                path.pop() # undo choice
                curr_sum -= nums[i] # undo choice
        dfs(0,0)
        return res