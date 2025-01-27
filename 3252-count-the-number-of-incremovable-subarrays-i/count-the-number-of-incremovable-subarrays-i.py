class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n = len(nums)
        is_strictly_increasing = True
        for i in range(n - 1):
            if nums[i] >= nums[i + 1]:
                is_strictly_increasing = False
                break
        if is_strictly_increasing:
            return n * (n + 1) // 2
        count = 0
        for i in range(n):
            for j in range(i, n):
                remaining = nums[:i] + nums[j+1:]
                is_valid = True
                for k in range(len(remaining) - 1):
                    if remaining[k] >= remaining[k + 1]:
                        is_valid = False
                        break
                if is_valid:
                    count += 1
        return count