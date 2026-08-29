class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Time Complexity: O(n * 2^n)

        res = []
        subset = []

        def dfs(i):
            # check out of bound
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i+1)

            # decision to NOT include nums[i]
            subset.pop()
            dfs(i+1)
        
        dfs(0)
        return res