class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        op = 0
        n = len(nums)
        for i in range(0, n + 1, 3):
            A = nums[i:]
            if len(A) == len(set(A)):
                return op
            op += 1
        return op
