# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Time Complexity: O(logn)
        # Space Complexity: O(1)

        cur = root

        while cur:
            # both greater than current value
            if p.val > cur.val and q.val > cur.val:
                 cur = cur.right
            # both smaller than current value
            elif p.val < cur.val and q.val < cur.val:
                 cur = cur.left
            else:
                return cur
