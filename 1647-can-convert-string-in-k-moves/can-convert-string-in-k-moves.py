class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        shift_count = defaultdict(int)
        for char_s, char_t in zip(s, t):
            shift = (ord(char_t) - ord(char_s) + 26) % 26
            if shift > 0:
                shift_count[shift] += 1
        for shift, count in shift_count.items():
            max_moves_needed = shift + 26 * (count - 1)
            if max_moves_needed > k:
                return False
        return True