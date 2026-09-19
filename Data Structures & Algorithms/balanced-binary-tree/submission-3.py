# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.is_balanced = True
        def dfs(root):
            if not root:
                return 0
            if not self.is_balanced:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)

            if abs(right - left) > 1:
                self.is_balanced = False
            return 1 + max(left, right)
        dfs(root)
        return self.is_balanced
        
        


            