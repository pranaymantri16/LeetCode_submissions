from typing import List

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        position = {}
        for i in range(m):
            for j in range(n):
                position[mat[i][j]] = (i, j)
        row_count = [0] * m
        col_count = [0] * n
        for i, num in enumerate(arr):
            r, c = position[num]
            row_count[r] += 1
            col_count[c] += 1
            if row_count[r] == n or col_count[c] == m:
                return i
        return -1
