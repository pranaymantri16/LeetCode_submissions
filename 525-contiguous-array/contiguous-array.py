class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        sum_index_map = {0: -1}
        cumulative_sum = 0
        max_length = 0
        for i, num in enumerate(nums):
            cumulative_sum += 1 if num == 1 else -1
            if cumulative_sum in sum_index_map:
                max_length = max(max_length, i - sum_index_map[cumulative_sum])
            else:
                sum_index_map[cumulative_sum] = i
        return max_length
