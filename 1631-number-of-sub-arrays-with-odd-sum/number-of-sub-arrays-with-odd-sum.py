class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        co, ce = 0, 1
        ps = 0
        R = 0
        for num in arr:
            ps += num
            if ps % 2 == 0:
                R += co
                ce += 1
            else:
                R += ce
                co += 1
            R %= MOD
        return R
