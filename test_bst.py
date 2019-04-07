import unittest

from bst import BST

def genTestTree():
    """
            10
          /    \
         5       15
       /  \    /   \
      4    6  13     16
     /      \
    3         7
    """
    tree = BST()
    # Root
    tree.insert(10)
    # Left subtree
    tree.insert(5)
    tree.insert(4)
    tree.insert(6)
    tree.insert(7)
    tree.insert(3)
    # Right subtree
    tree.insert(15)
    tree.insert(16)
    tree.insert(13)
    return tree

class BSTTestInsertion(unittest.TestCase):
    def test_bst_insertion(self):
        tree = BST()
        tree.insert(1)
        tree.insert(2)
        self.assertTrue(tree.contains(1))
        self.assertTrue(tree.contains(2))

class BSTTestDeletion(unittest.TestCase):
    def test_bst_delete_twochildren(self):
        tree = genTestTree()
        # Test deltion of node with 2 children
        tree.delete(15)
        self.assertFalse(tree.contains(15))
        self.assertTrue(tree.contains(3))
        self.assertTrue(tree.contains(4))
        self.assertTrue(tree.contains(5))
        self.assertTrue(tree.contains(6))
        self.assertTrue(tree.contains(7))
        self.assertTrue(tree.contains(10))
        self.assertTrue(tree.contains(13))
        self.assertTrue(tree.contains(16))
    def test_bst_delete_nochildren(self):
        tree = genTestTree()
        # Test deletion of node with no children
        tree.delete(3)
        self.assertFalse(tree.contains(3))
        self.assertTrue(tree.contains(4))
        self.assertTrue(tree.contains(5))
        self.assertTrue(tree.contains(6))
        self.assertTrue(tree.contains(7))
        self.assertTrue(tree.contains(10))
        self.assertTrue(tree.contains(13))
        self.assertTrue(tree.contains(15))
        self.assertTrue(tree.contains(16))
    def test_bst_delete_rightchild(self):
        tree = genTestTree()
        # Test deletion of node with one child (right)
        tree.delete(6)
        self.assertFalse(tree.contains(6))
        self.assertTrue(tree.contains(3))
        self.assertTrue(tree.contains(4))
        self.assertTrue(tree.contains(5))
        self.assertTrue(tree.contains(7))
        self.assertTrue(tree.contains(10))
        self.assertTrue(tree.contains(13))
        self.assertTrue(tree.contains(15))
        self.assertTrue(tree.contains(16))
    def test_bst_delete_leftchild(self):
        tree = genTestTree()
        # Test deletion of node with one child (right)
        tree.delete(4)
        self.assertFalse(tree.contains(4))
        self.assertTrue(tree.contains(3))
        self.assertTrue(tree.contains(5))
        self.assertTrue(tree.contains(6))
        self.assertTrue(tree.contains(7))
        self.assertTrue(tree.contains(10))
        self.assertTrue(tree.contains(13))
        self.assertTrue(tree.contains(15))
        self.assertTrue(tree.contains(16))
    def test_bst_delete_one(self):
        tree = genTestTree()
        tree.insert(6)
        tree.delete(6)
        self.assertTrue(tree.contains(6))
    def test_bst_delete_all(self):
        tree = genTestTree()
        tree.insert(6)
        tree.delete(6, all=True)
        self.assertFalse(tree.contains(6))

class BSTTestSize(unittest.TestCase):
    def test_bst_size_one(self):
        tree = genTestTree()
        self.assertEqual(len(tree), 9)
        # Delete item with size == 1
        tree.delete(6)
        self.assertEqual(len(tree), 8)
    def test_bst_size_one_of_multiple(self):
        tree = genTestTree()
        self.assertEqual(len(tree), 9)
        # Insert item that is already in the tree
        tree.insert(10)
        tree.delete(10)
        self.assertEqual(len(tree), 9)
    def test_bst_size_all_of_multiple(self):
        tree = genTestTree()
        self.assertEqual(len(tree), 9)
        # Delete ALL of item with count > 1
        tree.insert(10)
        self.assertEqual(len(tree), 10)
        # Delete item with count = 1
        tree.delete(10, all=True)
        self.assertEqual(len(tree), 8)

if __name__ == '__main__':
    unittest.main()