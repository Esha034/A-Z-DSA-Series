#optimal code


class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        def count_elements(mid):
            count=0
            for i in range(1,m+1):
                count+=min(n,mid//i)
            return count


        low,high=1,m*n
        ans=-1
        while low<=high:
            mid=(low+high)//2
            count=count_elements(mid)
            if count<k:
                low=mid+1
            else:
                ans=mid
                high=mid-1
        return ans
        
