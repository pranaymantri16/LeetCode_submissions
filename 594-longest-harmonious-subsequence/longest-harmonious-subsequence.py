class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)
        res = 0
        for num in freq:
            if num + 1 in freq:
                res = max(res, freq[num] + freq[num + 1])
        return res
