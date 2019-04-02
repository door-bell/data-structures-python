import unittest

from linkedlist import LinkedList

class TestInsertion(unittest.TestCase):
    def test_insertion(self):
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

class TestDeletion(unittest.TestCase):
    def test_deletion(self):
        ll = LinkedList()

        # Build our linked list
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        ll.insert(4)
        ll.insert(5)
        ll.insert(6)

        # Test deleting the first item
        self.assertEqual(ll.delete(0), 1)
        self.assertEqual(ll.get(0), 2)
        self.assertFalse(ll.contains(1))
        # [2, 3, 4, 5, 6]

        # Test deleting last item
        self.assertEqual(ll.delete(-1), 6)
        self.assertEqual(ll.get(-1), 5)
        self.assertFalse(ll.contains(6))
        # [2, 3, 4, 5]

        # Test deleting an item in the middle
        self.assertEqual(ll.delete(1), 3)
        self.assertEqual(ll.get(1), 4)
        self.assertFalse(ll.contains(3))
        # [2, 4, 5]

        # Test deleteFirst() instance of an number
        # deleteFirst() also returns the index the item was at
        self.assertEqual(ll.deleteFirst(4), 1)
        self.assertEqual(ll.get(1), 5)
        self.assertFalse(ll.contains(4))
        # Also make sure deleteFirst() returns -1 when nothing is found
        self.assertEqual(ll.deleteFirst(10), -1)
        # [2, 5] 

        # Make sure we have the same list as we think we do
        self.assertEqual(ll.size, 2)
        self.assertTrue(ll.get(0), 2)
        self.assertTrue(ll.get(1), 5)


if __name__ == '__main__':
    unittest.main()