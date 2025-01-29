class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        r = list(range(len(edges) + 1))
        def find_r(n):
            if r[n] != n:
                r[n] = find_r(r[n])
            return r[n]
        for n1, n2 in edges: 
            r1, r2 = find_r(n1), find_r(n2)
            if r1 == r2:
                return [n1, n2]
            r[r2] = r1            