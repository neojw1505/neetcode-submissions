# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.nodes = []
        self.ans = None
        def dfs(root):
            if not root: 
                return 
            dfs(root.left)
            self.nodes.append(root.val)
            if len(self.nodes) == k:
                self.ans = root.val
                return
            dfs(root.right)
        dfs(root)
        return self.ans


