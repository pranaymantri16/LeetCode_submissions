class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        P = defaultdict(int)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                p = nums[i] * nums[j]
                P[p] += 1
        R = 0
        for count in P.values():
            if count > 1:
                R += (count * (count - 1)) // 2 * 8
        return R