# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        def dfs(root, max_seen_so_far):
            if not root:
                return 0
            if root.val >= max_seen_so_far:
                self.count += 1
            left = dfs(root.left, max(max_seen_so_far, root.val))
            right = dfs(root.right, max(max_seen_so_far, root.val))

        dfs(root,root.val)
        return self.count