from itertools import permutations
class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        c = 0
        A=set()
        for perm in permutations(digits, 3):
            num = perm[0] * 100 + perm[1] * 10 + perm[2]
            if perm[0] != 0 and num % 2 == 0:
                c += 1
                A.add(num)
        #A=A.sort()
        return sorted(A)