class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # s=set()
        # for i in nums:
        #     if i in s:
        #         return i
        #     s.add(i)
        for i in range(len(nums)-2):
            if nums[i]==nums[i+1] or nums[i]==nums[i+2]:
                return nums[i]
        return nums[-1]