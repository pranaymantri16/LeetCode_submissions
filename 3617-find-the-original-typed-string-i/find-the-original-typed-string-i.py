class Solution:
    def possibleStringCount(self, word: str) -> int:
        res = 1
        i = 0
        n = len(word)
        while i < n:
            j = i
            while j < n and word[j] == word[i]:
                j += 1
            k = j - i
            if k >= 2:
                res += (k - 1)
            i = j
        return res
