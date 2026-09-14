#optimal code

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        bestending=nums[0]
        ans=nums[0]

        for i in range(1,n):
            c1=bestending+nums[i]
            c2=nums[i]
            bestending=max(c1,c2)

            if bestending >ans:
                ans=bestending
        return ans
