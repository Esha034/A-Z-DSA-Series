class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        presum=0
        premap={0:1}
        count=0
        for i in range(n):
            presum+=nums[i]
            if (presum-k) in premap:
                count+=premap[presum-k]

            if presum in premap:
                premap[presum]+=1
            else:
                premap[presum]=1
        return count


        
