# Python3 program to swap first
# and last element of a list

# Swap function
def swapList(list):
	
	# Storing the first and last element
	# as a pair in a tuple variable get
	get = list[-1], list[0]
	
	# unpacking those elements
	list[0], list[-1] = get
	
	return list
	
# Driver code
newList = [12, 35, 9, 56, 24]
print(swapList(newList))