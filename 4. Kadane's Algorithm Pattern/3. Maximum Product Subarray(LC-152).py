class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        minend=nums[0]
        maxend=nums[0]
        res=nums[0]
        for i in range(1,n):
            v1=nums[i]
            v2=minend*nums[i]
            v3=maxend*nums[i]
            minend=min(v1,min(v2,v3))
            maxend=max(v1,max(v2,v3))
            res=max(res,max(maxend,minend))
        return res

        
