# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        # 1. get root from preorder, always first value
        root = TreeNode(preorder[0])
        # 2. search idx of root node in inorder, to split left and right sub array
        inorder_map = {val: i for i, val in enumerate(inorder)}
        mid = inorder_map[root.val]
        # 3. slice 
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
        

