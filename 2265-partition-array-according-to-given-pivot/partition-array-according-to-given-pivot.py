class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        L, E, G = [], [], []
        for num in nums:
            if num < pivot:
                L.append(num)
            elif num == pivot:
                E.append(num)
            else:
                G.append(num)
        return L + E + G