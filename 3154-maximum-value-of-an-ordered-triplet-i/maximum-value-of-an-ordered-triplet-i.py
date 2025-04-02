class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = 0
        max_before_j = [0] * n
        max_before_j[0] = nums[0]
        
        for i in range(1, n):
            max_before_j[i] = max(max_before_j[i - 1], nums[i])
        for j in range(1, n - 1):
            for k in range(j + 1, n):
                triplet_value = (max_before_j[j - 1] - nums[j]) * nums[k]
                max_value = max(max_value, triplet_value)
        
        return max_value
