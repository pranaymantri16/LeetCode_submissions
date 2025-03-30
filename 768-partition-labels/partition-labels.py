class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        li = {char: idx for idx, char in enumerate(s)}
        A = []
        i, end = 0, 0
        for idx, char in enumerate(s):
            end = max(end, li[char])
            if idx == end:
                A.append(end - i + 1)
                i = idx + 1
        return A
