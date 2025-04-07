class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False
        t = s // 2
        n = len(nums)
        dp = [False] * (t + 1)
        dp[0] = True
        for num in nums:
            for i in range(t, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[t]
