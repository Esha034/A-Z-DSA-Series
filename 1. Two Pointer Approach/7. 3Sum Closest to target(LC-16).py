Approach 1 — Brute Force

Try every possible combination of 3 elements.


#code

    class Solution:
    def threeSumClosest(self, nums, target):
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):

                    total = nums[i] + nums[j] + nums[k]

                    if abs(total - target) < abs(closest - target):
                        closest = total

        return closest


#complexity

Time  : O(n³)
Space : O(1)



Approach 3 — Optimal:  Sorting + Two Pointers



#code

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


#complexity

Time  : O(n²)
Space : O(1)
