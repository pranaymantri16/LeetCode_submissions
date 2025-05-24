class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        R = []
        def backtrack(path, remaining):
            if not remaining:
                R.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        backtrack([], nums)
        return R
