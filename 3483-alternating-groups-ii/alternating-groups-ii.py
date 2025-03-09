from typing import List

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        n = len(colors)
        c = 0
        v = [colors[i] != colors[(i + 1) % n] for i in range(n)]
        ac = sum(v[:k-1])
        for i in range(n):
            if ac == k - 1:
                c += 1
            ac -= v[i]
            ac += v[(i + k - 1) % n]
        return c