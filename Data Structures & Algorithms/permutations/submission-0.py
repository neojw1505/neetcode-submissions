class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans, sol = [], []

        def backtrack():
            if len(nums) == len(sol):
                ans.append(sol[:])
                return
            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        backtrack()
        return ans                 