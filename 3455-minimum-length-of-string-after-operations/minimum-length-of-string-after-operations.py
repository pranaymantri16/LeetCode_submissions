class Solution:
    def minimumLength(self, s: str) -> int:
        cc = {}
        for char in s:
            cc[char] = cc.get(char, 0) + 1
        t = 0
        for char, f in cc.items():
            if f % 2 == 0:
                t += 2
            else:
                t += 1
        return t
