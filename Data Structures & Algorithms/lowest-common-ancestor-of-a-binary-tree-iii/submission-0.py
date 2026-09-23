"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_start = p 
        q_start = q

        while p != q:
            p = p.parent
            q = q.parent 

            if not p:
                p = q_start
            if not q:
                q = p_start
        return p