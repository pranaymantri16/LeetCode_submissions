class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed_nums = list(enumerate(nums))
        top_k = sorted(indexed_nums, key=lambda x: x[1], reverse=True)[:k]
        top_k.sort(key=lambda x: x[0])
        return [x[1] for x in top_k]
