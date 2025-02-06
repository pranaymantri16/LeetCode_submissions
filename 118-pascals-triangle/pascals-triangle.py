class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        T = [[1]]
        for i in range(1, numRows):
            p = T[-1]
            n = [1]
            for j in range(1, i):
                n.append(p[j - 1] + p[j])
            n.append(1)
            T.append(n)
        return T