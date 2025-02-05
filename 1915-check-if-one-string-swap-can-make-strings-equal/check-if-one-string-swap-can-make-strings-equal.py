class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        diff = [(i, (s1[i], s2[i])) for i in range(len(s1)) if s1[i] != s2[i]]
        if len(diff) == 2:
            return diff[0][1] == diff[1][1][::-1]
        return False
