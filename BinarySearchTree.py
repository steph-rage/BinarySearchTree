from random import randint

class BinarySearch():

	def __init__(self):
		self.tree = [None]

	def add_element(self, element):
		current_index = 0
		while True:
			if self.tree[current_index] == None:
				self.tree[current_index] = element
				while len(self.tree) < 2 * current_index + 3:
					self.tree.append(None)
				return self.tree
			elif element < self.tree[current_index]:
				current_index = 2 * current_index + 1
			elif element > self.tree[current_index]:
				current_index = 2 * current_index + 2
			else:
				return self.tree

	def search(self, element):
		current_index = 0
		while self.tree[current_index] != None:
			if element == self.tree[current_index]:
				return True
			elif element < self.tree[current_index]:
					current_index = 2 * current_index + 1
			elif element > self.tree[current_index]:
				current_index = 2 * current_index + 2
		return False


test_tree = BinarySearch()
test = [randint(0,500) for _ in range(1000)]
for value in test:
	test_tree.add_element(value)

while True:
	test_me = int(input("Pick a test number: "))
	print(test_tree.search(test_me))

