class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        L, R = 1, min(ranks) * (cars ** 2)
        def CanT(T):
            Tc = sum(int(math.sqrt(T // r)) for r in ranks)
            return Tc >= cars
        while L < R:
            mid = (L + R) // 2
            if CanT(mid):
                R = mid
            else:
                L = mid + 1
        return L
