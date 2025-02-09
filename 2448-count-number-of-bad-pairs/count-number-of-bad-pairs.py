class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        tp = n * (n - 1) // 2
        g = 0
        D = defaultdict(int)
        for i, num in enumerate(nums):
            diff = num - i
            g += D[diff]
            D[diff] += 1
        return tp - g