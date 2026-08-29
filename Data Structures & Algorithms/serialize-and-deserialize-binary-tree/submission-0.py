# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node: # ✅ node, not root
                res.append("N")
                return # ✅ need return
            res.append(str(node.val))
            dfs(node.left) # ✅ recurse left
            dfs(node.right) # ✅ recurse right
        dfs(root)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0
        def dfs():
            if vals[self.i] == "N": # ✅ check for "N"
                self.i += 1
                return None
            node = TreeNode(vals[self.i])  # ✅ convert to int
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
            