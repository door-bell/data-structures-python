class BST:
    class TreeNode:
        def __init__(self, val=0):
            self.val = val
            self.left = None
            self.right = None
            self.count = 1
    
    def __init__(self):
        self._root = None
        self._size = 0
    
    def _insert(self, node, value):
        if value < node.val:
            if node.left is not None:
                self._insert(node.left, value)
            else:
                node.left = BST.TreeNode(value)  
        elif value > node.val:
            if node.right is not None:
                self._insert(node.right, value)
            else:
                node.right = BST.TreeNode(value)  
        else: # values are equal
            node.count += 1

    def insert(self, value):
        if self._root is None:
            self._root = BST.TreeNode(value)
        else:
            self._insert(self._root, value)
        self._size += 1

    def _delete(self, node, value):
        pass

    def delete(self, value):
        self._delete(self._root, value)

    def _contains(self, node, value):
        if node is None: # Reached bottom of tree
            return False

        if value < node.val:
            return self._contains(node.left, value)
        elif value > node.val:
            return self._contains(node.right, value)
        else: # Value is equal
            return True

    def contains(self, value):
        return self._contains(self._root, value)

    def size(self):
        return self._size