class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        maxh = minh = 0
        mas = mis = 0
        for num in nums:
            maxh = max(num, maxh + num)
            minh = min(num, minh + num)
            mas = max(mas, maxh)
            mis = min(mis, minh)
        return max(mas, abs(mis))
