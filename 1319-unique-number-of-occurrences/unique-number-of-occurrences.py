class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        A = Counter(arr)
        return len(set(A.values())) == len(A.values())
