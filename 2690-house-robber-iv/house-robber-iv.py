class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        L, R = min(nums), max(nums)
        def canRob(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 1
                i += 1
            return count >= k
        while L < R:
            mid = (L + R) // 2
            if canRob(mid):
                R = mid
            else:
                L = mid + 1        
        return L
