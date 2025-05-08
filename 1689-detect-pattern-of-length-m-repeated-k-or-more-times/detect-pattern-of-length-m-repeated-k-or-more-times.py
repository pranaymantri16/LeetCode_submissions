from typing import List

class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        n = len(arr)
        for i in range(n - m * k + 1):
            c = 0
            for j in range(i, i + m * k, m):
                if arr[j:j + m] == arr[i:i + m]:
                    c += 1
                else:
                    break
            if c >= k:
                return True
        return False
