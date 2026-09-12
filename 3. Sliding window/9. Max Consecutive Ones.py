#Optimal Solution 

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n=len(nums)
        maxlen=0
        currlen=0
        low=0
        for high in range(n):
            if nums[high]==0:
                low=high+1
            if nums[high]==1:
                currlen=high-low+1
                maxlen=max(maxlen,currlen)
        return maxlen

