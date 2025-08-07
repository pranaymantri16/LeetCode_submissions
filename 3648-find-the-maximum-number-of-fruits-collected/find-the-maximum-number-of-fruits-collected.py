class Solution(object):
    def maxCollectedFruits(self, grid):
        n = len(grid)
        total = 0
        for i in range(n):
            total += grid[i][i]

        for pass_ in range(2):
            if pass_ == 1:
                grid = [list(row) for row in zip(*grid)]
            dp = [-1] * n
            dp[n - 1] = grid[0][n - 1]
            for row in range(1, n - 1):
                new_dp = [-1] * n
                for col in range(n):
                    if dp[col] == -1:
                        continue
                    for d in [-1, 0, 1]:
                        nc = col + d
                        if 0 <= nc < n:
                            new_dp[nc] = max(new_dp[nc], dp[col] + grid[row][nc])
                dp = new_dp

            total += dp[n - 1]
        
        return total
