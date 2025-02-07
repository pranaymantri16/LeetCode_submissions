class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        bc = {}
        cf = defaultdict(int)
        distinct_cs = 0
        R = []
        for b, c in queries:
            if b in bc:
                prev_c = bc[b]
                cf[prev_c] -= 1
                if cf[prev_c] == 0:
                    distinct_cs -= 1
            bc[b] = c
            if cf[c] == 0:
                distinct_cs += 1
            cf[c] += 1            
            R.append(distinct_cs)
        return R
