# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left - root - right
    
        stack, res = [], [] 
        curr = root
        # stack: []
        # res: [4, 2, 5, 1, ]
        # curr: 3
        # 
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left 
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right 
        return res 
            



            
        


