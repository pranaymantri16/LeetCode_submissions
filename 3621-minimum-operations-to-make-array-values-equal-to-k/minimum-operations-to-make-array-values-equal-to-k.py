class Solution(object):
    def minOperations(self, nums, k):
        nums.sort()
        min_val = nums[0]
        if min_val < k:
            return -1

        operations = 0
        index = 0
        while index < len(nums):
            if nums[index] > k:
                operations += 1
                while index + 1 < len(nums) and nums[index] == nums[index + 1]:
                    index += 1
            index += 1
        return operations
