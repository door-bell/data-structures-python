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

    def _delete(self, node, parent, value, all=False):
        if node is None:
            return node
        
        if value < node.val:
            if node.left is not None:
                return self._delete(node.left, node, value, all=all)
            else:
                return None
        elif value > node.val:
            if node.right is not None:
                return self._delete(node.right, node, value, all=all)
            else:
                return None
        else: # values are equal
            if node.count > 1 and all is False:
                node.count -= 1
                return 1
            # Handles leafs and one subtree
            if node.left is None:
                if parent.left.val == node.val:
                    parent.left = node.right
                else:
                    parent.right = node.right
                return node.count
            elif node.right is None:
                if parent.left.val == node.val:
                    parent.left = node.left
                else:
                    parent.right = node.left
                return node.count
            else: # Has a left and right subtree
                min_node = self._minval(node.right)
                result = node.count
                node.val = min_node.val
                node.count = min_node.count
                self._delete(node.right, node, min_node.val, all=True)
                return result

    def delete(self, value, all=False):
        result = self._delete(self._root, None, value, all=all)
        if result:
            self._size -= result
        return None if not result else result

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

    def __len__(self):
        return self._size