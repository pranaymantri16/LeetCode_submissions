class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        v = nums[0]
        d = -1
        for i in range(1, len(nums)):
            if nums[i] > v:
                d = max(d, nums[i] - v)
            else:
                v = nums[i]
        return d
