class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        sc = defaultdict(int)
        for cs, ct in zip(s, t):
            s = (ord(ct) - ord(cs) + 26) % 26
            if s > 0:
                sc[s] += 1
        for s, count in sc.items():
            m = s + 26 * (count - 1)
            if m > k:
                return False
        return True