class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n=len(nums)
        currmin=currmax=0
        maxsum=minsum=0

        for num in nums:
            currmax=max(currmax+num,num)
            maxsum=max(maxsum,currmax)

            currmin=min(currmin+num,num)
            minsum=min(currmin,minsum)

        return max(abs(maxsum),abs(minsum))
    


        
