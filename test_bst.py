import unittest

from bst import BST

class TestInsertion(unittest.TestCase):
    def test_insertion(self):
        tree = BST()

        tree.insert(1)
        tree.insert(2)
        self.assertTrue(tree.contains(1))
        self.assertTrue(tree.contains(2))
    def test_deletion(self):
        tree = BST()
        # Root
        tree.insert(10)
        # Left subtree
        tree.insert(5)
        tree.insert(4)
        tree.insert(6)
        # Right subtree
        tree.insert(15)
        tree.insert(14)
        tree.insert(13)

        # Test deltion of node with 2 children
        tree.delete(15)
        self.assertFalse(tree.contains(15))
        self.assertTrue(tree.contains(5))
        self.assertTrue(tree.contains(4))
        self.assertTrue(tree.contains(6))
        self.assertTrue(tree.contains(14))
        self.assertTrue(tree.contains(13))


if __name__ == '__main__':
    unittest.main()