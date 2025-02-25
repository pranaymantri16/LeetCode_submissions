class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        R = []
        while columnNumber > 0:
            columnNumber -= 1
            R.append(chr(ord('A') + columnNumber % 26))
            columnNumber //= 26
        return ''.join(reversed(R))
