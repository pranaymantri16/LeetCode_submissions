from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        i = 0
        n = len(nums)
        while i < n:
            remaining = nums[i:]
            if len(remaining) == len(set(remaining)):
                return operations
            operations += 1
            i += 3
        return operations
