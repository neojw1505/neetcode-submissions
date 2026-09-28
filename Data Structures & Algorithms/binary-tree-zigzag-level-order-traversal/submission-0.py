# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        queue = collections.deque([root])
        left_to_right = True
        while queue:
            level_size = len(queue)
            temp = []
            for _ in range(level_size):
                node = queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if left_to_right:
                res.append(temp)
            else:
                temp.reverse()
                res.append(temp)
            
            left_to_right = not left_to_right
        return res
            
                