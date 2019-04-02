class LinkedList:
	class Node:
		def __init__(self, val=0):
			self.val = val
			self.next = None

	def __init__(self):
		self.head = None
		self.size = 0

	def insert(self, value, index=-1):
		if self.head is None:
			self.head = LinkedList.Node(value)
		elif index is -1:
			current = self.head
			while current.next is not None:
				current = current.next
			current.next = LinkedList.Node(value)
		else:
			if index < -1:
				raise IndexError(f'Index out of bounds: {index}')
			
			if index is 0:
				temp = self.head
				self.head = LinkedList.Node(value)
				self.head.next = temp
			else:
				counter = 0
				current = self.head
				while counter is not index - 1:
					current = current.next
					counter += 1
				temp = current.next
				current.next = LinkedList.Node(value)
				current.next.next = temp

		self.size += 1

	def delete(self, index=0):
		if index is -1:
			index = self.size - 1
		if index is 0:
			result = self.head.val
			self.head = self.head.next
			self.size -= 1
			return result
		elif index > self.size - 1 or index < 0:
			raise IndexError(f'Index out of bounds: {index}')

		counter = 0
		current = self.head
		while counter is not index - 1:
			current = current.next
			counter += 1
		result = current.next.val
		current.next = current.next.next

		self.size -= 1
		return result

	def get(self, index=0):
		if index is 0:
			return self.head.val
		elif index >= self.size:
			raise IndexError(f'Index out of bounds: {index}')
		counter = 0
		current = self.head
		while counter is not index:
			current = current.next
			counter += 1
		return current.val

	def getIndexOf(self, value):
		counter = 0
		current = self.head
		while current is not None and current.val is not value:
			current = current.next
			counter += 1
		return counter if current is not None else -1

	def deleteFirst(self, value):
		index = self.getIndexOf(value)
		self.delete(index)

	def contains(self, value):
		current = self.head
		while current is not None:
			if current.val is value:
				return True
			current = current.next
		return False

	def __str__(self):
		if self.size is 0:
			return '[]'
		elif self.size is 1:
			return f'[{self.head.val}]'

		result = str('[')
		current = self.head
		while current.next is not None:
			result += f'{current.val}, '
			current = current.next
		result += f'{current.val}]'
		return result


if __name__ == '__main__':
	linkedlist = LinkedList()
	
	linkedlist.insert(0, 0)
	linkedlist.insert(1)
	linkedlist.insert(2)
	linkedlist.insert(3)
	linkedlist.insert(4, 3)
	linkedlist.insert(5, -1)
	print(linkedlist)
	
	linkedlist.delete(0)
	linkedlist.delete(2)
	linkedlist.delete(-1)
	print(linkedlist)

	print(linkedlist.getIndexOf(2))

	linkedlist.deleteFirst(2)
	print(linkedlist)
