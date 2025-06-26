class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        n = len(s)
        count = 0
        value = 0
        power = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                count += 1
            else:
                if power < 32 and value + (1 << power) <= k:
                    value += (1 << power)
                    count += 1
            power += 1
        
        return count
