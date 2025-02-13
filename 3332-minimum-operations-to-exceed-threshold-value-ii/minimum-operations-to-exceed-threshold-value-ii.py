from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        op = 0
        while nums[0] < k:
            if len(nums) < 2:
                return -1
            x = heappop(nums)
            y = heappop(nums)
            n = min(x, y) * 2 + max(x, y)
            heappush(nums, n)
            op += 1
        return op
