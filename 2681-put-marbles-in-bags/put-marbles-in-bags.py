class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        n = len(weights)
        A = [weights[i] + weights[i + 1] for i in range(n - 1)]
        A.sort()
        mis = sum(A[:k - 1])
        mas = sum(A[-(k - 1):])
        return mas - mis
