class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        R = []
        for i, word in enumerate(words):
            if x in word:
                R.append(i)
        return R
