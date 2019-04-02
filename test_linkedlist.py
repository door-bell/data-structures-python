import unittest

from linkedlist import LinkedList

class TestInsertion(unittest.TestCase):
    def test_insertion_edges(self):
        ll = LinkedList()

        # Test inserting into a new linked list
        ll.insert(5)
        self.assertEqual(ll.get(0), 5)
        self.assertTrue(ll.contains(5))
        self.assertEqual(ll.getIndexOf(5), 0)

        # Test inserting at the end
        ll.insert(2, -1) # Same as without the second argument
        self.assertEqual(ll.get(1), 2)
        self.assertTrue(ll.contains(2))
        self.assertEqual(ll.getIndexOf(2), 1)

        # Test inserting at the beginning
        ll.insert(1, 0)
        self.assertEqual(ll.get(0), 1)
        self.assertTrue(ll.contains(1))
        self.assertEqual(ll.getIndexOf(1), 0)

        # Test inserting in the middle
        ll.insert(3, 1)
        self.assertEqual(ll.get(1), 3)
        self.assertTrue(ll.contains(3))
        self.assertEqual(ll.getIndexOf(3), 1)

if __name__ == '__main__':
    unittest.main()