class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        n=len(nums)
        presum=0
        res=0
    
        premap={0:1}
        for i in range(n):

            presum+=nums[i]
            rem=presum%k

            # if rem<0:
            #     rem=rem+k
            
            if rem in premap:
                res+=premap[rem]
                premap[rem]+=1
            else:
                premap[rem]=1

        return res

        
