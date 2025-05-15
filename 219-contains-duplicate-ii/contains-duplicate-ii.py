class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        D = {}
        for i, num in enumerate(nums):
            if num in D and i - D[num] <= k:
                return True
            D[num] = i        
        return False
