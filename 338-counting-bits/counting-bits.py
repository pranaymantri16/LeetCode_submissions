class Solution:
    def countBits(self, n: int) -> List[int]:
        R = [0] * (n + 1)
        for i in range(1, n + 1):
            R[i] = R[i >> 1] + (i & 1)
        
        return R