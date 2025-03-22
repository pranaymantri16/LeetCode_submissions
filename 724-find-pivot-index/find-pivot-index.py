class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ts = sum(nums)
        ls = 0
        for i, num in enumerate(nums):
            if ls == (ts - ls - num):
                return i
            ls += num
        return -1
