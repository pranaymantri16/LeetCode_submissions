from heapq import heappop, heappush
from collections import deque

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = {
            1: (0, 1),
            2: (0, -1),
            3: (1, 0),
            4: (-1, 0)
        }
        m, n = len(grid), len(grid[0])
        costs = [[float('inf')] * n for _ in range(m)]
        costs[0][0] = 0
        pq = [(0, 0, 0)]
        while pq:
            cost, x, y = heappop(pq)
            if (x, y) == (m - 1, n - 1):
                return cost
            if cost > costs[x][y]:
                continue
            for d, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost if grid[x][y] == d else cost + 1
                    if new_cost < costs[nx][ny]:
                        costs[nx][ny] = new_cost
                        heappush(pq, (new_cost, nx, ny))
        return -1
