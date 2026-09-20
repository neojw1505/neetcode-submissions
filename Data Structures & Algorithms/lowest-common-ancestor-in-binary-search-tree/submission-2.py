# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curr = root

        while curr:
            # BST properties: both greater than root, means right sub tree
            if p.val > root.val and q.val > root.val:
                curr = curr.right
            # BST properties: both lesser than root, means left sub tree
            elif p.val < root.val and q.val < root.val:
                curr = curr.left
            # curr node = p or q, or p and q split
            else:
                return curr
                

