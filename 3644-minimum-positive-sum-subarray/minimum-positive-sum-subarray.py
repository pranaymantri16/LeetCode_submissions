class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_ps = float('inf')
        f = False
        for size in range(l, r + 1):
            cs = sum(nums[:size])
            if cs > 0:
                min_ps = min(min_ps, cs)
                f = True
            for i in range(size, len(nums)):
                cs += nums[i] - nums[i - size]
                if cs > 0:
                    min_ps = min(min_ps, cs)
                    f = True
        return min_ps if f else -1