class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        total_count = nums.count(candidate)
        if total_count * 2 <= len(nums):
            return -1
        
        left_count = 0
        for i in range(len(nums) - 1):
            if nums[i] == candidate:
                left_count += 1
            right_count = total_count - left_count
            
            if left_count * 2 > (i + 1) and right_count * 2 > (len(nums) - (i + 1)):
                return i
        
        return -1
