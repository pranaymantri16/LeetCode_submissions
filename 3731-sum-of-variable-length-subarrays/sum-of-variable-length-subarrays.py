class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        n = len(nums)
        ps = [0] * (n + 1)
        for i in range(n):
            ps[i + 1] = ps[i] + nums[i]
        ts = 0
        for i in range(n):
            s = max(0, i - nums[i])
            ts += ps[i + 1] - ps[s]
        return ts
