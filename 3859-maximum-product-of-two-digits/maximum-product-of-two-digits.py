class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [int(d) for d in str(n)]
        return max(a * b for i, a in enumerate(digits) for b in digits[i + 1:])
