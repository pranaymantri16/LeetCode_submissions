from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        pt = [0] * n
        pb = [0] * n
        pt[0] = grid[0][0]
        pb[0] = grid[1][0]
        for i in range(1, n):
            pt[i] = pt[i - 1] + grid[0][i]
            pb[i] = pb[i - 1] + grid[1][i]
        r2m = float('inf')
        for i in range(n):
            points_above = pt[n - 1] - pt[i]
            points_below = pb[i - 1] if i > 0 else 0
            r2max = max(points_above, points_below)
            r2m = min(r2m, r2max)
        return r2m
