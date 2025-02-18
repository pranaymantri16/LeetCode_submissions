class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        W = sentence.split()
        for i in range(len(W) - 1):
            if W[i][-1] != W[i + 1][0]:
                return False
        return W[-1][-1] == W[0][0]