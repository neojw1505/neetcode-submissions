# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Time Complexity: O(p + q)
        
        # empty tree are equal
        if not p and not q:
            return True

        # 1 tree empty 1 not or compare value not equal
        if not p or not q or p.val != q.val:
            return False
        
        # if above 2 cases not triggered, means node equal
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) 
