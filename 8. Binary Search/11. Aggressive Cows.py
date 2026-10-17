
class Solution:
    def aggressiveCows(self, arr, k):
        n=len(arr)
        arr.sort()
        def nocows(guess):
            
            prevpos=arr[0]
            
            cow=1
            for i in range(1,n):
                dis=arr[i]-prevpos
                if dis>=guess:
                    cow+=1
                    prevpos=arr[i]
            return cow
            
        low,high=1,max(arr)-min(arr)
        
        while low<=high:
            
            guess=(low+high)//2
            
            cows=nocows(guess)
            
            if cows>=k:
                low=guess+1
            else:
                high=guess-1
        return high
            
                
             
