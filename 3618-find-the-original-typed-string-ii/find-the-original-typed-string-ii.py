class Solution:
    def possibleStringCount(self, w: str, k: int) -> int:
        MOD = 10**9 + 7
        if not w:
            return 0

        counts = []
        c = 1
        for i in range(1, len(w)):
            if w[i] == w[i - 1]:
                c += 1
            else:
                counts.append(c)
                c = 1
        counts.append(c)

        res = 1
        for g in counts:
            res = (res * g) % MOD

        if k <= len(counts):
            return res

        dp = [0] * k
        dp[0] = 1

        for g in counts:
            new_dp = [0] * k
            sm = 0
            for i in range(k):
                if i > 0:
                    sm = (sm + dp[i - 1]) % MOD
                if i > g:
                    sm = (sm - dp[i - g - 1] + MOD) % MOD
                new_dp[i] = sm
            dp = new_dp

        bad = sum(dp[len(counts):]) % MOD
        return (res - bad + MOD) % MOD
