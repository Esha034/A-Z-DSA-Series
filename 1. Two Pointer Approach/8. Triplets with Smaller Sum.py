class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        n=len(arr)
        count=0
        
        for i in range(n-2):
            j=i+1
            k=n-1
            
            while j<k:
                total=arr[i]+arr[j]+arr[k]
                if total>=sum:
                    k-=1
                    
                else:
                    count+=(k-j )
                    j+=1
                    
        return count
