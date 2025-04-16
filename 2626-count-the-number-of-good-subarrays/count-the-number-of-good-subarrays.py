class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        left = 0
        pairs = 0
        res = 0
        for right in range(len(nums)):
            pairs += count[nums[right]]
            count[nums[right]] += 1
            while pairs >= k:
                res += len(nums) - right
                count[nums[left]] -= 1
                pairs -= count[nums[left]]
                left += 1
        return res
