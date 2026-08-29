# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        res = []

        if root:
            queue.append(root)
            res.append([root.val])
        while len(queue) > 0:
            level = []
            for i in range(len(queue)):
                curr = queue.popleft()

                if curr.left:
                    queue.append(curr.left)
                    level.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    level.append(curr.right.val)
            if level:
                res.append(level)

        return res         

            