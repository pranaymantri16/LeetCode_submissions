class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        ml = 1
        cl = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cl += 1
                ml = max(ml, cl)
            else:
                cl = 1
        return ml
