#optimal code

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n=len(arr)
        low,high=0,n-1
        peak=-1

        while low<=high:
            mid=(low+high)//2

            if arr[mid]<arr[mid+1]:
                low=mid+1
            else:
                peak=mid
                high=mid-1
                
        return peak





class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n=len(arr)
        low,high=0,n-1
        while low<=high:
            mid=(low+high)//2

            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid]<arr[mid+1]:
                low=mid+1
            else:
                high=mid-1
        return mid

