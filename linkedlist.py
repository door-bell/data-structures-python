class LinkedList:
	class Node:
		def __init__(self, val=0):
			self.val = val
			self.next = None

	def __init__(self):
		self.head = None
		self._size = 0

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

		self._size += 1

	def delete(self, index=0):
		if index is 0:
			result = self.head.val
			self.head = self.head.next
			self._size -= 1
			return result
		if index is -1:
			index = self._size - 1
		elif index > self._size - 1 or index < 0:
			raise IndexError(f'Index out of bounds: {index}')

		counter = 0
		current = self.head
		while counter is not index - 1:
			current = current.next
			counter += 1
		result = current.next.val
		current.next = current.next.next

		self._size -= 1
		return result

	def get(self, index=0):
		if index is 0:
			return self.head.val
		if index is -1:
			index = self._size - 1
		elif index >= self._size:
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
		if index is not -1:
			self.delete(index)
		return index

	def contains(self, value):
		current = self.head
		while current is not None:
			if current.val is value:
				return True
			current = current.next
		return False

	def size(self):
		return self._size

	def __str__(self):
		if self._size is 0:
			return '[]'
		elif self._size is 1:
			return f'[{self.head.val}]'

		result = str('[')
		current = self.head
		while current.next is not None:
			result += f'{current.val}, '
			current = current.next
		result += f'{current.val}]'
		return result