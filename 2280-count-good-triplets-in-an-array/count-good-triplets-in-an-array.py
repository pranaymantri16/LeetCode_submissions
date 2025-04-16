
class FenwickTree:
    def __init__(self, size):
        self.tree = [0] * (size + 2)

    def update(self, index, value):
        index += 1  # 1-based indexing
        while index < len(self.tree):
            self.tree[index] += value
            index += index & -index

    def query(self, index):
        index += 1  # 1-based indexing
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result
    def query_range(self, left, right):
        return self.query(right) - self.query(left - 1)

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos = {num: i for i, num in enumerate(nums2)}
        transformed = [pos[num] for num in nums1]
        bit1 = FenwickTree(n)
        left_smaller = [0] * n
        for i in range(n):
            left_smaller[i] = bit1.query(transformed[i] - 1)
            bit1.update(transformed[i], 1)
        bit2 = FenwickTree(n)
        right_larger = [0] * n
        for i in range(n - 1, -1, -1):
            right_larger[i] = bit2.query(n - 1) - bit2.query(transformed[i])
            bit2.update(transformed[i], 1)
        result = 0
        for i in range(n):
            result += left_smaller[i] * right_larger[i]
        return result
