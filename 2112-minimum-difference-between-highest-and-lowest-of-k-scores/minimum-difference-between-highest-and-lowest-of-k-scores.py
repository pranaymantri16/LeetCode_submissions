class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if(len(nums)<2):
            return 0
        nums.sort()
        d=float('inf')
        for i in range(len(nums)-k+1):
            m=nums[i+k-1]-nums[i]
            if(m<d):
                d=m
        return d