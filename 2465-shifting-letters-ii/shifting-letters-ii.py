class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        delta = [0] * (n + 1)
        
        for start, end, direction in shifts:
            shift_val = 1 if direction == 1 else -1
            delta[start] += shift_val
            if end + 1 < n:
                delta[end + 1] -= shift_val
        
        cumulative_shift = 0
        result = []
        for i in range(n):
            cumulative_shift += delta[i]
            new_char = chr((ord(s[i]) - ord('a') + cumulative_shift) % 26 + ord('a'))
            result.append(new_char)
        return ''.join(result)
