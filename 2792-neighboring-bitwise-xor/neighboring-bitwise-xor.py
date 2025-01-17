class Solution:
    def doesValidArrayExist(self, derived: list[int]) -> bool:
        n = len(derived)
        def is_valid(start):
            original = [0] * n
            original[0] = start
            for i in range(1, n):
                original[i] = original[i-1] ^ derived[i-1]
            return (original[n-1] ^ original[0]) == derived[n-1]
        return is_valid(0) or is_valid(1)
