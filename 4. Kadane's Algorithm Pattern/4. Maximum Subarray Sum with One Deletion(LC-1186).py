class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n=len(arr)
        nodel=arr[0]
        onedel=float("-inf")
        res=arr[0]
        for i in range(1,n):
            prevnodel=nodel
            
            nodel=max(prevnodel+arr[i],arr[i]) 
            onedel=max(prevnodel,onedel+arr[i])      
            res=max(res,nodel,onedel)
            
        return res
