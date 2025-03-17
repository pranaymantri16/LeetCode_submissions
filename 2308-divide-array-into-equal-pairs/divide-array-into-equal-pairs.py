class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        C = {}
        for num in nums:
            C[num] = C.get(num, 0) + 1
        for freq in C.values():
            if freq % 2 != 0:
                return False
        return True