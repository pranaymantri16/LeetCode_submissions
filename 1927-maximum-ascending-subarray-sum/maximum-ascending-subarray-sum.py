class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        ms = cs = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cs += nums[i]
            else:
                ms = max(ms, cs)
                cs = nums[i]
        return max(ms, cs)
