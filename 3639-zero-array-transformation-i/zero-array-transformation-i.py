class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        n = len(nums)
        adjustments = [0] * (n + 1)
        for start, end in queries:
            adjustments[start] += 1
            adjustments[end + 1] -= 1
        for i in range(1, n + 1):
            adjustments[i] += adjustments[i - 1]
        return all(adjustments[idx] >= value for idx, value in enumerate(nums))
