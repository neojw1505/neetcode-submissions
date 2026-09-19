# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "#X"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return "#" + str(root.val) + left + right

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        tokens = data.split("#")[1:]
        self.i = 0
        def dfs():
            if self.i >= len(tokens):
                return None
            if tokens[self.i] == "X":
                self.i += 1
                return None
            node = TreeNode(int(tokens[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
