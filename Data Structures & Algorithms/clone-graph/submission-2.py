"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        oldToNew = {}
        stk = [node]

        while stk:
            curr = stk.pop()
            if curr not in oldToNew:
                copy = Node(curr.val)
                oldToNew[curr] = copy
            
            for nei in curr.neighbors:
                if nei not in oldToNew:
                    stk.append(nei)
        
        for old, new in oldToNew.items():
            for oldNei in old.neighbors:
                new.neighbors.append(oldToNew[oldNei])
        
        return oldToNew[node]