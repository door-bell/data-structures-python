import unittest

from bst import BST

class TestInsertion(unittest.TestCase):
    def test_insertion(self):
        tree = BST()

        tree.insert(1)
        tree.insert(2)
        self.assertTrue(tree.contains(1))
        self.assertTrue(tree.contains(2))

if __name__ == '__main__':
    unittest.main()