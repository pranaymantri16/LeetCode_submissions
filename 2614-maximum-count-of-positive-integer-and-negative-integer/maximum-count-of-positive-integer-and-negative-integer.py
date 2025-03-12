class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p=0
        n=0
        for i in range(len(nums)):
            if(nums[i]>0):
                p+=1
            elif(nums[i]<0):
                n+=1
        return max(p,n)