class BST:
    class TreeNode:
        def __init__(self, val=0, count=1):
            self.val = val
            self.left = None
            self.right = None
            self.count = 1
    
    def __init__(self):
        self._root = None
        self._size = 0

    def _minval(self, node):
        while node.left is not None:
            node = node.left
        return node

    def minval(self, node):
        if self._root is not None:
            return (_minval(self._root)).val
        return None
    
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

    def _delete(self, node, value, all=False):
        if node is None:
            return node
        
        if value < node.val:
            if node.left is not None:
                return self._delete(node.left, value)
            else:
                return None
        elif value > node.val:
            if node.right is not None:
                return self._delete(node.right, value)
            else:
                return None
        else: # values are equal
            if node.count > 1 and all is False:
                node.count -= 1
                return node
            # Handles leafs and one subtree
            if node.left is None:
                node = node.right
                return node
            elif node.right is None:
                node = node.left
                return node
            else: # Has a left and right subtree
                min_node = self._minval(node.right)
                temp = node
                node.val = min_node.val
                node.count = min_node.count
                self._delete(node.right, min_node.val, all=True)
                return temp

    def delete(self, value):
        result = self._delete(self._root, value)
        if result:
            self._size -= 1
        return None if not result else result.val

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