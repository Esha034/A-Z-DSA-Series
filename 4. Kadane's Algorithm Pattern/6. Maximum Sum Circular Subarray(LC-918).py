class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n=len(nums)
        currmax=currmin=0
        maxsum=minsum=nums[0]
        totalsum=0
        for num in nums:
            totalsum+=num

            currmax=max(currmax+num,num)
            maxsum=max(maxsum,currmax)

            currmin=min(currmin+num,num)
            minsum=min(minsum,currmin)

        if maxsum<0:
            return maxsum

        return max(maxsum,totalsum-minsum)
        
