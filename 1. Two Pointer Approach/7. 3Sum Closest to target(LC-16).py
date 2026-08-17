class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        res_sum=0
        diff=float("inf")

        for i in range(n-2):
            j=i+1
            k=n-1
            
            while j<k:
                total=nums[i]+nums[j]+nums[k]
                d=abs(target-total)

                if d<diff:
                    diff=d
                    res_sum=total

                if total==target:
                    return res_sum

                elif total<target:
                    j+=1
                else:
                    k-=1

        return res_sum
        
