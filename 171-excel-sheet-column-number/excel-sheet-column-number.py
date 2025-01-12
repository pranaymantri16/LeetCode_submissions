class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        cn = 0
        for char in columnTitle:
            c = ord(char) - ord('A') + 1
            cn = cn * 26 + c
        return cn
