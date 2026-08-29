class TreeNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key,val)
        if not self.root:
            self.root = newNode
            return
        
        curr = self.root
        while curr:
            if curr.key > key:
                if not curr.left:
                    curr.left = newNode
                    return
                curr = curr.left
            elif curr.key < key:
                if not curr.right:
                    curr.right = newNode
                    return
                curr = curr.right
            else:
                curr.val = val
                return 

    def get(self, key: int) -> int:
        curr = self.root
        
        if not curr:
            return -1

        while curr:
            if curr.key > key:
                curr = curr.left
            elif curr.key < key:
                curr = curr.right
            else:
                return curr.val
        
        return -1
        
    def getMin(self) -> int:
        curr = self.root

        if not curr:
            return -1
        
        while curr.left: 
            curr = curr.left

        return curr.val if curr else -1

    def getMax(self) -> int:
        curr = self.root

        if not curr:
            return -1
        
        while curr.right:
            curr = curr.right

        return curr.val if curr else -1

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
    
    # Returns the new root of the subtree after removing the key
    def removeHelper(self, curr: TreeNode, key: int) -> TreeNode:
        if curr == None:
            return None

        if key > curr.key:
            curr.right = self.removeHelper(curr.right, key)
        elif key < curr.key:
            curr.left = self.removeHelper(curr.left, key)
        else:
            if curr.left == None:
                # Replace curr with right child
                return curr.right
            elif curr.right == None:
                # Replace curr with left child
                return curr.left
            else:
                # Swap curr with inorder successor
                minNode = self.findMin(curr.right)
                curr.key = minNode.key
                curr.val = minNode.val
                curr.right = self.removeHelper(curr.right, minNode.key)
        return curr

        # Returns the node with the minimum key in the subtree
    
    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node
        
    def getInorderKeys(self) -> List[int]:
        res = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.key)
            inorder(root.right)

        inorder(self.root)
        return res
