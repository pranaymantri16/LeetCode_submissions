class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        R = 0
        for char in s + t:
            R ^= ord(char)
        return chr(R)