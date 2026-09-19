# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialise(root):
            if not root:
                return "#X"
            left = serialise(root.left)
            right = serialise(root.right)
            return "#" + str(root.val) + left + right 
        
        root_str = serialise(root)
        subRoot_str = serialise(subRoot)
        return subRoot_str in root_str