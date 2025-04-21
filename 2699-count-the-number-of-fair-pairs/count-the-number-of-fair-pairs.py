from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        for i in range(n):
            low = lower - nums[i]
            high = upper - nums[i]
            start = bisect_left(nums, low, i + 1)
            end = bisect_right(nums, high, i + 1)
            ans += end - start
        
        return ans
