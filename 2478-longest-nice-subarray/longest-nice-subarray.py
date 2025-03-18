class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ub = 0
        l = 0
        ml = 0
        for r in range(len(nums)):
            while (ub & nums[r]) != 0:
                ub ^= nums[l]
                l += 1
            ub |= nums[r]
            ml = max(ml, r - l + 1)
        return ml
