# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # if none just return
        if not preorder or not inorder:
            return None
        # get root node, 1st num in preorder
        root = TreeNode(preorder[0])
        # get index of the root node in preorder array
        mid = inorder.index(preorder[0])
        # build left sub tree recursively
        root.left = self.buildTree(preorder[1 : mid + 1], inorder[:mid]) 
        # build right sub tree recursively
        root.right = self.buildTree(preorder[mid+1 : ], inorder[mid + 1:])
        # return root
        return root
    
