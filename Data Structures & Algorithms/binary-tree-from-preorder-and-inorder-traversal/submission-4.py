class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # 🔍 1. Map values to their indices once for instant O(1) lookups
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        # 🧵 Set up a pointer to read preorder sequentially left-to-right
        self.pre_idx = 0
        
        def dfs(left, right):
            # 🛑 BASE CASE: If our boundary walls cross, this subtree is empty!
            if left > right:
                return None
                
            # 🛠️ Step 1: get root from preorder, always first value
            root_val = preorder[self.pre_idx]
            root = TreeNode(root_val)
            
            # Shift the pointer forward so the next node gets the next value
            self.pre_idx += 1
            
            # 🔍 Step 2: search idx of root node in inorder
            mid = inorder_map[root_val]
            
            # 🚀 Step 3: Shift the fences inward to build the children!
            # Left Subtree: lives between our current left wall and mid - 1
            root.left = dfs(left, mid - 1)
            
            # Right Subtree: lives between mid + 1 and our current right wall
            root.right = dfs(mid + 1, right)
            
            return root
            
        # Start the engine using the full boundaries of the inorder map
        return dfs(0, len(inorder) - 1)
