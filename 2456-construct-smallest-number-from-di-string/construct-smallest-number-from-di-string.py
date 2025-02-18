class Solution:
    def smallestNumber(self, pattern: str) -> str:
        S = []
        R = ""
        num = 1
        for c in pattern:
            S.append(str(num))
            num += 1
            if c == 'I':
                while S:
                    R += S.pop()
        S.append(str(num))
        while S:
            R += S.pop()
        return R