class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        char_count = Counter(s)
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        return k >= odd_count and k <= len(s)