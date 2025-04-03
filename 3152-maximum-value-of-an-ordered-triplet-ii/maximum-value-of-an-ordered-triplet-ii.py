class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        max_value = 0
        
        prefix_max = [0] * n
        prefix_max[0] = nums[0]
        for i in range(1, n):
            prefix_max[i] = max(prefix_max[i - 1], nums[i])
        
        suffix_max = [0] * n
        suffix_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            suffix_max[i] = max(suffix_max[i + 1], nums[i])
        
        for j in range(1, n - 1):
            max_i = prefix_max[j - 1]  # Maximum nums[i] for i < j
            max_k = suffix_max[j + 1]  # Maximum nums[k] for k > j
            
            triplet_value = (max_i - nums[j]) * max_k
            max_value = max(max_value, triplet_value)
        
        return max_value
