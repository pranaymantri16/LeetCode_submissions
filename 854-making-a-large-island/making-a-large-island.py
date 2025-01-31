class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        island_id = 2
        island_sizes = {0: 0}
        def dfs(x, y, island_id):
            stack = [(x, y)]
            size = 0
            while stack:
                i, j = stack.pop()
                if grid[i][j] == 1:
                    grid[i][j] = island_id
                    size += 1
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 1:
                            stack.append((ni, nj))
            return size
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    island_sizes[island_id] = dfs(i, j, island_id)
                    island_id += 1
        max_area = max(island_sizes.values() or [0])
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen_islands = set()
                    area = 1
                    for di, dj in directions:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] > 1:
                            seen_islands.add(grid[ni][nj])
                    area += sum(island_sizes[island] for island in seen_islands)
                    max_area = max(max_area, area)
        return max_area