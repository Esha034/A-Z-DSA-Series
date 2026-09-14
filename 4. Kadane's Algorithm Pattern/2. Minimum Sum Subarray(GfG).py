Given an array arr[], find the sub-array containing at least one number which has the minimum sum and return its sum.



  #optimal code
class Solution:
    def minSubarraySum(self, arr: list[int]) -> int:
        n=len(arr)
        bestending=arr[0]
        ans=bestending
        for i in range(1, n):
            bestending=min(bestending+arr[i],arr[i])
            if bestending<ans:
                ans=bestending
        return ans
            
