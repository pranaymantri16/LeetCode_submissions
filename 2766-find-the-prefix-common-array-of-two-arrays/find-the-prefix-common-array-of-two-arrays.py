class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        Seen_A = set()
        Seen_B = set()
        R = []
        for a, b in zip(A, B):
            Seen_A.add(a)
            Seen_B.add(b)
            common_count = len(Seen_A & Seen_B)
            R.append(common_count)
        return R
