class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n=len(nums)
        low,high=0,0
        curr_sum=0
        res=float("inf")
    
        while high<n:
            curr_sum+=nums[high]
            while curr_sum>=target:
                res=min(res,(high-low+1))
                curr_sum-=nums[low]
                low+=1
            high+=1
        return res if res != float("inf") else 0

