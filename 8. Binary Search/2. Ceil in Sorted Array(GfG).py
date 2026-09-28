class Solution:
    def findCeil(self, arr, x):
        
        n=len(arr)
        low,high=0,n-1
        ans=-1
        
        while low<=high:
            mid=(low+high)//2
            if arr[mid]>=x:
                ans=mid
                high=mid-1
            else:
                low=mid+1
                
        return ans 
       
