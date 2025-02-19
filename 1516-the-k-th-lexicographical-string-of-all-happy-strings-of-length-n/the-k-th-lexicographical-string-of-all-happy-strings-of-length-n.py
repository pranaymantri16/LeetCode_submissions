class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        R = []
        def backtrack(current):
            if len(current) == n:
                R.append(current)
                return
            for char in ['a', 'b', 'c']:
                if not current or current[-1] != char:
                    backtrack(current + char)
        backtrack("")
        return R[k - 1] if k <= len(R) else ""
