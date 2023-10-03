#src:https://www.geeksforgeeks.org/linked-list-vs-array/

# Linked list implementation in python

# Creating a node
class Node:
	
	def __init__(self):
		self.value = 0
		self.next = None

head = None
one = None
two = None
three = None

# allocate 3 nodes in the heap
one = Node()
two = Node()
three = Node()

# Assign value values
one.value = 1
two.value = 2
three.value = 3

# Connect nodes
one.next = two
two.next = three
three.next = None

# print the linked list value
head = one

while (head != None):
	print(head.value)
	head = head.next

# The code is contributed by Nidhi goel.