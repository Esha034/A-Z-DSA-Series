class Solution:
    def findCeil(self, arr, x):
        
        n=len(arr)
        low,high=0,n-1
        ans=float("inf")
        
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=x:
                ans=min(ans,mid)
                high=mid-1
            else:
                low=mid+1
        return ans if ans!= float("inf") else -1
        # code here
