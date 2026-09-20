# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root or not root.left or not root.right:
            return

        if root.left.val < root.val and root.right.val > root.val:
            return True
        return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)
        

