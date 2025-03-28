class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        d = [(-1,0), (1,0), (0,-1), (0,1)]
        Qi = sorted(enumerate(queries), key=lambda x: x[1])
        A = [0] * len(queries)
        V = [[False] * n for _ in range(m)]
        mih = [(grid[0][0], 0, 0)]
        V[0][0] = True
        count = 0
        for index, query in Qi:
            while mih and mih[0][0] < query:
                value, r, c = heappop(mih)
                count += 1
                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not V[nr][nc]:
                        heappush(mih, (grid[nr][nc], nr, nc))
                        V[nr][nc] = True
            A[index] = count
        return A
