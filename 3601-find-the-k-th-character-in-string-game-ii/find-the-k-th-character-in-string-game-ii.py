class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        n = len(operations)
        lengths = [1]
        for op in operations:
            lengths.append(lengths[-1] * 2)
        
        shift = 0
        for i in reversed(range(n)):
            half = lengths[i]
            if operations[i] == 0:
                if k > half:
                    k -= half
            else:
                if k > half:
                    k -= half
                    shift = (shift + 1) % 26
        
        return chr((ord('a') - ord('a') + shift) % 26 + ord('a'))
