class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        min_open = max_open = 0
        for i in range(len(s)):
            if locked[i] == '1':
                if s[i] == '(':
                    min_open += 1
                    max_open += 1
                else:
                    min_open -= 1
                    max_open -= 1
            else:
                min_open -= 1
                max_open += 1
            min_open = max(min_open, 0)
            if max_open < 0:
                return False
        min_close = max_close = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1':
                if s[i] == ')':
                    min_close += 1
                    max_close += 1
                else:
                    min_close -= 1
                    max_close -= 1
            else:
                min_close -= 1
                max_close += 1
            min_close = max(min_close, 0)
            if max_close < 0:
                return False
        return True
