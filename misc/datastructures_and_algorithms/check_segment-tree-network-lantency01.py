class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)
        
    def build(self, nums, idx, left, right):
        if left == right:
            self.tree[idx] = nums[left]
        else:
            mid = (left + right) // 2
            self.build(nums, 2 * idx + 1, left, mid)
            self.build(nums, 2 * idx + 2, mid + 1, right)
            self.tree[idx] = min(self.tree[2 * idx + 1], self.tree[2 * idx + 2])
        
    def query(self, idx, left, right, query_left, query_right):
        if left > query_right or right < query_left:
            return float('inf')
        elif query_left <= left and query_right >= right:
            return self.tree[idx]
        else:
            mid = (left + right) // 2
            left_min = self.query(2 * idx + 1, left, mid, query_left, query_right)
            right_min = self.query(2 * idx + 2, mid + 1, right, query_left, query_right)
            return min(left_min, right_min)
            

if __name__ == "__main__":
    # 範例使用
    nums = [4, 2, 7, -1, 5, 6, 3, 9]
    segment_tree = SegmentTree(nums)

    # index for search boundary
    query_left = 0
    query_right = 7
    min_value = segment_tree.query(0, 0, segment_tree.n - 1, query_left, query_right)
    print(f"The minimum value in the range [{query_left}, {query_right}] is {min_value}")