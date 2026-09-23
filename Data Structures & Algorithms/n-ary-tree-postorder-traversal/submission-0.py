"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []


        stack = [root]
        res = []

       
        while stack:

            node = stack.pop()
            res.append(node.val)

            if node.children:
                for child in node.children:
                    if child:
                        stack.append(child)
        
        return res[::-1]