class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nc = {}
        for row in grid:
            for num in row:
                nc[num] = nc.get(num, 0) + 1
        repeated, missing = -1, -1
        for num in range(1, n * n + 1):
            if num in nc:
                if nc[num] == 2:
                    repeated = num
            else:
                missing = num
        return [repeated, missing]