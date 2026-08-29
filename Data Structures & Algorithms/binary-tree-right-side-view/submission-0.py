# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        res = []
        
        if root:
            queue.append(root)

        while queue:
            rightSide = None
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr:
                    rightSide = curr
                    queue.append(curr.left)
                    queue.append(curr.right)
            
            if rightSide:
                res.append(rightSide.val)

        return res

