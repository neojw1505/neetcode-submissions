# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # main tree and subTree both empty
        if not root and not subRoot:
            return True
        # main tree empty, subTree not empty
        if not root:
            return False
        if root.val == subRoot.val:
            if self.sameTree(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def sameTree(self, root1, root2):
        # both empty
        if not root1 and not root2:
            return True
        # one of them empty
        if not root1 or not root2:
            return False
        # mismatch val
        if root1.val != root2.val:
            return False
        
        left = self.sameTree(root1.left, root2.left)
        right = self.sameTree(root1.right, root2.right)

        return left and right