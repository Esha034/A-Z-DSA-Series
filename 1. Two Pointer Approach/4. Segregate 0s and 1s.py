class Solution:
    def segregate0and1(self, arr):
        i=0
        n=len(arr)
        for j in range(n):
            if arr[j]==0:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
        return arr
