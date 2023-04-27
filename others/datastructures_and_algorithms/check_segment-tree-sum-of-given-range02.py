class SegmentTree:
	def __init__(self, array):
		self.size = len(array)
		self.tree = [0] * (4 * self.size)
		self.build_tree(array, 0, 0, self.size - 1)

	def build_tree(self, array, tree_index, left, right):
		if left == right:
			self.tree[tree_index] = array[left]
			return
		mid = (left + right) // 2
		self.build_tree(array, 2 * tree_index + 1, left, mid)
		self.build_tree(array, 2 * tree_index + 2, mid + 1, right)
		self.tree[tree_index] = min(self.tree[2 * tree_index + 1], self.tree[2 * tree_index + 2])

	def query(self, tree_index, left, right, query_left, query_right):
		if query_left <= left and right <= query_right:
			return self.tree[tree_index]
		mid = (left + right) // 2
		min_value = float('inf')
		if query_left <= mid:
			min_value = min(min_value, self.query(2 * tree_index + 1, left, mid, query_left, query_right))
		if query_right > mid:
			min_value = min(min_value, self.query(2 * tree_index + 2, mid + 1, right, query_left, query_right))
		return min_value

	def query_range(self, left, right):
		return self.query(0, 0, self.size - 1, left, right)


if __name__ == '__main__':
	array = [1, 3, 2, 5, 4, 6]
	st = SegmentTree(array)
	print(st.query_range(1, 5)) # 2